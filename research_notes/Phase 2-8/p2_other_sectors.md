# Phase 2: Product gap discovery in the remaining sectors (electrical, appliances/HVAC, industrial, oil & gas, solar, automotive aftermarket, food-factory parts, maintenance spares, stationery, medical)

Research date: 2026-10-04. Data files:
- `/home/user/ghanoubenz/data/phase2_other_sectors_opportunities.csv`: 112 candidates, OS-001 to OS-112, in the exact OPPORTUNITY_SCHEMA. Machine-fit numbers are computed in every injection row.
- `/home/user/ghanoubenz/data/phase2_other_sectors_signals.csv`: 24 signals.

**Method caveat (read first).**
- **Searches.** I ran about 24 web searches in French, English and Arabic. The session's shared web-search quota (200) then ran out, so the planned ~40 searches were not reached. Food-factory, stationery and medical sectors got no new searches and rest on prior notes and engineering judgement.
- **Page fetches.** Every page fetch was blocked by the egress proxy: tsa-algerie.com, sogedim.net, mabricole.com.dz, assly.dz and caplugs.com. All new facts below come from **search-result snippets**, not full pages.
- **Ouedkniss, Facebook, forums.** Not reachable, so no maintenance-manager complaint ("pièce de rechange introuvable", "قطع غيار بلاستيكية غير متوفرة") could be read directly.
- **Engineering and cost figures.** All part weights, areas, cavities, cycles, mold costs, resin prices and the machine-hour rate in the CSV are **ASSUMPTION**:
  - Resin: PP/PE at 300 DZD/kg; PA/POM at 700–800; ABS at 550; PC/PBT at 900. No Algerian quote exists; see `resin_materials.md`.
  - Machine-hour rate: 2,000 DZD/h at 85% efficiency.
  - Retail to ex-works conversion: retail ÷ 1.19 VAT ÷ 1.6 channel margin.
- **Observed prices.** Only five retail listings came from the snippets; they are real (snippets of Algerian e-shop listings).

**Machine-fit method.** Clamp, shot and fit follow the schema:
- clamp = area × cavities × 1.15 × factor × 1.2.
- shot = part weight × cavities × 1.25 for a cold runner, or × 1.08 for a hot runner.
- The shot is converted to a PP-equivalent volume (× 0.9/density), so PA, POM and PC shots are judged fairly against the 45–200 g PP window of a 120 t press.

**Machine-fit results across the 112 rows:**

| Result | Rows |
|---|---|
| Fits 120T confidently | 72 |
| Borderline 120T | 19 (each row's stage_notes gives the reason) |
| Requires larger injection press | 13 |
| Other process | 4 |
| Requires extrusion | 3 |
| Requires blow molding | 1 |

**Verdicts across the 112 rows:**

| Verdict | Rows |
|---|---|
| GO-candidate (for validation) | 1 |
| INVESTIGATE, priority | 2 |
| INVESTIGATE | 29 |
| INVESTIGATE, low | 26 |
| KILL | 40 |
| FUTURE MACHINE | 14 |

---

## 1. Is there real, named-buyer pain in these sectors?

### Takeaway
Only two lanes have evidence that a **named Algerian buyer** wants local supply, and neither is yet a proven plastic-part shortage:
- **(a) Sonatrach's spare-parts localisation programme.** It holds 700k references, local content was at most 5% historically, it saved more than EUR 30M a year through national production, and it runs pre-qualification and technical days.
- **(b) Sider El Hadjar's seamless-tube unit (TSS).** It is producing 1,000 km of casing for Sonatrach in 2024–2026, so it consumes OCTG thread protectors whose source is unknown.

The car aftermarket shows a strong shortage signal at sector level. No factory-downtime complaint about missing imported plastic parts was found online.

### Cited Findings
- Sonatrach saved more than EUR 30M in one year by using nationally produced spare parts. Partners first met in Feb 2022 now make the parts, and the next step is electrical, electronic and more complex parts. — [Algérie Eco, 1 Mar 2023](https://algerie-eco.com/2023/03/01/pieces-de-rechange-sonatrach-a-economise-plus-de-30-millions-deuros-grace-au-recours-la-production-nationale/); [Radio Algérie](https://news.radioalgerie.dz/fr/node/22565)
- Sonatrach's spare-parts stock was over 700,000 references and local content did not exceed 5%, although more than 50% of purchases were paid in dinars. The target is 55% local spares. This comes from a search summary, and the exact page is uncertain. — [Algérie Eco ?p=35108](https://algerie-eco.com/?p=35108) / [Algérie360](https://www.algerie360.com/algerie-le-prive-industriel-simplique-dans-le-secteur-energetique/)
- "Pièces de rechange : Sonatrach prospecte des prestataires locaux". Sonatrach also issued pre-qualification notices for local designers and makers of precision mechanical spares. — [Algérie Eco ?p=127943](https://algerie-eco.com/?p=127943)
- 81 exhibitors attended the Hassi Messaoud technical days on mechanical, electrical and instrumentation manufacturing (May 2024). — [Algérie Eco, 20 May 2024](https://www.algerie-eco.com/2024/05/20/hassi-messaoud-81-exposants-aux-journees-techniques-dediees-a-la-fabrication-mecanique-electrique-et-instrumentation/)
- Sonatrach ordered 1,000 km of casing (USD 158.5M, in lots of 292 km and 766 km, delivered 2024–2026) from El Hadjar's TSS. TSS is the only seamless mill in the Maghreb, with casing from 6 to 16 in and 45,000 t/yr. — [Algérie Eco, 26 Oct 2023](https://algerie-eco.com/2023/10/26/sonatrach-commande-1000-km-de-tubes-pour-158-millions-a-sider-el-hadjar/). Shipments started in July 2024 (684 tubes on 12 trains). — [Algérie Eco ?p=196146](https://algerie-eco.com/?p=196146)
- TSA headlines report a severe car spare-parts shortage:
  - Importers say their import files have been blocked for about two years.
  - Parts cost 2–4× their real price.
  - 96% of respondents in a TSA poll say parts are hard to find.
  - The dates were not visible and the pages were blocked. — [TSA: grave pénurie](https://www.tsa-algerie.com/automobile-grave-penurie-de-pieces-de-rechange-en-algerie/); [TSA: la crise s'aggrave](https://www.tsa-algerie.com/pieces-de-rechange-automobile-en-algerie-la-crise-saggrave/)
- ENIEM's CKD air-conditioner start slipped from Aug to Dec 2024 because of administrative and Red Sea logistics delays (prior notes). — [Algérie Eco, 21 Nov 2024](https://www.algerie-eco.com/2024/11/21/leniem-a-signe-des-accords-avec-deux-entreprises-chinoise-et-turque/)
- Searches found **no** online evidence for:
  - appliance-spare shortages (Condor, ENIEM) in French or Arabic;
  - factory stoppages caused by missing plastic spares (Arabic query);
  - any Algerian thread-protector maker or importer (only patents and US makers Drilltec, MSI and Caplugs). — [Caplugs OCTG](https://www.caplugs.com/c/octg); [Rigzone MSI](https://www.rigzone.com/directory/company/5608/MSIProducts/)

### Inferences
- The best pain-backed lane is **"plastic spares for state energy companies"**. It is a service, not a product: reverse-engineer from a sample, then 3D print or machine prototypes, then mold repeat parts. Registration as a local supplier at Sonatrach and Sonelgaz is the gate.
- The car-aftermarket shortage probably covers plastic clips and fasteners too, but that is an inference, not evidence.

### Gaps
- No maintenance manager, factory or forum post naming a specific missing plastic part was found. Interviews are needed (see section 9).
- The plastic share of Sonatrach's 700k references is unknown.

---

## 2. Electrical (conduit clips, cable clips, glands, trunking accessories, markers, wall plugs, small housings, cable end caps)

### Takeaway
Retail prices confirm that imported commodity fixings are **very cheap**. Clips with nails cost 2–3 DZD and nylon PG9 glands 35–50 DZD. That kills cable clips with nails, cable ties and glands for a start-up. Plasterboard butterfly anchors (55 DZD retail) and hammer-fix anchors (15 DZD) show headroom on paper. The open niches are **trunking accessories matched to local extruders' profiles** and **cable-maker consumables (ENICAB)**. Small junction and flush boxes are already contested by local makers.

### Cited Findings
- PG09 nylon IP68 cable gland sells at 50 DZD (another listing shows 35 DZD). — [SOGEDIM](https://sogedim.net/product/presse-etoupe-pg09/)
- Ø8 PP cable clip with nail sells at 2 DZD/pc. — [SOGEDIM](https://sogedim.net/product/attache-cable-o8mm/). Round clips with steel nails sell at 200/250/300 DZD per 100 for 12/14/16 mm. — [Mabricole](https://mabricole.com.dz/accessoires-d-electricite/lot-de-100-pcs-attache-cable-ronde-avec-clou-en-acier-14mm-max-clips-ronde-pour-fil-en-plastique-5829)
- The hammer-fix anchor 8×80 sells at 15 DZD — [SOGEDIM](https://sogedim.net/product/cheville-a-frapper-8x80-mm-gris/). The butterfly anchor 08 without screw sells at 55 DZD — [SOGEDIM](https://sogedim.net/product/cheville-papillon-08-sans-vis/). Assly lists chevilles in boxes. — [Assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/)
- Turkish OZTURK cable ties sell at 450 DZD per 100 (prior notes). — [Mabricole](https://mabricole.com.dz/fr/fixation/jeu-de-colliers-de-serrage-en-plastique-100-200mm-250pcs-onsite-1845)
- The local HAOUAS brand sells junction boxes alongside Spanish FAMATEL (prior notes). — [SOGEDIM](https://sogedim.net/product/boite-etanche-electrique-80x80-mm/)
- Searches for an Algerian maker of glands, wall plugs or ICTA/trunking clips returned only European brands (ING Fixations, Legrand, HellermannTyton) and generic Algerian activity codes. — [123elec](https://www.123elec.com/cables-gaines-conduits/colliers-fixation.html); [conformepro](https://conformepro.dz/resources/codes-activites/production-de-biens/fabrication-de-materiaux-de-construction-en-plastique)
- Sonelgaz's SAIEG makes meters (El Eulma) and switchboards (Oran), and exports meter spares to Tunisia, so meter plastics are captive. — [Algérie Eco, 12 Aug 2026](https://algerie-eco.com/2026/08/12/sonelgaz-signature-de-deux-accords-pour-la-fabrication-locale-dequipements-electriques/); [Radio Algérie](https://news.radioalgerie.dz/fr/node/52006)
- ENICAB produces about 20,000 t/yr of copper cable (prior notes). GPI lists cable-industry components in its scope. — [Dzair Tube](https://www.dzair-tube.dz/en/enicab-boosts-rail-sector-with-2000-tons-of-annual-cable-production-eyes-regional-export-expansion); [Algérie360](https://www.algerie360.com/gpi-tissemsilt-pieces-plastiques-industrie-auto/)

### Inferences
- Computed economics, before mold amortisation:
  - Butterfly anchor (OS-010): about 2.4 DZD cost against about 29 DZD implied ex-works. This is the only GO-candidate, and it rests on a **single retail listing**.
  - Hammer-fix sleeve (OS-009): the margin depends on the bought-in nail-screw (cost unknown).
  - Clip with nail (OS-004): 19–46% margin at an ASSUMED 0.5 DZD nail, before manual insertion. KILL.
  - Glands (OS-011): 65–75% paper margin, but about 12–18 molds with unscrewing cores across sizes. KILL.
- Every electrical fixing computes as a fit on 120 t once cavities are set to 32–64.

### Gaps
- No wholesaler volumes. Trunking extruders in Algeria were not identified. ENICAB's consumables list is unknown.

---

## 3. Appliances and HVAC (feet, knobs, condensate fittings, filter caps, covers, clips; after-sales for Condor, ENIEM, Géant, Samha, Iris)

### Takeaway
The OEM pull is real in volume (Condor–Hisense planning 2M ACs/yr, Samha with only 30–40% AC integration, Géant adding units), but **no part-level sourcing or after-sales shortage evidence** surfaced. Condor and GPI cover large parts. Fitting candidates are small generic parts (levelling feet, strain-relief clamps, condensate elbows, filter caps, knobs) to be checked against CKD kit contents.

### Cited Findings
- Samha (Sétif) runs at about 5M units/yr with an AC integration target of only 30–40%. — [Algérie Eco ?p=183402](https://algerie-eco.com/?p=183402)
- Condor–Hisense plans 2M ACs/yr in BBA. — [Algérie Eco ?p=211059](https://algerie-eco.com/?p=211059). Condor claims 45–100% integration and a "100% Algerian" fridge. — [Algérie Eco, 14 Jul 2026](https://algerie-eco.com/2026/07/14/condor-present-sur-18-marches-et-realise-50-des-exportations-algeriennes-en-electromenager/)
- Géant is adding AC and fridge units (70% fridge integration). — [Dzair Tube](https://www.dzair-tube.dz/en/geant-electronics-expands-production-with-two-new-units-for-air-conditioners-and-refrigerators-in-january)
- ENIEM signed Turkish (heaters) and Chinese (CKD ACs) partnerships, its start slipped, and it has payment risk (prior notes). — [Algérie Eco](https://www.algerie-eco.com/2024/11/21/leniem-a-signe-des-accords-avec-deux-entreprises-chinoise-et-turque/)
- Iris (Sétif) opened an electronics complex in 2019 (TVs, smartphones). No plastic-sourcing information was found. — [Algérie Eco ?p=43308](https://algerie-eco.com/?p=43308)
- Searches for appliance after-sales spare shortages returned only French consumer content and Algerian activity codes. — [conformepro](https://conformepro.dz/ar/resources/codes-activites/الخدمات/تركيب-تصليح-و-صيانة-الأجهزة-الكهرومنزلية)

### Inferences
- The best appliance targets are generic small parts sold to the **local-integration managers** at Samha, Géant and Condor–Hisense (OS-032 feet, OS-039 condensate elbows, OS-046 strain-relief). Model-specific aftermarket spares (knobs, filter caps) fragment into many molds per small volume.
- Door bins, detergent drawers, 200 mm grilles and 10" filter housings need 160–300 t presses.

### Gaps
- The contents of the CKD kits, meaning which plastics are still imported, are unknown. No price was found for any appliance spare.

---

## 4. Industrial components (caps, plugs, thread protectors, knobs, bushings, gears, spacers, cable guides, custom housings)

### Takeaway
Industrial components are technically ideal for 120 t: LDPE caps and plugs in 16–32 cavities, and PA-GF knobs with inserts. But **no named industrial buyer** was found online, so every row is INVESTIGATE. The "caps & plugs" family (OS-051/052/053/073) is the best catalogue-able set, and it doubles as a door-opener with Sonatrach maintenance.

### Cited Findings
- Global protection-cap makers (Caplugs, Essentra) are the reference suppliers. There is no evidence they supply Algeria directly. — [Caplugs](https://www.caplugs.com/thread-and-flange/); [Essentra](https://ecompreprod.essentracomponents.com/fr-nl/s/pehd?page=2)
- CDTA (Baba Hassen) offers reverse engineering and prototyping (prior notes). — [CDTA](https://www.cdta.dz/en/?p=12201)
- Sonatrach's local-spares programme is described in section 1.

### Inferences
- Knobs and feet with steel inserts are dominated by bought-in metal cost. Bushings and gears are usually machined at the low volumes a maintenance buyer needs, so molding pays only for repeat sizes.

### Gaps
- No hydraulic-hose assembler, small-tube maker or machine builder was named. This needs a Kompass or field sweep.

---

## 5. Oil & gas (OCTG thread protectors: Alfapipe, Tosyali, Sonatrach suppliers)

### Takeaway
Alfapipe and Tosyali make **large-diameter welded line pipe** (Alfapipe Battioua alone has 360 kt/yr; Tosyali makes mega-pipe over 1,300 mm). That pipe needs end or bevel protection far beyond a 120 t press, if any protection is used at all. The real **OCTG thread-protector buyer is Sider El Hadjar TSS** (casing 6–16 in). Imported premium OCTG (Vallourec, USD 250M+) arrives with protectors already fitted. On the founder's press only the 4½–5½ in protectors fit. TSS's range starts at 6 in, where 6⅝–7 in protectors already exceed the 120 t shot.

### Cited Findings
- Alfapipe opened its Battioua (Oran) unit in July 2025 (360,000 t/yr welded pipe plus coating), in addition to Annaba and Ghardaïa. — [AISU](https://new.aisusteel.org/archives/214); [Yieh](https://yieh.com/en/News/algeria-opens-new-steel-pipe-production-unit-in-battioua/155657)
- Tosyali (Bethioua) has 300 kt/yr of spiral pipe capacity and exported 15,000 t to Angola. — [Algérie Eco](https://algerie-eco.com/2022/09/26/tosyali-algerie-exportation-de-15-000-tonnes-de-tubes-vers-langola/)
- TSS has the Sonatrach casing contract described in section 1. — [Algérie Eco](https://algerie-eco.com/2023/10/26/sonatrach-commande-1000-km-de-tubes-pour-158-millions-a-sider-el-hadjar/)
- Vallourec supplies threaded OCTG with VAM premium connections from Brazil, China, France and Indonesia (2025–2026). — [Vallourec PR](https://www.vallourec.com/app/uploads/2025/04/20250408-Vallourec_Communique-de-Presse_Sonatrach.pdf)
- Sonatrach imported USD 731M of tubing in 2009–10 while AMPTA (ex-TSS) struggled (headline). — [Algérie360](https://www.algerie360.com/alors-que-les-travailleurs-dampta-ex-tss-etaient-en-grande-difficulte-sonatrach-a-importe-en-20092010-pour-731-millions-de-dollars-de-tuberie/)

### Inferences
Computed fits, based on assumed part weights:

| Row | Protector | Clamp | Shot (PP-eq) | Result |
|---|---|---|---|---|
| OS-068 | 4½–5½ in | 66 t | 178 g | Fits |
| OS-112 | 6⅝–7 in | 104 t | 332 g | Larger press (shot) |
| OS-069 | 9⅝–13⅜ in | 215 t | — | Larger press (needs 300 t+) |

- API protectors for premium connections may also need licensor approval.
- **Single buyer, high switching difficulty.** Make one call to TSS purchasing before any further work.

### Gaps
- What TSS currently fits, where it is from, the price and the annual quantity by size are all unknown. Any Algerian protector importer or recycler is unknown.

---

## 6. Solar (cable clips, MC4 caps, module edge protectors)

### Takeaway
There is a **policy pull** (Solar 1000 MW requires at least 30% national integration; LONGi in talks on local production) but no buyer pain. Module plastics arrive embedded in Chinese imports (850 MW in H1 2025). The only plausible products are UV-PA66 cable clips and transport corners for local module assemblers. Junction boxes are a KILL because of certification.

### Cited Findings
- National integration of at least 30% is required for Solar 1000 MW. Junction box, frame and glass shares of module cost are about 6%, 10% and 16% (search summary). — [Legal Doctrine](https://legal-doctrine.com/edition/LAlg%C3%A9rie-bient%C3%B4t-leader-dans-le-domaine-des-panneaux-photovolta%C3%AFques)
- The PM received a LONGi delegation on local panel production (Apr 2025). — [Algérie Eco](https://algerie-eco.com/2025/04/21/fabrication-de-panneaux-solaires-en-algerie-ghrieb-recoit-une-delegation-de-la-societe-chinoise-longi/)
- Algeria imported 850 MW of Chinese panels in H1 2025 (prior notes). — [Algérie Eco](https://algerie-eco.com/2025/08/10/algerie-850-mw-de-panneaux-solaires-chinois-importes-au-premier-semestre-2025/)
- ENERGIA SUN SOLUTION (PV supports) was created; this is an old headline. — [Algérie Eco ?p=26255](https://algerie-eco.com/?p=26255)

### Inferences
- **INVESTIGATE (low):** UV-stabilised PA66 is not stocked locally (resin notes), which blocks fast supply.

### Gaps
- No EPC or installer names; the status of local module lines is unknown.

---

## 7. Automotive small components (aftermarket only)

### Takeaway
OEM supply stays **KILL**: GPI's import ban from 1 Jan 2027, IATF/PPAP requirements, and more than 200 qualified SMEs. **Aftermarket clips and fasteners** are INVESTIGATE because of the strong sector-level parts shortage reported by TSA.

### Cited Findings
- The TSA shortage reporting is described in section 1. — [TSA](https://www.tsa-algerie.com/automobile-grave-penurie-de-pieces-de-rechange-en-algerie/)
- Imports of auto plastic parts that GPI can make end from 2027. — [ObservAlgérie, 25 Sep 2026](https://observalgerie.com/2026/09/25/economie/lalgerie-annonce-la-fin-de-limportation-des-pieces-plastiques-pour-voitures/)
- More than 200 SMEs are said to be able to supply the car industry. — [Algérie Eco, 26 Sep 2024](https://algerie-eco.com/2024/09/26/industrie-automobile-plus-200-pme-sous-traitantes-capables-dapprovisionner-secteur/)
- Counterfeit auto parts are among the most counterfeited goods (prior notes, supply_ecosystem.md).

### Inferences
- Pick 10–20 clip types for the dominant fleet models (48-cavity PA66 tools fit easily). Avoid branded caps (counterfeiting) and pressure caps (safety).

### Gaps
- No aftermarket wholesaler was named, and the TSA article dates are unknown. Whether the GPI ban also restricts aftermarket imports of clips is unknown.

---

## 8. Food-factory parts, maintenance spares, stationery, medical

### Takeaway
No new evidence was gathered (search quota exhausted). On engineering grounds:
- Wear strips (UHMW-PE) and star wheels cannot be injection molded.
- Tabletop chain links are brand-precision parts.
- Guide-rail brackets and clamp knobs are feasible reverse-engineered spares.
- Stationery is seasonal and China-priced, so KILL.
- Medical is KILL: ISO 13485, and MBS PLAST (Sétif) is already qualified.

### Cited Findings
- MBS PLAST runs ISO 13485 clean-room medical injection (prior notes). — [Maghreb Pharma](https://www.maghrebpharma.com/en/exhibitors/mbs-plast-240861)
- SANIST 2025 (7th edition, 70 exhibitors) focuses on local components and spare parts. — [Algérie Eco ?p=215691](https://algerie-eco.com/?p=215691)

### Gaps
- No food-plant maintenance buyer was named. Stationery and medical demand were not searched this session.

---

## 9. GO / INVESTIGATE / KILL by family

| Family (rows) | Verdict | Reason |
|---|---|---|
| Plasterboard / hammer-fix anchors (OS-009, OS-010) | **GO-candidate → validate** | Real retail prices of 15–55 DZD against about 2.5 DZD resin+machine cost; high volume; fits on 16–20 cavities. Risk: single listings, Chinese bulk, nail-screw cost. |
| Plastic spares service for Sonatrach/Sonelgaz and large plants (OS-098, plus OS-059, OS-073) | **INVESTIGATE – priority** | Only lane with named-buyer, programme-level demand for local spares. Needs supplier registration, CNC/3D-print partner, repeat parts. |
| OCTG thread protectors for TSS (OS-068) | **INVESTIGATE – priority call** | Named single buyer with verified volume; only the 4½–5½ in sizes fit. TSS's 6–16 in range mostly needs 200–450 t presses. API and licensor risk. |
| Protection caps & plugs (OS-051 to OS-054, OS-073) | INVESTIGATE | Ideal multi-cavity LDPE parts; catalogue family; buyers unnamed. |
| Trunking accessories (OS-014 to OS-016) | INVESTIGATE | Must match local trunking profiles; find the extruders. |
| Conduit clips/couplers (OS-001, OS-002) | INVESTIGATE | Simple, fit easily; no price or pain yet; construction-researcher overlap. |
| Cable-maker consumables (OS-025, OS-063) | INVESTIGATE | ENICAB volume verified; GPI scope overlap; heat-shrink may replace. |
| Appliance generic OEM parts (OS-032, OS-039, OS-046, OS-030, OS-037) | INVESTIGATE | Samha's low integration means imported kits; need integration-manager contact. ENIEM only on advance payment. |
| AC installer consumables (OS-040, OS-042) | INVESTIGATE | Seasonal; needs a duct-extruder partner. |
| Auto aftermarket clips (OS-078, OS-082, OS-084, OS-066) | INVESTIGATE | Sector shortage strong; model fragmentation; counterfeit environment. |
| Machine knobs/feet/handles; food guide brackets (OS-055 to OS-058, OS-092, OS-096) | INVESTIGATE | Feasible; insert cost dominates; buyers unnamed. |
| Custom housings (OS-064) | INVESTIGATE | Job-shop filler; low copy risk. |
| Solar clips/corners (OS-075, OS-077) | INVESTIGATE (low) | Policy pull only; UV-PA66 not stocked. |
| Cable clips with nail, cable ties, adhesive mounts (OS-004 to OS-007, OS-081) | **KILL** | Retail 2–4.5 DZD/pc; nail insertion or PA66 conditioning; Turkish/Chinese commodity. |
| Cable glands and locknuts (OS-011, OS-012) | **KILL** | 35–50 DZD retail; 12–18 unscrewing molds; TPE seal not stocked. |
| Flush/junction/surface boxes (OS-020 to OS-022, OS-028) | **KILL as lead** | Local HAOUAS and others already on shelf. |
| Meter parts, terminal blocks, lamp holders, PV junction box (OS-019, OS-024, OS-027, OS-111) | **KILL** | Certification or captive (SAIEG). |
| Auto OEM parts, coolant caps, wheel caps, valve caps (OS-083, OS-086, OS-088, OS-089) | **KILL** | IATF/GPI, safety, brand IP, negligible value. |
| Tabletop chains, bearing housings, impellers, drag chains, spacers (OS-093, OS-097, OS-100, OS-062, OS-061) | **KILL** | Brand precision systems or commodity. |
| Stationery (OS-101 to OS-106) | **KILL** | Seasonal, China-priced, assembly/printing steps. |
| Medical (OS-107 to OS-110) | **KILL** | ISO 13485; MBS PLAST incumbent. |

---

## 10. Future machine opportunities (not 120 t injection), with buyer pull observed

| Item | Process needed | Buyer pull observed |
|---|---|---|
| OCTG protectors 6⅝–7 in (OS-112) and 9⅝–13⅜ in (OS-069) | 200–450 t injection | **Verified volume:** TSS casing 6–16 in for Sonatrach, 1,000 km, 2024–26 |
| Line-pipe bevel/end protectors 500–1,400 mm (OS-071) | Very large injection, rotomolding or thermoforming | Alfapipe (3 units, Battioua 360 kt/yr), Tosyali (300 kt/yr); protection practice UNKNOWN |
| Distribution-board enclosures (OS-023) | 350–450 t | Housing boom (indirect); no buyer named |
| Wire spools/bobbins (OS-026) | 160–250 t | ENICAB (~20 kt/yr cable) |
| Fridge door bins (OS-034), detergent drawers (OS-038) | 160–300 t | Condor/Géant/Samha volumes; probably captive |
| Ventilation grilles 200 mm+ (OS-049) | about 250 t | None named |
| Water filter housings 10" (OS-050) | 160–200 t (shot) | None named |
| Licence-plate frames (OS-087), mud flaps (OS-090) | 160–250 t (mold over 410 mm) | Car-parts shortage (TSA) |
| AC line-set duct (OS-041), conveyor wear strips (OS-091), binding combs (OS-104) | Extrusion | AC volumes (Condor–Hisense 2M/yr planned); food plants unnamed |
| Urinal bottles (OS-109) | Blow molding | Hospitals; regulatory barrier |
| Star wheels / change parts (OS-094), composite protectors (OS-070) | CNC machining; steel + overmould | Food plants; Sonatrach drilling |

---

## 11. Next validation actions (ordered)
1. **Call Sider El Hadjar TSS purchasing.** Ask:
   - protector type, origin, unit price and quantity by size;
   - API and licensor requirements;
   - whether used protectors are recycled.
2. **Register as a local supplier with Sonatrach and Sonelgaz.** Request their lists of imported plastic spares, and attend the next Hassi Messaoud technical days and SANIST.
3. **Quote anchors with SOGEDIM, Mabricole, Assly and two El Hamiz/El Eulma quincaillerie wholesalers.** Ask for the price per 100 and per 1,000 for butterfly, hammer-fix and nylon anchors, monthly volume and origin.
4. **Call Samha, Géant and Condor–Hisense local-integration managers.** Ask which small plastics (feet, clamps, condensate elbows) are still in CKD kits.
5. **Call three aftermarket parts wholesalers.** Ask which plastic clips are out of stock and their prices.
6. **Ask ENICAB** for its list and prices of cable end caps and drum consumables.
