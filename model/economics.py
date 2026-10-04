"""Phase 2 funnel + Phase 4 economics and machine-fit model.

Reads data/opportunities_master.csv (normalised by the scoring pass) and writes:
  data/funnel_scores.csv, data/top20_economics.csv, data/machine_comparison.csv,
  model/phase4_results.md
All inputs not marked VERIFIED in the master file are ASSUMPTIONS. Change the
parameters below and re-run: python3 model/economics.py
"""
import csv, os, statistics as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)

# ---------------- parameters (ASSUMPTIONS unless noted) ----------------
FX = 133.0                     # DZD/USD official (VERIFIED Jul 2026)
HOURS_AVAILABLE = 2 * 8 * 25   # 2 shifts, 25 days -> 400 h/month
OEE = 0.85                     # good parts / theoretical
FIXED_MONTHLY = {              # DZD/month, own 120 t cell, 2 shifts
    "depreciation": 55_000, "labour_2shift": 173_000, "rent": 120_000,
    "admin": 60_000, "interest": 12_000, "maintenance": 19_000,
}
POWER_KW_AVG = 18; TARIFF_DZD_KWH = 5.0          # VERIFIED tariff ~4.7-5.5
MB_SHARE = 0.02; MB_PRICE = 600                  # masterbatch
LOSS = 0.03; REJECT = 0.03                       # purge/start-up loss, rejects
PACK = 0.03; DELIVERY = 0.03; SELLING = 0.05     # % of price
QC_DZD_PER_HOUR = 0                              # QC inside labour
ANNUAL_RATE = 0.08                               # credit cost (overdraft ~7.5% VERIFIED)
MOLD_LIFE_YEARS = 2                              # amortise mold over 2 years of volume
MOLD_LANDED_FACTOR = 1.25                        # freight, duty 5%, fees
RESIN_CASES = [220, 300, 400]
UTIL_CASES = [0.5, 0.7, 0.9]
CREDIT_CASES = [30, 60, 90]

PRESSES = {   # tonnage: FOB USD (ESTIMATE), tie-bar mm, practical PP shot g (min,max), connected kVA
    60:  dict(fob=9_500,  tiebar=310, shot=(20, 90),  kva=35, aux=6_000),
    80:  dict(fob=11_500, tiebar=360, shot=(30, 135), kva=45, aux=7_000),
    100: dict(fob=12_500, tiebar=380, shot=(35, 160), kva=55, aux=8_000),
    120: dict(fob=14_300, tiebar=410, shot=(45, 200), kva=65, aux=9_000),
    160: dict(fob=19_000, tiebar=470, shot=(60, 280), kva=85, aux=11_000),
}
def landed_usd(t):
    p = PRESSES[t]; fob = p["fob"]
    freight = 3_500 if t <= 120 else 4_500
    cif = fob + freight
    duties = cif * 0.10          # 5% duty + 3% TCS + 2% PRCT (VERIFIED rates); 0 with AAPI
    port_inland = 1_500 + t * 5
    install = 2_000 + t * 10     # commissioning, electrics, spares kit
    return round(fob + freight + duties + port_inland + install + p["aux"])

def f(x, d=0.0):
    try: return float(str(x).replace(",", "").split()[0])
    except Exception: return d

def machine_hour_cost(util):
    fixed = sum(FIXED_MONTHLY.values())
    hrs = HOURS_AVAILABLE * util
    return fixed / hrs + POWER_KW_AVG * TARIFF_DZD_KWH

def unit_cost(r, resin, util, credit_days, price):
    g = f(r["part_weight_g"]); cav = max(1, f(r["cavities"], 1)); cyc = f(r["cycle_s"], 20)
    blend = (1 - MB_SHARE) * resin + MB_SHARE * MB_PRICE
    material = g * (1 + LOSS) * blend / 1000 / (1 - REJECT)
    pph = cav * 3600 / cyc * OEE
    conversion = machine_hour_cost(util) / pph
    vol = max(1.0, f(r["annual_volume_pcs"], 100_000))
    mold = f(r["mold_cost_usd"], 6000) * MOLD_LANDED_FACTOR * FX / (vol * MOLD_LIFE_YEARS)
    pct = price * (PACK + DELIVERY + SELLING)
    credit = price * ANNUAL_RATE * credit_days / 365
    return dict(material=material, conversion=conversion, mold=mold, pct=pct, credit=credit,
                total=material + conversion + mold + pct + credit, pph=pph)

def main():
    rows = list(csv.DictReader(open(D("data", "opportunities_master.csv"), newline="")))
    # ---- funnel ----
    MA = ["s_demand","s_shortage","s_import_dep","s_local_comp","s_cust_conc","s_recurring","s_margin","s_switching","s_custom_b2b"]
    FE = ["s_mold_afford","s_machine_compat","s_resin_avail","s_tech","s_regulatory","s_quality_risk","s_copy_risk","s_payment_risk","s_wc","s_speed","s_sku_family","s_utilization"]
    for r in rows:
        r["market_attractiveness"] = round(st.mean(f(r[k]) for k in MA) * 10, 1)
        r["founder_entry"] = round(st.mean(f(r[k]) for k in FE) * 10, 1)
        ev = f(r.get("evidence_strength", 0))           # 0 none .. 3 verified pain + price
        r["combined"] = round(0.45 * r["market_attractiveness"] + 0.45 * r["founder_entry"] + 10 * ev / 3, 1)
    def alive(r):
        v = r.get("researcher_verdict", "").upper()
        return (r["machine_fit"] in ("Fits 120T confidently", "Borderline 120T") and r.get("hard_kill", "").strip() == ""
                and not v.startswith("KILL") and "FUTURE" not in v and f(r["min_press_t"], 999) <= 160)
    inj = [r for r in rows if alive(r)]
    inj.sort(key=lambda r: -r["combined"])
    top50 = {r["product_id"] for r in inj[:50]}
    def econ_row(r):
        price = f(r["price_dzd"])
        row = dict(product_id=r["product_id"], product=r["product"], family=r["family"], price_dzd=price,
                   price_basis=r["price_basis"], annual_volume_pcs=f(r["annual_volume_pcs"]))
        for resin in RESIN_CASES:
            for util in UTIL_CASES:
                c = unit_cost(r, resin, util, 60, price)
                row[f"margin_r{resin}_u{int(util*100)}"] = round((price - c["total"]) / price * 100, 1)
        for cd in CREDIT_CASES:
            c = unit_cost(r, 300, 0.7, cd, price)
            row[f"margin_r300_u70_credit{cd}"] = round((price - c["total"]) / price * 100, 1)
        r2 = dict(r); r2["annual_volume_pcs"] = str(2 * f(r["annual_volume_pcs"]))
        c2 = unit_cost(r2, 300, 0.7, 60, price)
        row["margin_r300_u70_volume_x2"] = round((price - c2["total"]) / price * 100, 1)
        b0 = unit_cost(r, 300, 0.7, 60, price)
        mold_total = f(r["mold_cost_usd"], 6000) * MOLD_LANDED_FACTOR * FX / MOLD_LIFE_YEARS
        ume = price - (b0["total"] - b0["mold"])
        row["breakeven_volume_pcs_per_year"] = round(mold_total / ume) if ume > 0 else "never"
        row.update(unit_cost_base=round(b0["total"], 2), material=round(b0["material"], 2),
                   conversion=round(b0["conversion"], 2), mold=round(b0["mold"], 2),
                   parts_per_hour=round(b0["pph"]), machine_hours_per_year=round(f(r["annual_volume_pcs"]) / b0["pph"]),
                   annual_revenue_dzd=round(price * f(r["annual_volume_pcs"])),
                   annual_contribution_dzd=round((price - b0["total"]) * f(r["annual_volume_pcs"])))
        m = row["margin_r400_u50"]
        row["economics_verdict"] = "KILL (collapses under stress)" if m < 0 else "FRAGILE" if m < 15 else "ROBUST"
        row["min_press_t"] = r["min_press_t"]; row["combined"] = r["combined"]; row["evidence_strength"] = r["evidence_strength"]
        return row
    ECON = {}
    top20 = []
    for r in inj:
        if f(r["price_dzd"]) <= 0: continue
        e = econ_row(r); ECON[r["product_id"]] = e
        if e["economics_verdict"].startswith("KILL"):
            r["kill_reason"] = f"Economics collapse: margin {e['margin_r400_u50']}% at resin 400 / 50% use (base {e['margin_r300_u70']}%)"
            continue
        top20.append(r["product_id"])
        if len(top20) == 20: break
    top20 = set(top20)
    for r in rows:
        if r["product_id"] in top20: r["stage"] = "TOP20"
        elif r.get("kill_reason", "").startswith("Economics collapse"): r["stage"] = "KILLED"
        elif r["product_id"] in top50:
            r["stage"] = "TOP50"
            if f(r["price_dzd"]) <= 0: r["kill_reason"] = "Held at top-50: no DZD price yet, cannot run economics"
        else:
            r["stage"] = "KILLED"
            if not r.get("kill_reason"):
                if r["machine_fit"] not in ("Fits 120T confidently", "Borderline 120T"):
                    r["kill_reason"] = "Future-machine opportunity: " + r["machine_fit"]
                elif r.get("hard_kill"):
                    r["kill_reason"] = r["hard_kill"]
                elif r.get("researcher_verdict", "").upper().startswith("KILL"):
                    r["kill_reason"] = "Killed by sector researcher (see stage notes)"
                else:
                    r["kill_reason"] = f"Below top-50 cut-off on combined score ({r['combined']})"
    keys = list(rows[0].keys())
    with open(D("data", "funnel_scores.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); w.writerows(sorted(rows, key=lambda r: -r["combined"]))

    econ = sorted([ECON[i] for i in top20], key=lambda e: -e["combined"])
    killed_econ = [e for e in ECON.values() if e["economics_verdict"].startswith("KILL")]
    with open(D("data", "economics_killed.csv"), "w", newline="") as fh:
        if killed_econ:
            w = csv.DictWriter(fh, fieldnames=list(killed_econ[0].keys())); w.writeheader(); w.writerows(killed_econ)
    with open(D("data", "top20_economics.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(econ[0].keys())); w.writeheader(); w.writerows(econ)

    # ---- machine comparison ----
    mc = []
    for t, p in PRESSES.items():
        cov20 = [e for e in econ if f(e["min_press_t"], 999) <= t]
        cov50 = [r for r in rows if r["stage"] in ("TOP20", "TOP50") and f(r["min_press_t"], 999) <= t]
        rev = sum(e["annual_revenue_dzd"] for e in cov20); con = sum(e["annual_contribution_dzd"] for e in cov20)
        land = landed_usd(t)
        mc.append(dict(press_t=t, fob_usd=p["fob"], landed_usd_no_aapi=land, tiebar_mm=p["tiebar"],
                       practical_pp_shot_g=f"{p['shot'][0]}-{p['shot'][1]}", connected_kva=p["kva"],
                       top20_covered=len(cov20), top50_covered=len(cov50),
                       revenue_pool_dzd=rev, contribution_pool_dzd=con,
                       top50_coverage_per_1000usd=round(len(cov50) / land * 1000, 2),
                       contribution_per_1000usd=round(con / land * 1000)))
    best = max(mc, key=lambda m: m["contribution_pool_dzd"])
    for m in mc:
        m["lost_contribution_vs_best_dzd"] = best["contribution_pool_dzd"] - m["contribution_pool_dzd"]
        m["extra_capital_vs_120_usd"] = m["landed_usd_no_aapi"] - landed_usd(120)
    with open(D("data", "machine_comparison.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(mc[0].keys())); w.writeheader(); w.writerows(mc)
    print("rows", len(rows), "injectable", len(inj))
    for m in mc: print(m)
    for e in econ: print(e["product_id"], e["product"][:40], e["price_dzd"], e["unit_cost_base"], e["margin_r300_u70"], e["margin_r400_u50"], e["economics_verdict"], e["min_press_t"])

if __name__ == "__main__":
    main()
