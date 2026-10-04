"""Phase 6 simulation calculator (analyst role-play support).

Turns the role-play decisions in research_notes/Phase 2-8/p6_simulation.md into
numbers, using ONLY the parameters and functions of model/economics.py plus the
per-SKU inputs in data/opportunities_master.csv. Every number it prints is a
SIMULATED OUTCOME driven by ASSUMPTION inputs; none is evidence.

Run: python3 model/sim_calcs.py            (prints all scenario blocks)
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import economics as E

M = {r["product_id"]: r for r in csv.DictReader(open(E.D("data", "opportunities_master.csv"), newline=""))}
T20 = list(csv.DictReader(open(E.D("data", "top20_economics.csv"), newline="")))
f = E.f

# ---------- extra simulation parameters (ALL ASSUMPTION unless noted) ----------
RESIN_BASE = 300                        # model base case (economics.py b0)
FIXED = sum(E.FIXED_MONTHLY.values())   # 439k DZD/month, 2 shifts, excl. power (power is per hour)
FOUNDER = 120_000                       # founder + overhead (seed 06)
FIXED_ALL = FIXED + FOUNDER             # 559k DZD/month cash fixed
CAP_H = E.HOURS_AVAILABLE               # 400 clock-h/month; OEE is inside parts/hour
POWER_H = E.POWER_KW_AVG * E.TARIFF_DZD_KWH   # 90 DZD per running hour
PRESS_LANDED_DZD = E.landed_usd(120) * E.FX   # ~33.9k USD landed, no AAPI
OVERDRAFT = 0.0751                      # VERIFIED H2 2025 average (seed 06)
CHANGE_FULL_H = 3.0                     # full mold change + purge + first-article
CHANGE_INSERT_H = 0.75                  # insert swap; vendor claims <5 min, we add purge/check
FX = E.FX


def sku(pid, **over):
    r = dict(M[pid]); r.update({k: str(v) for k, v in over.items()}); return r


def pph(r):
    return max(1, f(r["cavities"], 1)) * 3600 / f(r["cycle_s"], 20) * E.OEE


def var_cost(r, price, resin=RESIN_BASE, credit_days=30):
    """Cash variable cost per piece: material + power + pack/deliver/sell % + credit cost."""
    g = f(r["part_weight_g"])
    blend = (1 - E.MB_SHARE) * resin + E.MB_SHARE * E.MB_PRICE
    material = g * (1 + E.LOSS) * blend / 1000 / (1 - E.REJECT)
    return material + POWER_H / pph(r) + price * (E.PACK + E.DELIVERY + E.SELLING) \
        + price * E.ANNUAL_RATE * credit_days / 365


def material(r, resin=RESIN_BASE):
    g = f(r["part_weight_g"]); blend = (1 - E.MB_SHARE) * resin + E.MB_SHARE * E.MB_PRICE
    return g * (1 + E.LOSS) * blend / 1000 / (1 - E.REJECT)


def cph(r, price=None, resin=RESIN_BASE):
    """Contribution per clock machine-hour (before fixed cost and mold)."""
    p = f(r["price_dzd"]) if price is None else price
    return (p - var_cost(r, p, resin)) * pph(r)


def hours(r, pcs):
    return pcs / pph(r)


def mold_dzd(usd):
    return usd * E.MOLD_LANDED_FACTOR * FX


def full_margin(r, resin=RESIN_BASE, util=0.7, credit=60, price=None):
    p = f(r["price_dzd"]) if price is None else price
    c = E.unit_cost(r, resin, util, credit, p)
    return (p - c["total"]) / p * 100, c


def hdr(t):
    print("\n" + "=" * 8 + " " + t + " " + "=" * 8)


# ---------------------------------------------------------------- baseline
def baseline():
    hdr("BASELINE: contribution per machine-hour and break-even (resin 300)")
    print(f"fixed cash/month = {FIXED_ALL:,.0f} DZD; capacity {CAP_H} clock-h; press landed {PRESS_LANDED_DZD/1e6:.2f} M DZD")
    for pid in ["JC-26", "JC-24", "JC-40", "JC-02", "JC-01", "IF-01", "IF-04", "IF-08", "CL-003", "JC-36", "OS-010", "JC-30"]:
        r = M[pid]; c = cph(r)
        print(f"{pid:7s} price {f(r['price_dzd']):6.2f} pph {pph(r):6.0f} var {var_cost(r, f(r['price_dzd'])):5.2f} "
              f"contrib/h {c:7.0f}  break-even h/month if sole product {FIXED_ALL / c:6.0f}")
    tot_h = sum(f(e["machine_hours_per_year"]) for e in T20)
    print(f"Top-20 at planned volumes: {tot_h:.0f} h/yr = {tot_h/12:.0f} h/month = {tot_h/12/CAP_H*100:.0f}% of 400 h")


# ---------------------------------------------------------------- S1 ramp
# Role-play output: active accounts by month and their monthly pieces (ASSUMPTION sizes).
# account = (sku, pcs/month at steady state); trial month at 30% of steady volume.
ACCOUNT_SIZE = {"JC-26": 15_000, "JC-24": 25_000, "JC-02": 15_000, "IF-01": 20_000,
                "IF-04": 15_000, "CL-003": 25_000, "JC-40": 15_000}
VARIANTS_S1 = {
    # name: list of (sku, month_won) — each account ramps: month_won trial 30%, then 100%
    "A spacers direct, no intro, price=street-20%": [("JC-26", 4), ("JC-24", 6), ("JC-26", 9), ("JC-24", 12), ("JC-26", 15)],
    "B spacers+packers via 2 wholesalers, maarifa intro": [("JC-26", 2), ("JC-24", 3), ("JC-02", 5), ("JC-26", 6), ("JC-24", 8),
                                                          ("JC-02", 10), ("JC-40", 11), ("JC-26", 13), ("JC-24", 15), ("JC-02", 16)],
    "C drip fittings via tube maker (seasonal)": [("IF-01", 4), ("IF-04", 4), ("IF-01", 9), ("IF-04", 10), ("IF-01", 15), ("IF-04", 16)],
    "D flip-top caps direct to SME fillers": [("CL-003", 5), ("CL-003", 8), ("CL-003", 11), ("CL-003", 14), ("CL-003", 17)],
}
SEASONAL = {"IF-01": [1.6, 1.6, 1.4, 1.0, 0.6, 0.5, 0.5, 0.6, 1.0, 1.4, 1.2, 1.0],  # Nov..Oct, mean ~1.0
            "IF-04": [1.6, 1.6, 1.4, 1.0, 0.6, 0.5, 0.5, 0.6, 1.0, 1.4, 1.2, 1.0]}


def s1_path(accts, months=18):
    out = []
    for m in range(1, months + 1):
        h = 0; rev = 0; con = 0
        for pid, won in accts:
            if m < won: continue
            k = 0.3 if m == won else 1.0
            k *= SEASONAL.get(pid, [1] * 12)[(m - 1) % 12]
            pcs = ACCOUNT_SIZE[pid] * k; r = M[pid]
            h += hours(r, pcs); rev += pcs * f(r["price_dzd"]); con += pcs * (f(r["price_dzd"]) - var_cost(r, f(r["price_dzd"])))
        out.append((m, h, rev, con))
    return out


def s1():
    hdr("S1 quiet entry: machine-hours, revenue, cash (3 molds landed + press capex)")
    capex = PRESS_LANDED_DZD + 3 * mold_dzd(7_500)
    for name, acc in VARIANTS_S1.items():
        p = s1_path(acc); cash = -capex; peak = cash; firsts = {}
        for m, h, rev, con in p:
            ar = rev * 0.5  # half of revenue on 30 days by month 6+ (baseline payment rule)
            cash += con - FIXED_ALL
            peak = min(peak, cash - ar)
            for t in (48, 107, 150):
                if h >= t and t not in firsts: firsts[t] = m
        row = {m: (h, rev, con) for m, h, rev, con in p}
        print(f"{name}\n   h/month m3 {row[3][0]:.0f}, m6 {row[6][0]:.0f}, m12 {row[12][0]:.0f}, m18 {row[18][0]:.0f}; "
              f"util m12 {row[12][0]/CAP_H*100:.0f}%; months to 48/107/150 h: {firsts.get(48,'>18')}/{firsts.get(107,'>18')}/{firsts.get(150,'>18')}; "
              f"rev m12 {row[12][1]/1e6:.2f} M; contrib m12 {row[12][2]/1e6:.2f} M vs fixed {FIXED_ALL/1e6:.2f} M; "
              f"cum cash m18 {cash/1e6:.1f} M; peak need {-peak/1e6:.1f} M DZD")
    # volume needed to break even with the B mix
    r = M["JC-26"]
    print(f"   pieces/month of JC-26 alone to cover fixed: {FIXED_ALL/(f(r['price_dzd'])-var_cost(r,f(r['price_dzd']))):,.0f}")


# ---------------------------------------------------------------- S2 caps
def s2():
    hdr("S2 flip-top caps: unit cost by colour MOQ vs landed import")
    r = sku("CL-003", mold_cost_usd=8000)
    for price in (4.0, 4.82, 6.0):
        for moq in (5_000, 10_000, 20_000):
            change_cost = CHANGE_FULL_H * 0 + 1.0 * (FIXED / CAP_H) + 3.0 * RESIN_BASE  # 1 h colour purge + 3 kg purge
            extra = change_cost / moq
            mold_pp = mold_dzd(8000) / (600_000 * 2)  # 600k caps/yr assumed, 2-yr life
            c = var_cost(r, price) + FIXED / (CAP_H * 0.7) / pph(r) + mold_pp + extra
            print(f"price {price:4.2f} MOQ {moq:6d}: unit cost {c:4.2f}, margin {(price-c)/price*100:5.1f}%  (colour-change adds {extra:.3f})")
    for fob in (0.012, 0.025, 0.045):
        print(f"FOB {fob}: landed official x237 = {fob*237:5.2f}, parallel x428 = {fob*428:5.2f} DZD")
    print(f"caps/month to fill 100 h: {100*pph(r):,.0f}; contrib/h at 4.82: {cph(r):.0f}")


# ---------------------------------------------------------------- S3 copy
def s3():
    hdr("S3 copycat on JC-26/JC-24: who can afford the cut?")
    for pid in ("JC-26", "JC-24"):
        r = M[pid]; p = f(r["price_dzd"])
        for cut in (0.10, 0.20, 0.30):
            q = p * (1 - cut)
            fm, _ = full_margin(r, util=0.7, price=q)
            cop, _ = full_margin(r, util=0.15, price=q)  # copycat with 1-2 SKUs ~15% util
            inc = (q - var_cost(r, q)) / q * 100  # incumbent pricing at marginal cost
            print(f"{pid} cut {int(cut*100)}% -> price {q:5.2f}: founder full margin (70% util) {fm:6.1f}%; "
                  f"copycat full margin (15% util) {cop:6.1f}%; incumbent marginal margin {inc:5.1f}%")
    r = M["JC-26"]
    print(f"copycat break-even pcs/month for JC-26 alone at -20%: {FIXED_ALL/(f(r['price_dzd'])*0.8-var_cost(r,f(r['price_dzd'])*0.8)):,.0f}")


# ---------------------------------------------------------------- S4 portfolio
def s4():
    hdr("S4 3 -> 10 -> 20 molds on one press")
    order = [e["product_id"] for e in sorted(T20, key=lambda e: -f(e["combined"]))]
    for n in (3, 10, 20):
        ids = order[:n]
        h = sum(f(e["machine_hours_per_year"]) for e in T20 if e["product_id"] in ids) / 12
        con = sum(f(M[i]["annual_volume_pcs"]) / 12 * (f(M[i]["price_dzd"]) - var_cost(M[i], f(M[i]["price_dzd"]))) for i in ids)
        mold_full = sum(mold_dzd(f(M[i]["mold_cost_usd"], 6000) or 6000) for i in ids)
        frames = 2 if n <= 10 else 4
        mold_ins = frames * mold_dzd(9000) + sum(0.4 * mold_dzd(f(M[i]["mold_cost_usd"], 6000) or 6000) for i in ids)
        for mode, runs in (("make-to-order (2 runs/SKU/month)", 2), ("2-4 wk stock (1 run/SKU/month)", 1)):
            for tool, ch in (("full molds", CHANGE_FULL_H), ("insert frames", CHANGE_INSERT_H)):
                lost = n * runs * ch
                print(f"n={n:2d} {mode:34s} {tool:13s}: run-h {h:5.0f}, changeover-h {lost:5.0f}, "
                      f"occupied {(h+lost)/CAP_H*100:4.0f}%  free h {CAP_H-h-lost:5.0f}")
        fg = sum(f(M[i]["annual_volume_pcs"]) / 52 * var_cost(M[i], f(M[i]["price_dzd"])) for i in ids)
        prov = 1.2 * sum((f(M[i]["mold_cost_usd"], 6000) or 6000) * 1.06 * FX for i in ids[3:]) if n > 3 else 0
        print(f"   n={n}: gross contrib/month {con/1e6:.2f} M vs fixed {FIXED_ALL/1e6:.2f} M; molds cash full {mold_full/1e6:.1f} M vs insert {mold_ins/1e6:.1f} M DZD; "
              f"FG stock per week of cover {fg/1e3:.0f} k DZD; 120% provisions if all new molds imported at once {prov/1e6:.1f} M DZD")
        print(f"   volume multiplier for press-1 >75% (full molds, stocked): {(0.75*CAP_H - n*CHANGE_FULL_H)/h:.2f}x planned volumes")


# ---------------------------------------------------------------- S6 resin
def s6():
    hdr("S6 resin shock: full margin (70% util, 60d) per top-20 SKU")
    levels = [300, 360, 450, 600]
    neg = {l: 0 for l in levels}; frag = {l: 0 for l in levels}
    for e in T20:
        r = M[e["product_id"]]; ms = []
        for l in levels:
            m, _ = full_margin(r, resin=l); ms.append(m)
            neg[l] += m < 0; frag[l] += m < 15
        dm = material(r, 600) - material(r, 300)
        print(f"{e['product_id']:7s} {e['family'][:26]:26s} " + " ".join(f"{m:6.1f}" for m in ms) +
              f"   price rise to hold margin at +100%: {dm/f(r['price_dzd'])*100:5.1f}%")
    for l in levels: print(f"resin {l}: SKUs <0% margin {neg[l]}, <15% {frag[l]}")
    # stock buffer: kg/month of the S1 variant-B month-12 mix
    kg = 0
    for pid, won in VARIANTS_S1["B spacers+packers via 2 wholesalers, maarifa intro"]:
        if won <= 12: kg += ACCOUNT_SIZE[pid] * f(M[pid]["part_weight_g"]) * 1.06 / 1000
    for w in (4, 8):
        st = kg * w / 4.33
        print(f"buffer {w} wk: {st:,.0f} kg = {st*300/1e6:.2f} M DZD at 300; carrying cost/yr {st*300*OVERDRAFT/1e3:.0f} k; "
              f"gain if resin +50% during cover {st*150/1e6:.2f} M; +100% {st*300/1e6:.2f} M")
    print(f"monthly resin need (variant B, m12): {kg:,.0f} kg")


# ---------------------------------------------------------------- S5/S7 import price umbrella
def s7():
    hdr("S5/S7 landed import price per piece vs founder cost/price")
    # landed = FOB * FX * freight 1.2 * duty factor * clearing 1.1 (P2-CL formula)
    cases = {"official FX, DD30 (today)": (133, 1.35), "official FX, DD15": (133, 1.20),
             "official FX, DD30+DAPS60": (133, 1.95), "parallel FX 240, DD30": (240, 1.35)}
    fobs = {"JC-24 spacer wheel": ("JC-24", 0.010, 0.015), "JC-26 spacer chair": ("JC-26", 0.02, 0.04),
            "JC-02 bridge packer": ("JC-02", 0.015, 0.045), "IF-04 drip coupling": ("IF-04", 0.01, 0.03),
            "CL-003 flip-top": ("CL-003", 0.012, 0.045)}
    for name, (pid, lo, hi) in fobs.items():
        r = M[pid]; uc = f(next(e for e in T20 if e["product_id"] == pid)["unit_cost_base"])
        s = f"{name:20s} price {f(r['price_dzd']):5.2f} cost {uc:5.2f} | "
        for c, (fx, d) in cases.items():
            s += f"{c}: {lo*fx*1.2*d*1.1:4.1f}-{hi*fx*1.2*d*1.1:4.1f}; "
        print(s)


# ---------------------------------------------------------------- S8 credit
def s8():
    hdr("S8 working capital at 30/60/90-day terms")
    for R in (1.0e6, 1.5e6, 2.5e6):
        for share in (0.3, 0.6, 0.9):
            for d in (30, 60, 90):
                ar = R * (1 - share) * 0 + R * share * d / 30   # credit sales outstanding
                print(f"rev {R/1e6:.1f} M/month, {int(share*100)}% on {d}d: receivables {ar/1e6:.2f} M DZD, "
                      f"overdraft cost/yr {ar*OVERDRAFT/1e3:.0f} k") if d in (60, 90) or share == 0.6 else None
    R = 1.5e6
    for share in (0.6, 0.9):
        for bounce in (0.05, 0.15):
            for d in (60, 90):
                loss = R * share * 12 * bounce * 0.5  # half recovered after cheque procedure
                print(f"rev 1.5 M, {int(share*100)}% credit {d}d, bounce {int(bounce*100)}% (50% recovered): bad debt/yr {loss/1e6:.2f} M; "
                      f"as % of annual gross contrib (~40% of rev) {loss/(R*12*0.4)*100:.0f}%")
    cap = 1.0  # one month of purchases cap
    print(f"exposure cap = 1 month purchases per customer: max receivable = 1.0x monthly rev of that customer")


# ---------------------------------------------------------------- S9 downtime
def s9():
    hdr("S9 downtime cost at month 8")
    for H in (120, 200):  # hours sold/month at month 8 (variant B ~ 120)
        con_h = 4_500  # blended contrib/h of spacer+packer mix (see baseline)
        per_day = H / 25 * con_h
        for days in (2, 7, 30):
            lost = per_day * days
            sub = H / 25 * days * 3_000 + days * 2 * 8_000 / 7  # subcontract 3000 DZD/h + transport of molds/parts
            print(f"H={H} h/month, {days:2d} days: contribution lost {lost/1e3:6.0f} k DZD (fixed {FIXED_ALL/25*days/1e3:5.0f} k keeps running); "
                  f"subcontract cost of the gap ~{sub/1e3:5.0f} k vs own variable ~{H/25*days*POWER_H/1e3:4.0f} k")
    for wk in (2, 4):
        print(f"FG buffer {wk} wk covers a stop of {wk*7} days at cost of stock ~ {120/4.33*wk*1113*var_cost(M['JC-24'],7.48)/1e3:.0f} k DZD (JC-24-equivalent)")


# ---------------------------------------------------------------- S11/12 mold funding
def s11_12():
    hdr("S11/S12 mold payback per top-20 SKU at planned volume (gross contribution before fixed)")
    rows = []
    for e in T20:
        r = M[e["product_id"]]; usd = f(r["mold_cost_usd"]) or 0
        if usd == 0: continue
        monthly = f(r["annual_volume_pcs"]) / 12 * (f(r["price_dzd"]) - var_cost(r, f(r["price_dzd"])))
        share_fixed = hours(r, f(r["annual_volume_pcs"]) / 12) / CAP_H * FIXED_ALL  # fixed cost absorbed by its hours at 100%
        net = monthly - hours(r, f(r["annual_volume_pcs"]) / 12) * FIXED_ALL / (CAP_H * 0.7)
        pb = mold_dzd(usd) / monthly; pbn = mold_dzd(usd) / net if net > 0 else float("inf")
        prem = mold_dzd(usd) / (f(r["annual_volume_pcs"]) * 1) / f(r["price_dzd"]) * 100  # premium to recover mold in 12 months
        rows.append((e["product_id"], usd, pb, pbn, prem))
        print(f"{e['product_id']:7s} mold {usd:6.0f} USD = {mold_dzd(usd)/1e6:4.2f} M DZD; payback gross {pb:5.1f} mo; "
              f"after fixed@70% {pbn:6.1f} mo; price premium to recover in 12 mo {prem:5.1f}%")
    for lim in (6, 12, 24):
        print(f"molds paying back (after fixed) within {lim} months: {sum(1 for r in rows if r[3] <= lim)}/{len(rows)}")
    for n in (3, 6, 10):
        cap = n * mold_dzd(7_500)
        print(f"{n} molder-funded molds: {cap/1e6:.1f} M DZD; overdraft interest/yr {cap*OVERDRAFT/1e3:.0f} k; leasing 10.09% {cap*0.1009/1e3:.0f} k")


# ---------------------------------------------------------------- S13 anchor
def s13():
    hdr("S13 anchor concentration")
    R = 1.5e6; gm = 0.40
    for share in (0.3, 0.5, 0.7):
        for days in (60, 90):
            ar = R * share * days / 30
            cut = R * share * 0.5 * gm
            print(f"anchor {int(share*100)}% of rev, pays {days}d: receivable {ar/1e6:.2f} M DZD; if pays 90d late extra {R*share*3/1e6:.2f} M; "
                  f"if halves volume: contrib -{cut/1e3:.0f} k/month (fixed {FIXED_ALL/1e3:.0f} k)")


# ---------------------------------------------------------------- S14 catalogue
def s14():
    hdr("S14 catalogue-lite: stock cash by SKU count and cover")
    for n, avg_mpcs in ((10, 18_000), (20, 14_000), (30, 10_000)):
        unit = 3.5  # avg variable cost per piece of spacers/packers/caps/drip mix
        for wk in (2, 4, 8):
            stock = n * avg_mpcs * wk / 4.33 * unit
            print(f"{n} SKUs x {avg_mpcs:,} pcs/month avg, {wk} wk cover: stock {stock/1e6:.2f} M DZD")
        print(f"   tooling: full molds {n*mold_dzd(7_500)/1e6:.1f} M vs insert frames {((n//6)+1)*mold_dzd(9_000)/1e6 + n*0.4*mold_dzd(7_500)/1e6:.1f} M DZD")


# ---------------------------------------------------------------- S15 price war
def s15():
    hdr("S15 price war on spacers (JC-26/JC-24) and drip (IF-01/IF-04)")
    for pid in ("JC-26", "JC-24", "IF-01", "IF-04"):
        r = M[pid]; p = f(r["price_dzd"])
        floor_inc = var_cost(r, p) + (FIXED - 55_000 - 12_000) / CAP_H / pph(r)  # incumbent: cash cost, no depreciation/interest, full press
        s = f"{pid} price {p:5.2f}, founder var {var_cost(r,p):4.2f}, incumbent cash floor {floor_inc:4.2f} ({(1-floor_inc/p)*100:3.0f}% below) | "
        for cut in (0.2, 0.3, 0.4):
            q = p * (1 - cut)
            s += f"-{int(cut*100)}%: contrib/h {cph(r, q):6.0f} ({cph(r, q)/cph(r)*100:3.0f}% of base); "
        print(s)


def s15_survival():
    hdr("S15b price war from month 8 on spacer families, S1 variant-B path (cash vs no-war)")
    acc = VARIANTS_S1["B spacers+packers via 2 wholesalers, maarifa intro"]
    # response: (price factor on spacers, share of spacer volume kept) -- ASSUMPTION role-play outputs
    def run(cut, months, resp):
        cash = 0; base = 0
        for m in range(1, 19):
            con = 0; con0 = 0
            for pid, won in acc:
                if m < won: continue
                k = 0.3 if m == won else 1.0; pcs = ACCOUNT_SIZE[pid] * k; r = M[pid]; p = f(r["price_dzd"])
                c0 = pcs * (p - var_cost(r, p)); con0 += c0
                if pid.startswith("JC-2") or pid == "JC-40":
                    if 8 <= m < 8 + months:
                        pf, keep = resp(cut)
                        q = p * pf; con += pcs * keep * (q - var_cost(r, q))
                        continue
                con += c0
            cash += con - FIXED_ALL; base += con0 - FIXED_ALL
        return cash, base
    resps = {"match": lambda c: (1 - c, 1.0), "partial match + service": lambda c: (1 - c / 2, 0.75),
             "hold price + traite contracts": lambda c: (1.0, 0.6 if c <= 0.2 else 0.4),
             "exit spacers (no redeploy demand)": lambda c: (1.0, 0.0)}
    for cut in (0.2, 0.3, 0.4):
        for months in (3, 6, 12):
            line = f"cut {int(cut*100)}% x {months:2d} mo: "
            for n, fn in resps.items():
                c, b = run(cut, months, fn); line += f"{n}: {(c-b)/1e6:+.2f} M; "
            print(line)


def s1_opcash():
    hdr("S1 operating cash excl. capex (cum. contribution - fixed), 18 months")
    for name, acc in VARIANTS_S1.items():
        cum = 0; trough = 0
        for m, h, rev, con in s1_path(acc):
            cum += con - FIXED_ALL; trough = min(trough, cum)
        print(f"{name}: cum op cash m18 {cum/1e6:+.2f} M, trough {trough/1e6:.2f} M DZD")


if __name__ == "__main__":
    baseline(); s1(); s1_opcash(); s2(); s3(); s4(); s6(); s7(); s8(); s9(); s11_12(); s13(); s14(); s15(); s15_survival()
