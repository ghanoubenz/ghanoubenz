# Phase 5 — Market, Competitor and Customer Simulation

> ## ⚠️ SIMULATED OUTCOME — NOT EVIDENCE
> **MiroFish was not run.** It needs an LLM API key and a Zep Cloud key, and this container's network policy blocks both endpoints (see `00-tool-setup.md`).
> As a substitute, an independent agent ran a structured 16-persona simulation over four time steps: month 0, 3, 9 and 24.
> - Persona behaviour was grounded **only** in this study's evidence files (P3, P4, E4–E7). No new web searches were run.
> - Behaviour not supported by evidence is marked **[ASSUMPTION]**.
> - Every probability and reaction below is simulated.
>
> **To run the real MiroFish simulation later:** follow `mirofish/run_mirofish.py`, using `mirofish/seed-uae-line-continuity.md` and `mirofish/simulation-requirements.md`.

## Concepts simulated
- **A — "Line Continuity."** Sells to SME plants. Enters through **I3** (compressed-air leak-to-savings), then cross-sells **I1** (critical-wear parts), **I4** (legacy automation continuity) and **I2** (reliability routes).
- **B — J1 cold-room reliability bundle.** About AED 450–900 per cold room per month. Sold to hotels, central kitchens, food distributors, and restaurant chains with 5–20 outlets.

## Personas (16)
- **Buyers:**
  - maintenance manager at an F&B plant in Sharjah
  - owner of a plastics converter in Ajman
  - engineering manager at a bottled-water group
  - procurement officer at a packaging plant
  - hotel chief engineer
  - operations manager at a central kitchen
- **Competitors and partners:**
  - local OEM packaging agent
  - electronics repair lab
  - compressor OEM dealer
  - 3D-print bureau
  - CNC shop in Sharjah
  - condition-monitoring firm
  - sensor SaaS vendor
  - facilities-management (FM) company
- **Others:** a senior automation engineer (a hiring target) and a lender.

## Results — SIMULATED OUTCOME

| Question | A: Line Continuity | B: Cold-room bundle |
|---|---|---|
| **1. Adoption** | First paid I3 programme: **25–45%** of plants walked. Retention at month 24: **55–75%**. Cross-sell at month 24: I1 **30–45%**, I4 **10–20%**, I2 **10–20%**. Owner-run plants buy first. Large groups stay out of reach for about 24 months. | Paid pilot: **20–35%** of qualified pitches. Retention at month 24: central kitchens and chains **65–85%**, hotels **40–60%** (hotels drift to FM bundles). |
| **2. Competitor reaction** | The compressor OEM counters with free audits and replacement quotes. It **doesn't copy repair + re-survey**, because that would cannibalise compressor sales [ASSUMPTION]. The repair-lab partner goes around us within 6–9 months. The CNC shop copies once it holds the drawing. The OEM agent warns about warranty and "non-genuine" parts. | The sensor vendor adds a response partner and copies the bundle within **6–12 months**. FM firms bundle monitoring at token prices within 9–18 months. |
| **3. Engineer trust** | Printed parts are trusted for **non-contact, non-safety parts on out-of-warranty machines**, and not in the food zone. Migrations are trusted because of **the engineer, not the brand**; a 12-month warranty is the minimum. **Independent leak verification is the strongest trust asset**, but only if savings are metered, not claimed. | Trust is built by night response within hours. **One missed alarm breaks it.** |
| **4. Pricing** | I3: **mid price wins** (AED 12k/yr, with the survey credited, so effectively free on signing). A premium savings guarantee only works for plants above about 75 kW. I1: reverse-engineering fee plus pricing on downtime avoided. The vault converts only after 3 or more parts have been delivered. | **AED 600–650** per room per month wins with chains. **AED 900 with a 4-hour SLA and a stock-loss credit** wins with hotels and central kitchens. AED 450 attracts churn. |
| **5. Copyability** | Easy to copy: the camera, printing, sensors. Hard to copy: **a verified-savings dataset across plants, per-plant parts vaults with failure history, an obsolescence register, and a bilingual part-number SEO library. No single competitor spans compressors, parts and electronics.** | Easy to copy apart from **route density for night response** and compliance history. |
| **6. Supplier risk** | Hikmicro: low (there are alternatives). igus filament: medium (imported, so hold 3 months of stock; never substitute generic filament in the food zone). **Repair-lab partner: high** (use two labs and our own labelling). Grey-market automation parts: high. | **Sensor vendor: medium-high.** If Kelsius supplies the sensors, it owns the data and the customer. Prefer neutral distributors. Gasket stock is imported, so watch the summer peak. |
| **7. What breaks first as it scales** | **5 accounts:** founder time. **25 accounts:** shutdown-window clashes, about **AED 100–150k stuck in receivables**, and the need for an automation engineer. **75 accounts:** 3–4 technicians plus a CAD designer; cash fails unless billed in advance. | **25 accounts (~100 rooms):** one on-call technician can't meet the SLA. **75 accounts:** a dispatcher and a rota of 3+ technicians; AED 400–500k of receivables unless billed monthly in advance. |

## Five simulated insights
1. **I3 converts only as a near-free wedge.** OEM audits are free, so revenue must come from the repair programme, not the survey.
2. **The whole of thesis A depends on one link: cross-selling I1 and I4.** Below about 25% cross-sell, A is a low-moat leak-fixing business. **This is the single most important number to measure in the field.**
3. **B reaches revenue faster and has better standalone economics** (break-even at 52% of base). But it gets copied within 6–12 months, and night response is its first operational failure point.
4. **Trust is personal and depends on the category.** Parts outside the food zone on out-of-warranty machines are the beachhead. Large groups come later.
5. **Partners are latent competitors.** This applies to the repair lab, the CNC shop, the sensor vendor and the FM firm. Control of drawings, data and customer contact has to be designed in from day one.

## Simulated verdict
**A (Line Continuity)** wins on defensibility and founder fit, *if* I1 cross-sell reaches at least 30% by month 9. **B** is the safer cash path but is likely to be commoditised. Run the cheap Phase 6 tests for both in parallel, and decide on **measured** cross-sell and pilot conversion, not on this simulation.

## Falsification tests (moved into Phase 6)
1. Fewer than 1 of 5 walked plants signs a paid programme even with repairs included. **Or** 4–5 of 5 sign at the full AED 3.5k with no credit. Either result breaks the conversion model.
2. OEM dealers already run independent repair-and-re-survey programmes, or plants say "we already have that".
3. Fewer than 3 of 10 walked plants name 3 or more parts with OEM lead time over 3 weeks or cost over AED 2k.
4. Hotels with AMCs pay for guaranteed response at a rate equal to or higher than central kitchens.
5. Kelsius or FM firms already sell a priced "monitoring + response + gasket" bundle in 2026.
