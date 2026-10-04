"""Phase 8: launch configuration, 24-month cash model (base/upside/downside) and scale levels.
Uses model/economics.py parameters and data/opportunities_master.csv. All volumes/prices are
ASSUMPTIONS from the master file unless labelled otherwise. Run: python3 model/phase8_plan.py
"""
import csv, os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
import economics as E

M = {r["product_id"]: r for r in csv.DictReader(open(E.D("data", "opportunities_master.csv")))}
f = E.f

# First commercial targets (selected in Phase 8 from the top 20; see final doc)
LAUNCH = [  # id, launch month (production), mold funded by: 'us' or 'customer', mold source
    ("IF-01", 6, "us", "China"),        # drip start connector
    ("IF-08", 6, "us", "Algeria/China"),# drip end plug
    ("JC-30", 6, "us", "Algeria"),      # formwork cone
    ("JC-24", 7, "us", "Algeria"),      # rebar spacer wheel (hours filler)
    ("CL-002", 8, "customer", "China"), # 28/410 flip-top, only if shampoo-maker case confirms
]
FILLER_MONTH = 9
PRESS_LANDED_USD = E.landed_usd(120) - 1_780  # AAPI duty exemption (VAT also exempt; VAT excluded anyway)
SETUP_DZD = 1_200_000        # company, rent deposit, electrical works, QC tools, first spares (ASSUMPTION)
FOUNDER_DZD = 120_000        # founder draw + overhead per month (ASSUMPTION)
LAB_1SHIFT = (36_000 + 65_000) * 1.26
LAB_2SHIFT = 173_000
OTHER_FIXED = {k: v for k, v in E.FIXED_MONTHLY.items() if k not in ("labour_2shift", "depreciation", "interest")}

CASES = {
    "BASE":     dict(vol=1.0, price=1.0, resin=300, credit=60, mold_factor=1.0, cav=1.0),
    "UPSIDE":   dict(vol=1.5, price=1.05, resin=220, credit=30, mold_factor=0.85, cav=1.0),
    "DOWNSIDE": dict(vol=0.5, price=0.8, resin=400, credit=90, mold_factor=1.15, cav=1.0),
    # Lean tooling: half the cavities (press time is idle anyway) -> mold cost x0.65 (ASSUMPTION)
    "BASE_LEAN_TOOLING":     dict(vol=1.0, price=1.0, resin=300, credit=60, mold_factor=0.65, cav=0.5),
    "DOWNSIDE_LEAN_TOOLING": dict(vol=0.5, price=0.8, resin=400, credit=90, mold_factor=0.75, cav=0.5),
}

def var_unit(r, resin, price, credit, cav=1.0):
    g = f(r["part_weight_g"]); blend = (1 - E.MB_SHARE) * resin + E.MB_SHARE * E.MB_PRICE
    material = g * (1 + E.LOSS) * blend / 1000 / (1 - E.REJECT)
    pph = max(1, f(r["cavities"]) * cav) * 3600 / f(r["cycle_s"]) * E.OEE
    power = E.POWER_KW_AVG * E.TARIFF_DZD_KWH / pph
    return material + power + price * (E.PACK + E.DELIVERY + E.SELLING), pph

def run(case):
    c = CASES[case]; months = 24
    press_dzd = PRESS_LANDED_USD * E.FX
    cash = 0; low = 0; rows = []; cum_profit = 0; be_month = None
    mold_paid = {}
    for m in range(1, months + 1):
        out = 0; inflow = 0; revenue = 0; varc = 0; hours = 0
        # capex timing: press 30% at order (m2), 70% + 120% provision effect at m3, lands m5
        if m == 2: out += press_dzd * 0.30
        if m == 3: out += press_dzd * 0.70
        if m == 1: out += SETUP_DZD * 0.5
        if m == 4: out += SETUP_DZD * 0.5
        for pid, start, funder, src in LAUNCH:
            r = M[pid]; mold = f(r["mold_cost_usd"]) * E.MOLD_LANDED_FACTOR * E.FX * c["mold_factor"]
            if funder == "us":
                if m == start - 3: out += mold * 0.3
                if m == start - 1: out += mold * 0.7
            if m >= start:
                ramp = min(1.0, 0.25 + 0.15 * (m - start))
                q = f(r["annual_volume_pcs"]) * c["vol"] / 12 * ramp
                price = f(r["price_dzd"]) * c["price"]
                vu, pph = var_unit(r, c["resin"], price, c["credit"], c["cav"])
                revenue += q * price; varc += q * vu; hours += q / pph
        # extra custom/filler jobs from month 9: 40 h/month at 6,000 DZD/h contribution-equivalent revenue (ASSUMPTION)
        if m >= FILLER_MONTH:
            fill_h = 40 * c["vol"]; revenue += fill_h * 9_000; varc += fill_h * 3_000; hours += fill_h
        shift2 = hours > 160
        labour = (LAB_2SHIFT if shift2 else LAB_1SHIFT) if m >= 5 else (LAB_1SHIFT * 0.5 if m == 4 else 0)
        fixed = labour + (sum(OTHER_FIXED.values()) if m >= 4 else 60_000) + FOUNDER_DZD
        profit = revenue - varc - fixed
        # cash: receivables per credit days (cash portion 50%), resin stock = 1.5 months of material
        cash_in = revenue * (0.5 + 0.5 * (1 if c["credit"] <= 30 else 0))
        rows.append(dict(month=m, revenue=round(revenue), variable=round(varc), fixed=round(fixed),
                         ebitda=round(profit), machine_hours=round(hours), two_shifts=shift2))
        cum_profit += profit
        # cash flow this month
        collected = revenue * 0.5 + (rows[-1 - int(c["credit"] / 30)]["revenue"] * 0.5 if len(rows) > int(c["credit"] / 30) else 0)
        resin_buy = (4_000 * c["resin"] if m == 4 else 0)
        provision = (0.2 * press_dzd if m == 2 else 0) - (0.2 * press_dzd if m == 4 else 0)
        cash += collected - varc - fixed - out - resin_buy - provision
        low = min(low, cash)
        rows[-1]["cash_balance"] = round(cash)
        if be_month is None and profit > 0 and m >= 6: be_month = m
    # cash: capex + cumulative operating losses + working capital (receivables + resin stock) at month 24
    capex = press_dzd + SETUP_DZD + sum(f(M[p]["mold_cost_usd"]) * E.MOLD_LANDED_FACTOR * E.FX * c["mold_factor"]
                                        for p, s, fu, _ in LAUNCH if fu == "us")
    run_cum = 0; peak_loss = 0
    for r in rows:
        run_cum += r["ebitda"]; peak_loss = min(peak_loss, run_cum)
    last = rows[-1]
    receivables = last["revenue"] * c["credit"] / 30 * 0.5
    resin_stock = 4_000 * c["resin"]
    domic_provision = 0.2 * press_dzd     # extra 20% of press value parked temporarily (120% rule)
    peak_need = -low
    year1 = rows[:12]; year2 = rows[12:]
    return dict(case=case, capex_dzd=round(capex), capex_usd=round(capex / E.FX),
                peak_operating_loss_dzd=round(-peak_loss), working_capital_dzd=round(receivables + resin_stock),
                peak_cash_need_dzd=round(peak_need), peak_cash_need_usd=round(peak_need / E.FX),
                y1_revenue=sum(r["revenue"] for r in year1), y1_ebitda=sum(r["ebitda"] for r in year1),
                y2_revenue=sum(r["revenue"] for r in year2), y2_ebitda=sum(r["ebitda"] for r in year2),
                first_profitable_month=be_month, m24_machine_hours=last["machine_hours"], monthly=rows)

def scale_levels():
    # revenue per productive machine-hour from the top-20 set (ASSUMPTION-derived)
    e = list(csv.DictReader(open(E.D("data", "top20_economics.csv"))))
    rev_h = sum(f(x["annual_revenue_dzd"]) for x in e) / sum(f(x["machine_hours_per_year"]) for x in e)
    hours_per_mold = sum(f(x["machine_hours_per_year"]) for x in e) / len(e)
    out = []
    for n, util, staff, area, kva, molds_note in [
        (1, 0.35, 3, 250, 70, "8-12 molds"), (3, 0.55, 10, 700, 200, "25-35 molds"),
        (5, 0.60, 18, 1200, 330, "40-60 molds"), (10, 0.65, 35, 2500, 650, "80-120 molds"),
        (20, 0.70, 70, 5000, 1300, "150-250 molds")]:
        hours = n * 4800 * util
        molds = round(hours / hours_per_mold)
        capex_usd = n * 32_000 + molds * 7_700 * (0.6 if n >= 5 else 1.0)  # toolroom/local molds cut cost at scale (ASSUMPTION)
        out.append(dict(machines=n, utilisation=util, productive_hours=round(hours), molds_needed=molds, molds_note=molds_note,
                        revenue_capacity_dzd=round(hours * rev_h), revenue_capacity_usd=round(hours * rev_h / E.FX),
                        capex_usd=round(capex_usd), staff=staff, area_m2=area, power_kva=kva))
    return out, rev_h, hours_per_mold

if __name__ == "__main__":
    res = {k: run(k) for k in CASES}
    lv, rev_h, hpm = scale_levels()
    for k, v in res.items():
        print(k, {a: b for a, b in v.items() if a != "monthly"})
    print("rev per machine hour", round(rev_h), "hours per mold/yr", round(hpm))
    for x in lv: print(x)
    json.dump(dict(cases=res, scale=lv, rev_per_hour=rev_h, hours_per_mold=hpm),
              open(E.D("data", "phase8_model.json"), "w"), indent=1, default=str)
