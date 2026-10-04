# Phase 4 — Technical Feasibility of the Top 5

Model: `scoring/unit_economics.py` (output in `scoring/unit_economics_output.txt`). Every figure is in AED and every input is an assumption grounded in evidence E1–E7, or in the Phase 4 searches cited below.

Rules applied to all five ideas:
- The founder is **unpaid** in the model.
- Licence cost is AED 25k all-in (Dubai technical-services licence, AED 15–30k per [avyanco](https://avyanco.com/news/technical-services-license-dubai/) and [bestaxca](https://bestaxca.com/technical-services-license-dubai/)).
- Overhead is AED 6k/month.
- Cash need = capex + 6 months of fixed cost + 25% of Year-1 revenue tied up in receivables (UAE B2B average is 47 days, and 58% of invoices are paid late).

## Phase 4 search findings that changed the plan

1. **Food contact is solvable.** igus iglidur **I151** (FDA + EU 10/2011, blue so it can be detected if it breaks off) and **A350** (FDA + EU 10/2011, rated to 180 °C, UL94-V0) are printable food-compliant wear filaments ([igus](https://www.igus.co.uk/3d-printing/3d-printing-food-grade), [igus press](https://press.igus.eu/iglidur-i151-for-fda-compliant-detectable-wear-resistant-parts-in-food-technology/)). This removes the main Phase 3 risk for I1. Standard MJF PA12 is *not* food-certified.
2. **Wireless sensors need TDRA type approval.** Approval costs AED 5–20k per product. The importer needs a telecom-equipment trade activity ([Middle East Briefing](https://www.middleeastbriefing.com/news/?p=5830), [TÜV](https://www.tuv.com/market-access-services/en/certification-filter/united-arab-emirates-telecommunication-apparatus-(tdra)-approval.html)). **Decision: never import our own radio hardware at the start.** Resell already-approved sensors through registered UAE distributors (RMT/Sensoteq, Kelsius, Testo, ABB channel), and put our value in installation, analytics and response.
3. **The acoustic camera is sold locally.** Hikmicro AI56 costs **AED 20,475** and the AD21 ultrasonic detector **AED 3,728** at anaum.com, UAE ([anaum](https://anaum.com/products/hikmicro-ai56)). There is no import lead time.

## Feasibility summary

| | I3 Compressed air | I1 Critical-wear parts | J1 Cold-room bundle | I4 Legacy automation | I2 Reliability route |
|---|---|---|---|---|---|
| Technical complexity | Low | Medium | Low–medium | **High** | Medium–high |
| Key hire | Compressed-air technician (~AED 6.5k/mo) | CAD/reverse-engineering designer (~AED 10k/mo) | Refrigeration technician (~AED 6.5k + on-call) | Automation engineer (~AED 17k/mo) | Cat II vibration analyst (~AED 13k/mo) |
| Capex incl. licence | ~85k | ~115k | ~78k | ~143k | ~130k |
| Base Y1 revenue | ~397k | ~477k | ~646k | ~538k | ~440k |
| Base Y1 EBITDA (before founder pay) | +96k | +134k | +157k | −15k | +52k |
| **Break-even as % of base revenue** | **61%** | **59%** | **52%** | **106%** | **81%** |
| Downside (50% revenue) EBITDA | −27k | −29k | −6k | −146k | −88k |
| Cash needed for Y1 | ~260k | ~330k | ~324k | ~415k | ~354k |
| Recurring share | Medium–high | Low → medium (vault) | **High** | Low | High |
| Supplier ecosystem in UAE | Good (Hikmicro local; fittings local) | Good (printers, filaments, Sharjah machining) | Good (sensors local; gasket profiles imported) | Mixed (grey-market risk) | Good (OEM channels) |

**Reading the table:**
- I3, I1 and J1 can stand alone.
- **I4 cannot stand alone at first.** A full-time automation engineer must be carried before demand is proven. Start I4 *asset-light*: broker repairs to an existing UAE lab, and sell audits and migration kits delivered by a freelance or contract engineer.
- **I2 should not lead.** It is viable only as an upsell on I3 visits, using the same ultrasound kit and the same plant.

---

## Shortlisted idea profiles (the 17 fields from the brief)

### 1) I3 — Compressed-air "leak-to-savings" programme

- **Problem.** Compressed air leaks through quick-connects, hoses, FRLs and drains. Plants typically lose 20–30% of compressor output this way. Leaks get tagged but never fixed, and they come back.
- **Buyer.** Plant manager or maintenance manager at an SME factory with at least 30 kW of compressors: F&B, blow-moulding and plastics, packaging, metal fabrication, print.
- **Current solution.** Free or cheap OEM audits (ELGi UAE, Atlas Copco AIRScan) that lead into selling a compressor. Otherwise, nothing.
- **Evidence.**
  - eng-tips practitioners: "needs to be a regular scheduled program or you wind up in the same spot".
  - Compressed Air Challenge: 20–30% leakage, payback under 1 year.
  - UK SME analogue: Direct Air sells survey days and discounts the first.
  - **No independent UAE provider found.** (E1, E4, E7)
- **Current cost.** About 7.5 kW of leaks × 6,000 h ≈ **AED 13–20k a year** at DEWA's 23/38 fils + surcharge. Larger plants lose multiples of this.
- **Frequency.** Continuous. Leaks return within months.
- **UAE reason.**
  - Post-Hormuz cost pressure.
  - The DEWA marginal tariff.
  - Abu Dhabi ETIP gives 20% weight to an energy-management system.
  - DSM 2050 "Top 50" industrial programme.
  - Humid air means condensate and dryer problems are common.
- **Global analogues.** Direct Air Pipework, Hayley Group, IPE Search (UK); Atlas Copco AIRScan (OEM). Leak-programme monitoring: ifm moneo, Invisible Systems.
- **Technology.** Ultrasonic and acoustic imaging, flow and pressure logging, a kWh savings calculation, basic pneumatic fitting work.
- **Hardware.** Hikmicro AI56 (AED 20.5k, local), AD21 (AED 3.7k), clamp-on flow and power loggers (~AED 18k), fittings stock.
- **Our value-add.** Independence (we don't sell compressors). **We repair on the spot.** Results are verified in AED. Quarterly re-surveys. Parts held in stock locally.
- **AI opportunity (real but modest).**
  - Auto-classify and size leaks from acoustic images and dB readings.
  - Generate tagged leak reports with AED-per-year estimates automatically.
  - Track compressor running hours and pressure for anomaly alerts.
  - This makes reports faster and more convincing. It does not replace the technician.
- **Revenue model.**
  - Paid first survey: AED 3.5k, credited toward a programme.
  - Annual programme: ~AED 12k (4 surveys + repair labour).
  - Parts at cost + 35%.
  - Monitoring: AED 250/month per compressor room.
  - Gain-share option for large plants.
- **Indicative capital to test.** AED ~25k: camera, detector and fittings. Licence and van can be via a partner LLC or a freelance permit at the test stage. **LEGAL/REGULATORY REVIEW LATER.**
- **Technical people.** One mechanical or pneumatic technician. Training is 2–4 weeks with the camera vendor plus field mentoring.
- **Expansion.**
  - Compressor-room optimisation (sequencing, pressure-band reduction, heat recovery).
  - Nitrogen, steam and vacuum leaks.
  - Ultrasound bearing checks, leading into I2.
  - Energy audits for the Abu Dhabi ETIP score.
- **Defensibility.** Weak on its own. A trader can buy the camera. The moat is (a) verified-savings data across many plants, (b) repair capability, and (c) the account relationship used to sell I1 and I4. **Treat I3 as a wedge, not the castle.**
- **First validation.** Rent or borrow an acoustic camera (or buy the AD21 for AED 3.7k). Run **5 free leak walks** at plants in Sharjah, Ajman or DIC. Count the leaks, compute AED per year, and ask each plant to sign a paid programme. Target: at least 2 of 5 sign.

### 2) I1 — Critical-wear parts: scan → CAD → print, machine or cast, plus a curated vault

- **Problem.** Non-critical wear and change parts break on packaging, bottling and food lines: guides, star-wheel segments, guards, brackets, sensor mounts, chute liners, gripper fingers, knobs, covers. The OEM part takes 6–19 weeks, or no longer exists, and costs 5–50× what it should.
- **Buyer.** Engineering or maintenance manager at an F&B, bottling, packaging or plastics plant. Also FM contractors and marine operators.
- **Current solution.**
  - Wait for the OEM.
  - Improvise a fix in the workshop.
  - Ask a Sharjah machine shop to copy the part by eye.
  - For oil & gas only: Immensa or FTI.
- **Evidence.**
  - Practical Machinist: 16–19 week spindles, 9-month toolchanger parts.
  - Fluke survey: 83% of UK plants delayed by unavailable parts.
  - Pet-food plant: a £45 printed part replaced one causing £5k/day downtime.
  - Suntory: −83% lead time, −70% cost.
  - ADNOC Gas: −50% lead time. RTA: 90% faster sourcing.
  - Hormuz disruption made imports slower and dearer. (E1, E3, E5)
- **Current cost.** The part itself is AED 200–5,000. **Downtime is AED 5–50k/day** for a food or packaging line (inferred from the £5k/day case). Validate this.
- **Frequency.** Plant-specific. Validate with the triage audit: Spare Parts 3D found only 7% of a catalogue suits printing.
- **UAE reason.**
  - Import dependence, plus the Hormuz disruption.
  - "Make it in the Emirates" localisation.
  - Ladder toward ICV-relevant local manufacturing.
  - More than 2,000 F&B and 569 plastics firms.
  - Hot plant rooms need heat-rated materials.
- **Global analogues.** Cadmore (US reverse engineering, $300–1,500 per part); Spare Parts 3D / DigiPART (triage); Replique; Deutsche Bahn; Wilhelmsen/Ivaldi (marine).
- **Technology.** Structured-light scanning, CAD reconstruction, materials selection (iglidur A350/I151, PA-CF, ASA, PA12), FDM printing, machining via Sharjah partners, and later vacuum casting.
- **Hardware.** EinScan-class handheld scanner plus an Einstar 2, two enclosed engineering printers, CAD/RE software. About **AED 90k**.
- **Our value-add.**
  - Diagnosis: what is critical and slow to import.
  - Material engineering for heat and food contact.
  - 48–72 h turnaround.
  - The digital record and fast reorder.
  - Choosing the right process (print vs machine vs cast).
  - Avoid safety-critical and pressure-retaining parts. Leave those to Immensa and FTI or partner with them.
- **AI opportunity (moderate).**
  - Triage the plant's spare-parts and BOM lists to find printable, economic candidates (the DigiPART approach).
  - Identify parts from photos (WhatsApp in → candidate match).
  - Generate quotes automatically from scan volume, material and process.
  - **This is where the founder's LLM and n8n skills create a real speed advantage.**
- **Revenue model.**
  - Paid triage audit: AED 3–5k.
  - Reverse-engineering fee: AED 1–3.5k per part.
  - Production priced on downtime value, not grams.
  - Vault subscription: AED 500–1,500/month per plant (stored designs, 48 h reprint SLA, priority).
- **Indicative capital to test.** About AED 15k (Einstar 2 + one printer + igus filaments). Machining outsourced.
- **Technical people.** One mechanical design engineer with reverse-engineering experience (Geomagic or Fusion). Junior to mid level, AED 8–12k.
- **Expansion.**
  - Vacuum casting for 20–500 parts.
  - Aluminium soft tooling and low-volume moulding.
  - 3D scanning of plant rooms for retrofit design.
  - Dimensional QC inspection.
  - Becoming a tier-2 supplier to Local+ manufacturers.
- **Defensibility.** Medium:
  - The vault creates lock-in.
  - Accumulated material and heat failure data.
  - Plant-specific relationships.
  - The capability ladder into casting and moulding.
- **First validation.** **10 plant walk-throughs.** Ask each plant: "which 10 parts would you never want to wait for?" Count parts with OEM lead time over 3 weeks or price over AED 2k. Deliver 3 parts free or at cost, then measure whether the plant reorders and pays for the next ones.

### 3) J1 — Cold-room reliability bundle (+ filtration add-on)

- **Problem.** At 45 °C ambient a failed cold room spoils stock within hours. Door gaskets, strip curtains and door closers degrade every 3–12 months and cause icing and excursions. Small operators keep paper logs and spot failures late.
- **Buyer.** Operations or engineering manager at hotels, central and cloud kitchens, food distributors, and restaurant chains with 5–20 outlets.
- **Current solution.**
  - Classified-ad cold-room technicians, called after the failure.
  - FM contracts (AMCs).
  - DIY loggers (Testo) or SaaS sensors (Kelsius) with nobody contracted to respond.
- **Evidence.**
  - Dubai has 29,303 food establishments, opening at about 10.5 a day.
  - Dubai Municipality requires ≤5 °C chilled and ≤−18 °C frozen, with daily logs.
  - ADAFSA closed outlets in 2024 partly for missing temperature records.
  - Analogues: The SEALS (6 units) and Gasket Guy (19 locations). (E1, E4, E6)
- **Current cost.** A single excursion loses AED 5–50k+ of stock (vendor and expert claims; validate). Plus inspection penalties.
- **Frequency.** Gaskets wear every 3–12 months. Summer peaks drive failures.
- **UAE reason.**
  - Heat.
  - Food-security priority and a cold-storage shortfall of at least 125k m².
  - Hormuz made replacement imported stock slower and dearer.
- **Global analogues.** The SEALS, Gasket Guy; Checkit (UK); Monnit / Danfoss Alsense.
- **Technology.** Refrigeration servicing, gasket fabrication from roll stock, approved wireless temperature and door sensors, alerting, compliance-ready reports.
- **Hardware.** Gasket profile stock and corner welder, refrigeration tools, resold TDRA-approved sensors and gateways. About **AED 53k** before licence.
- **Our value-add.**
  - **One accountable party** for sensors, physical fixes, alarm response and inspection-ready records.
  - Gaskets made locally the same day.
- **AI opportunity (moderate, credible).**
  - Detect defrost and compressor anomalies and door-left-open patterns from temperature curves, before an excursion.
  - Auto-generate HACCP / Food Code logs and corrective-action records.
  - WhatsApp alert triage.
- **Revenue model.**
  - About **AED 450–900 per cold room per month**, covering sensors, monitoring, 4 visits and alarm response.
  - Installation fee.
  - Parts outside the bundle.
  - Filtration add-on for ice and coffee machines.
- **Indicative capital to test.** About AED 20k: gasket stock, sensors for 2 pilot accounts, and a partner refrigeration technician on call.
- **Technical people.** One refrigeration technician, plus an on-call rota or partner.
- **Expansion.**
  - Reach-in fridges and blast chillers.
  - Pharmacy and clinic vaccine fridges (DHA).
  - Food distributors' reefer trucks.
  - Kitchen equipment PM.
  - Franchise-style replication across emirates and the GCC.
- **Defensibility.** Medium. Response network density, plus compliance data history, plus account bundling. Monitoring alone is a commodity.
- **First validation.** Sell **2 paid pilots** (one hotel, one central kitchen) of 3 months at about AED 600 per room per month. Test whether a chain will pay for *guaranteed response* on top of its existing AMC.
- **Founder-fit caveat.** This is the most "service-ops" of the five. It is less aligned with the industrial-engineering ladder than I1/I3/I4.

### 4) I4 — Legacy automation continuity

- **Problem.** Machines from 2000–2012 run obsolete PLCs, HMIs and drives (S7-300/400, SLC500, PanelView, older Red Lion and Siemens panels). When one fails, the OEM has no stock, repair takes weeks, and full migration is quoted as a large project.
- **Buyer.** Plant maintenance or engineering manager. Also OEM agents and machine traders.
- **Current solution.** Panic buying on eBay or from Deira traders. Repair shops (WEDIAN, Automat, CNC Experts). Large system-integrator migrations.
- **Evidence.**
  - plctalk: PLCs replaced "due to not being able to get spare parts".
  - HMI repair quotes: $250–5,500, or 50–60% of new.
  - Analogues: Industrial Monitor Direct drop-in kits; HMI repair at $450–2,200 with 12-month warranty.
  - Roll-up exits (Radwell, EU Automation). (E1, E5, E7)
- **Current cost.** Downtime of AED 10–100k/day, plus panic purchase premiums.
- **Frequency.** Episodic but certain. The installed base keeps ageing.
- **UAE reason.**
  - Ageing SME installed base in Sharjah, Ajman and DIC.
  - Import delays make local repair-exchange and stock valuable.
  - Repair instead of replacement supports the circular economy.
- **Global analogues.** Essential Automation (UK), NJT and Flexa (HMI repair), Industrial Monitor Direct (migration kits + SEO), Radwell (consolidator).
- **Technology.** PLC/HMI programming and migration, electronics repair triage, panel-cutout adaptation, documentation.
- **Hardware.** Bench tools, exchange pool, licensed engineering software. Capex is moderate but the **people cost is the risk**.
- **Our value-add.**
  - Obsolescence audit: a risk register per line.
  - Drop-in migration kits that keep the same cutout and minimise reprogramming.
  - A local exchange pool.
  - **Bilingual part-number SEO pages and WhatsApp quoting** (founder strength).
- **AI opportunity (strong and specific).**
  - Read nameplate and label photos into part numbers.
  - Look up obsolescence status and successor parts.
  - Extract I/O and program documentation from old projects.
  - Auto-draft migration bills of materials and quotes.
  - Turn the founder's document-AI experience into the audit product.
- **Revenue model.**
  - Audit: AED 3–7.5k.
  - Migration kits and projects: AED 15–50k.
  - Brokered repairs at 25–40% margin.
  - Emergency call-out fee.
  - Later: an annual "continuity plan" retainer with a guaranteed exchange unit.
- **Indicative capital to test.** About AED 10k. Website and SEO, a contract engineer by the day, and repairs brokered to an existing lab.
- **Technical people.** **This is the binding constraint.** One senior automation engineer (Siemens and Rockwell), AED 15–20k/month, or a profit-share partner.
- **Expansion.**
  - Control-panel refurbishment.
  - Drive and motor efficiency (VFD packages).
  - Machine digitisation (old machine → OEE data).
  - Regional GCC exchange hub.
- **Defensibility.** Medium–high once established: know-how, exchange-pool inventory, SEO content library, installed-base data.
- **First validation.** Publish 30 part-number and "replacement for X" pages, then measure inbound enquiries for 6 weeks. Run **5 paid obsolescence audits** using a contract engineer.

### 5) I2 — Reliability route + wireless sensors (bolt-on to I3)

- **Problem.** SME plants run rotating equipment until it fails. Bearing, alignment and imbalance failures cause unplanned downtime. Summer heat speeds up motor and drive failures.
- **Buyer.** The same as I3.
- **Current solution.** Nothing (run to failure). Or Vibrant Electromechanical, Pruftechnik and OEM service. Sensors from RMT/Sensoteq or remote platforms (Tractian, Waites).
- **Evidence.**
  - Global practitioners confirm the pain.
  - The UAE has real incumbents and **thin SME demand signals** (9 vibration-analyst job listings in the UAE).
  - ADNOC lists machine condition monitoring as a localisation category. (E3, E4, E7)
- **Revenue model.**
  - Monthly route: about AED 2–4k per site (20–40 assets).
  - Sensors: about AED 150–250 per asset per month.
  - Alignment, balancing and root-cause analysis jobs.
- **Hardware.** Vibration collector (AED ~45k mid-range), IR camera (AED ~15k), alignment tool (AED ~25k). Ultrasound shared with I3.
- **Technical people.** ISO 18436 Cat II analyst (AED ~10–15k). Training is available locally (Vibrant runs Mobius courses).
- **AI opportunity (highest of the five on paper).** Spectral anomaly detection, automated fault classification, maintenance recommendations. But funded global players (Tractian, Augury) already do this well. **We should resell their analytics or use an OEM's, not build our own.**
- **Defensibility.** Low against incumbents. Medium as part of a multi-service account.
- **First validation.** Offer a **free thermography and ultrasound walk** to each I3 customer. Convert 1 in 3 to a monthly route.

---

## The combined company: "Line Continuity"

| Element | Detail |
|---|---|
| Customer | Maintenance or engineering manager of a UAE SME plant (F&B, bottling, packaging, plastics, light manufacturing) |
| Promise | "When your line stops, we get it running, and we stop it from stopping again." |
| Door-opener | **I3 leak-to-savings.** Cheap kit, fast paid ROI, gets the team onto the plant floor |
| Margin and moat | **I1 critical-wear parts** + **I4 legacy automation continuity.** These deal with the two things that *actually* stop lines: parts and electronics |
| Recurring | I3 programme + I1 vault + I2 routes/sensors + I4 continuity retainer |
| Shared assets | One CRM and asset register, one AI document and quoting engine, one van, one plant relationship |
| Capability ladder | Survey kit → scanner/printer → casting/soft tooling → low-volume moulding (ICV, Local+ tier-2) → regional GCC service hub |
| Combined Y1 test capital | **About AED 60–100k** to validate (I3 kit + I1 starter cell + I4 web/SEO + licence via partner). **About AED 400–550k** to run I3+I1 properly with 2 hires for 12 months, including working capital |

J1 (cold-room bundle) has the best standalone economics, but **it serves a different buyer** (F&B operators, not plants). It is kept as the **alternative path**: the best choice if the founder prefers a service business with high recurring revenue over an industrial-engineering company.

## Local manufacturing opportunity (honest)

- **Real and near-term:** printed and machined replacement parts (I1), gaskets cut from roll stock (J1), and fabricated HMI migration bezels and adapter plates (I4).
- **Medium-term (18–36 months):** vacuum casting and aluminium soft tooling for 20–5,000-part runs. This is the realistic route into "injection moulding" without starting a factory.
- **Not justified now:** a full injection-moulding plant, metal additive manufacturing, or our own sensor hardware (because of TDRA type approval and existing funded competitors).
