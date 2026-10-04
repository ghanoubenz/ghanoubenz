# Phase 3 — UAE Competition and Demand: 10 → 5

Evidence: `evidence/E6` (commercial and building ideas), `evidence/E7` (industrial ideas). Scoring is in `scoring/score.py` and `scoring/scores.csv`, and can be rerun.

## Customer-base numbers that matter

| Base | Size | Source |
|---|---|---|
| UAE industrial enterprises | ~33,000 (95% SMEs) | MoIAT via E3 |
| Food & beverage manufacturers | 2,000+ (~25% of manufacturing GDP) | Dubai Media Office (E7) |
| Rubber and plastics converters | 569 | MoIAT (E7) |
| Dubai food establishments | 29,303; ~10.5 new per day | Dubai Municipality via Gulf News (E6) |
| Dubai hotels | 770 hotels / 158,700 rooms, 81% occupancy, AED 746 average daily rate | Cavendish Maxwell (E6) |
| Dubai EV charge points | 2,223 (Q1 2026), target 10,000 by Dec 2026 | WAM / zigwheels (E7) |
| B2B payment reality | 47-day average terms; 58% of credit sales paid late | Atradius 2025 (E7) |

## What the UAE competition check changed

- **I3 Compressed air: confirmed.** OEM audits exist (ELGi UAE, Atlas Copco AIRScan), and they give the survey away to sell compressors. No independent provider runs a survey → repair → re-survey → monitor cycle. Rough arithmetic for a mid-size plant: 7.5 kW of leaks ≈ AED 13–20k a year wasted. That makes a programme priced at AED 8–15k a year easy to justify. Plants below about 30 kW of compressors are not worth targeting.
- **I2 Reliability route: weaker than it looked.** There is a real incumbent: Vibrant Electromechanical, which does vibration, balancing, alignment, thermography and root-cause analysis, and also trains Cat I–IV analysts. RMT Reliability has distributed Sensoteq wireless sensors since August 2024, which occupies our sensor step. Only 9 vibration-analysis jobs appear on NaukriGulf for the whole UAE, so SME demand is unproven. **It is now a bolt-on to I3, not a lead business.**
- **I1 Scan-to-part: survives, but narrower.**
  - Generic printing is a commodity: Hubs quotes instantly for Dubai, and Orbit3D, LayerX and Paradigm all exist.
  - Nobody has positioned for F&B and packaging line parts.
  - New risk: **food contact.** PA-CF and ASA are not generally food-contact certified, so the service starts with non-contact parts (guards, brackets, sensor mounts, chute liners, covers) and certified PA12 where contact is needed.
  - The real competitor is a machined UHMW or POM part from a Sharjah machine shop, so we should *offer machining as well as printing*.
- **I4 Legacy automation: confirmed, as a differentiation play.**
  - Break-fix repair is crowded (WEDIAN, Automat, CNC Experts, Indian repairers).
  - What nobody offers: obsolescence audits, drop-in HMI migration kits, a stocked repair-exchange pool, and searchable part-number pages.
  - Risks: counterfeit parts and liability, HMI software licensing, and WhatsApp price-shopping.
- **J1 Cold-room bundle: confirmed, with a sharper target.**
  - The sensor layer exists (Kelsius, Testo), and cold-room repair is done by classified-ad technicians. Nobody bundles the two.
  - The regulatory hook is **records, not sensors**. Dubai Municipality accepts paper logs, but Abu Dhabi has closed establishments partly for missing fridge and freezer records.
  - Sell to hotels, central kitchens, food distributors and chains of 5–20 outlets. Avoid single restaurants: they churn and they shop on price.
- **J2 Leak pinpointing: downgraded.**
  - DEWA's free High Water Usage Alert already covers detection.
  - UAE home insurance excludes gradual leaks.
  - Tenants pay the bill while landlords own the pipes.
  - Plumbers set a low price floor of about AED 250–1,000.
  - It survives only as a premium pinpointing service plus valve installs: a decent small business, but **no capability ladder.**
- **J5 Hotel FCU EC conversion: downgraded.**
  - Retrofitting EC fans into air-handling units is already done locally (Qey + ebm-papst + Taka at Swiss Tower, about 60% savings).
  - Etihad ESCO and Quantum Eurostar hold the hotel ESCO relationships.
  - Viable only as an FCU-specialist subcontractor, with long sales cycles and 90–120-day payment terms.
- **J3 Laser cleaning: killed.** No UAE demand signal, dry-ice cleaning is entrenched, Chinese continuous-wave lasers undercut on price, and the NZ comparable exited below its sunk cost.
- **J4 Filtration-as-a-service: merged into J1.** It is a commodity (Ekuep sells online), OEM dealers control warranty paperwork, and Rational's CareControl weakens the combi-oven case.

**Evidence still missing for every idea:** UAE prices in AED and customer reviews. Neither appears in search results, which suggests prices are hidden and buying happens through relationships. Phase 6 phone calls and visits must fill this gap.

## Scoring: 29 criteria → 4 composites → test priority

Every criterion is scored 0–10, with 10 always meaning better for us (for example, startup capital 10 = little capital needed). The composites:

- **Market Attractiveness** = mean of demand, pain, urgency, revenue per customer, margin, recurring revenue, downtime value, customer concentration, competition, competitor sophistication, scalability.
- **Technical Opportunity** = mean of moat, import dependence, local manufacturing, AI value, hardware+software, service revenue, defensibility, ROI demonstrability.
- **Founder Entry** = mean of learnability, founder fit, ability to hire expertise, capital, acquisition ease, sales cycle, asset-light.
- **UAE Strategic Fit** = mean of future relevance, national value, import dependence, export potential, local manufacturing.
- **Overall Test Priority** = 0.3 Market + 0.2 Technical + 0.3 Founder + 0.2 Strategic.

| Idea | Market | Technical | Founder entry | UAE fit | **Test priority** |
|---|---|---|---|---|---|
| I1 Critical-wear parts (scan-to-part) | 6.4 | 6.9 | 6.6 | 8.6 | **7.00** |
| I4 Legacy automation continuity | 7.0 | 6.6 | 6.6 | 6.4 | **6.68** |
| J1 Cold-room reliability bundle | 7.0 | 5.8 | 7.4 | 5.6 | **6.60** |
| I3 Compressed-air leak-to-savings | 6.1 | 5.6 | 8.0 | 5.2 | **6.39** |
| I2 Reliability route + sensors | 6.3 | 6.5 | 5.4 | 5.8 | **5.97** |
| I5 Enclosure climate hardening | 5.6 | 6.2 | 4.9 | 7.6 | 5.91 |
| J2 Leak pinpoint + shutoff | 5.6 | 4.2 | 7.7 | 4.4 | 5.71 |
| J5 Hotel FCU EC conversion (sub) | 5.1 | 5.2 | 5.3 | 5.8 | 5.32 |
| J4 Filtration-as-a-service | 5.1 | 3.1 | 7.7 | 3.6 | 5.18 |
| J3 Pulsed laser cleaning | 5.1 | 3.2 | 6.3 | 3.8 | 4.82 |

**How to read this.** The scores are structured judgement, not measurement. Gaps under about 0.4 are not meaningful, so I1/I4/J1 and I2/I5 are effectively ties. The value is in the profile shapes:
- I3 has the easiest entry but the weakest moat.
- I1 has the strongest national fit but the weakest demand proof.
- I5 has strong strategic and export value but is blocked by gated buyers.

## The 5 going to Phase 4

1. **I1 Critical-wear parts:** scan → CAD → print or machine or cast, plus a curated vault.
2. **I4 Legacy automation continuity:** obsolescence audit, repair-exchange, HMI migration kits.
3. **J1 Cold-room reliability bundle,** with J4 filtration as an add-on.
4. **I3 Compressed-air leak-to-savings programme.**
5. **I2 Reliability route + sensors.** Chosen over I5 even though they are tied: I2 uses the same kit, visit and customer as I3, while I5's buyers are gated (vendor registration, SIRA, OEM warranties). **I5 is kept as the reserve**, to revisit if private charge-point operators say summer derating costs them revenue.

## The structural finding gets stronger

Four of the five (I1, I2, I3, I4) sell to **the same person**: the maintenance or engineering manager of a UAE SME plant (F&B, bottling, packaging, plastics). Each solves a different version of one fear: **"the line stops and we can't get it running fast enough."** Phase 4 therefore evaluates each one alone, and also as entry points into a single company. Working name: **"Line Continuity"**.
