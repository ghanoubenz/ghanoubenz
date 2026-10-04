"""Phase 3 scoring. All 29 criteria scored 0-10 where 10 is always BETTER for us
(e.g. startup_capital 10 = little capital needed; competition 10 = little competition).
Scores are analyst judgement grounded in evidence/E1-E7; see 03-phase3 report."""
import csv, sys

C = ["demand_evidence","pain_intensity","urgency","uae_future_relevance","national_value",
     "import_dependence","technical_moat","technical_learnability","founder_fit","hire_expertise",
     "startup_capital","revenue_per_customer","gross_margin","recurring_revenue","downtime_value",
     "customer_concentration","competition","competitor_sophistication","acquisition_ease",
     "sales_cycle","roi_demonstrability","asset_light","local_manufacturing","ai_value_add",
     "hardware_software","service_revenue","export_later","scalability","defensibility"]

S = {
 "I3 Compressed-air leak-to-savings": [6,6,5,7,6,4,4,9,8,8,9,5,7,7,3,9,7,6,6,7,10,9,2,6,6,9,7,6,4],
 "I4 Legacy automation continuity":   [7,8,8,6,7,7,7,5,7,6,7,6,7,4,9,9,5,7,6,8,7,7,4,7,6,9,8,7,6],
 "I1 Critical-wear parts (scan-to-part)":[5,7,7,9,9,9,6,7,7,7,8,5,7,4,8,8,6,6,5,6,8,6,9,6,5,6,7,7,6],
 "I2 Reliability route + sensors":    [4,6,4,8,7,4,6,5,6,5,7,7,7,9,8,8,4,5,4,4,6,7,3,9,9,9,7,7,6],
 "I5 Enclosure climate hardening":    [5,7,6,8,7,6,7,6,5,6,6,6,6,5,6,4,6,4,3,3,5,5,8,5,7,6,9,7,6],
 "J1 Cold-room reliability bundle":   [7,7,7,8,6,4,4,8,8,8,8,5,6,9,8,9,6,6,6,6,7,8,3,6,8,9,7,7,5],
 "J2 Leak pinpoint + shutoff":        [7,7,8,6,6,3,4,7,8,7,8,3,7,2,4,9,4,6,7,9,7,8,2,4,4,7,5,5,3],
 "J5 Hotel FCU EC conversion (sub)":  [5,5,4,7,7,4,5,6,6,6,6,9,6,3,3,6,5,4,4,3,8,6,4,5,5,6,7,6,5],
 "J3 Pulsed laser cleaning":          [2,4,3,5,5,3,3,7,7,6,7,5,7,4,4,7,8,8,5,6,4,6,2,2,2,7,4,4,3],
 "J4 Filtration-as-a-service":        [4,4,3,5,4,3,2,9,7,9,9,3,5,8,5,9,5,5,5,7,5,8,1,4,2,6,5,5,2],
}
G = {
 "Market Attractiveness": ["demand_evidence","pain_intensity","urgency","revenue_per_customer","gross_margin",
     "recurring_revenue","downtime_value","customer_concentration","competition","competitor_sophistication","scalability"],
 "Technical Opportunity": ["technical_moat","import_dependence","local_manufacturing","ai_value_add",
     "hardware_software","service_revenue","defensibility","roi_demonstrability"],
 "Founder Entry": ["technical_learnability","founder_fit","hire_expertise","startup_capital",
     "acquisition_ease","sales_cycle","asset_light"],
 "UAE Strategic Fit": ["uae_future_relevance","national_value","import_dependence","export_later","local_manufacturing"],
}
W = {"Market Attractiveness":.3,"Technical Opportunity":.2,"Founder Entry":.3,"UAE Strategic Fit":.2}
rows=[]
for name,v in S.items():
    assert len(v)==len(C), name
    d=dict(zip(C,v)); r={"idea":name}
    for g,cs in G.items(): r[g]=round(sum(d[c] for c in cs)/len(cs),1)
    r["Overall Test Priority"]=round(sum(r[g]*w for g,w in W.items()),2)
    rows.append((r,d))
rows.sort(key=lambda x:-x[0]["Overall Test Priority"])
hdr=["idea"]+list(G)+["Overall Test Priority"]
print("| "+" | ".join(hdr)+" |"); print("|"+"---|"*len(hdr))
for r,_ in rows: print("| "+" | ".join(str(r[h]) for h in hdr)+" |")
with open(sys.argv[1] if len(sys.argv)>1 else "scores.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["idea"]+C+list(G)+["Overall Test Priority"])
    for r,d in rows: w.writerow([r["idea"]]+[d[c] for c in C]+[r[g] for g in G]+[r["Overall Test Priority"]])
