"""Phase 4 unit economics — base-case Year-1 model per shortlisted idea (AED).
Every input is an ASSUMPTION derived from evidence E1-E7 (sources cited in 04-phase4 report).
Purpose: order-of-magnitude feasibility and break-even, not a forecast."""

LICENCE = 25_000          # Dubai technical-services licence all-in, AED 15-30k (E7/Phase4 search)
OVERHEAD_M = 6_000        # vehicle lease, fuel, phone, insurance, software per month

ideas = {
 "I3 Compressed-air leak-to-savings": dict(
    capex={"Hikmicro AI56 acoustic camera (AED, anaum.com)":20_475, "Hikmicro AD21 ultrasonic":3_728,
           "Clamp-on flow + pressure/power loggers":18_000, "Fittings/FRL/drain stock":12_000, "Tools, PPE":6_000},
    staff_m={"Compressed-air technician":6_500},
    revenue_lines=[  # (name, customers in Y1, AED per customer per year, gross margin)
      ("Annual programme: 4 surveys + repair labour", 20, 12_000, 0.70),
      ("Repair parts (cost+35%)",                     20, 4_000,  0.26),
      ("One-off paid first surveys (not converted)",  15, 3_500,  0.80),
      ("Pressure/flow monitoring subscription",        8, 3_000,  0.65),
    ]),
 "I4 Legacy automation continuity": dict(
    capex={"Bench electronics/test rig":18_000, "Refurb HMI/drive exchange pool (seed)":60_000,
           "Engineering software licences (TIA/FTView, Y1)":30_000, "Migration-kit fabrication tools":10_000},
    staff_m={"Automation engineer (PLC/HMI)":17_000},
    revenue_lines=[
      ("Obsolescence audits",                 15, 4_500,  0.75),
      ("HMI/PLC migration kits & projects",   10, 28_000, 0.45),
      ("Repair-exchange / brokered repairs",  40, 3_500,  0.35),
      ("Emergency call-outs",                 25, 2_000,  0.70),
    ]),
 "I1 Critical-wear parts (scan-to-part)": dict(
    capex={"Handheld scanner (EinScan-class) + Einstar 2":45_000, "2x enclosed CF/engineering printers":18_000,
           "Food-compliant & engineering filament stock (igus A350/I151, PA-CF, ASA)":12_000,
           "CAD/RE software (Y1)":15_000, "Vacuum-casting chamber (phase 1b)":0},
    staff_m={"CAD/reverse-engineering designer":10_000},
    revenue_lines=[
      ("Paid triage line audits",               15, 4_000,  0.80),
      ("Reverse-engineering fees (parts)",      15, 9_000,  0.75),   # ~4-6 parts x AED 1.5-2k
      ("Part production (print/machine/cast)",  15, 14_000, 0.55),   # machining subcontracted
      ("Digital vault subscription",             8, 9_000,  0.85),
    ]),
 "J1 Cold-room reliability bundle": dict(
    capex={"Gasket profile roll stock + corner welder":18_000, "Refrigeration tools/recovery unit":15_000,
           "Sensor/gateway float (TDRA-approved, resold)":20_000},
    staff_m={"Refrigeration technician":6_500, "On-call allowance":1_500},
    revenue_lines=[  # customer = account; avg 8 cold rooms x AED 650/month
      ("Monthly bundle (8 rooms x AED 650)",     8, 62_400, 0.55),
      ("Hardware install fee",                   8, 6_000,  0.30),
      ("Repairs/parts outside bundle",           8, 10_000, 0.35),
      ("Filtration add-on (ice/coffee)",         4, 4_800,  0.40),
    ]),
 "I2 Reliability route + sensors": dict(
    capex={"Vibration analyser/collector (mid-range)":45_000, "IR camera":15_000,
           "Alignment tool":25_000, "Sensor float (approved)":20_000},
    staff_m={"Cat II vibration analyst":13_000},
    revenue_lines=[
      ("Monthly route contracts (AED 2.8k/mo)",   8, 33_600, 0.65),
      ("Wireless sensors (10 assets x AED 200/mo)",4, 24_000, 0.55),
      ("Alignment/balancing/RCA jobs",            15, 5_000,  0.70),
    ]),
}

print(f"{'Idea':40} {'Capex':>9} {'Y1 Rev':>9} {'Y1 GP':>9} {'Fixed':>9} {'Y1 EBITDA':>10} {'Cash need':>10}")
out=[]
for name,d in ideas.items():
    capex=sum(d["capex"].values())+LICENCE
    rev=sum(n*v for _,n,v,_ in d["revenue_lines"])
    gp=sum(n*v*m for _,n,v,m in d["revenue_lines"])
    fixed=12*(sum(d["staff_m"].values())+OVERHEAD_M)
    ebitda=gp-fixed
    # cash need: capex + 6 months fixed cost runway (47-day terms, 58% late -> assume ~3 months receivables)
    cash=capex+6*(fixed/12)+0.25*rev
    out.append((name,capex,rev,gp,fixed,ebitda,cash))
    print(f"{name:40} {capex:9,.0f} {rev:9,.0f} {gp:9,.0f} {fixed:9,.0f} {ebitda:10,.0f} {cash:10,.0f}")
