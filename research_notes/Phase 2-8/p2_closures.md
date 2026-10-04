# Phase 2: Personal care, cosmetics and detergent closures. Product gap discovery

Researched 2026-10-04. Data files:
- `data/phase2_closures_opportunities.csv`: 30 rows, CL-001 to CL-030, in the schema format, with machine-fit numbers.
- `data/phase2_closures_signals.csv`: 19 new signals.

**Method limits. Read these first.**
- About 37 web searches were run before the session-wide search cap (200) was hit.
- Every Algerian page fetch failed because the egress proxy blocks it: Ouedkniss, Kompass, ConformePro. Everything Algerian here comes from **search snippets**.
- No buyer or supplier was interviewed.
- **No DZD price for any plastic closure was found anywhere.** All DZD price figures below are **researcher arithmetic** from Chinese FOB listings (ASSUMPTION). Treat them as benchmarks, not market prices.
- No buyer, contact or price was invented. Unknowns are written UNKNOWN.

Cost model used in the CSV (all ASSUMPTION unless cited):

| Input | Value | Basis |
|---|---|---|
| Resin | 0.295 DZD/g, +5% losses | PP/HDPE 285 DZD/kg, the midpoint of the 220–350 estimate in `resin_materials.md`, plus masterbatch |
| Press cost | 700 DZD/h | Energy of 50–80 DZD/h is sourced in `cost_inputs_market_prices.md`; the rest is assumed |
| OEE | 75% | |
| Mould exchange rate | 153 DZD/US$ | Official rate of 133 plus 5% duty and freight |
| Landed import, official FX | FOB × 1.2 (freight) × 1.35 (30% DD + TCS + PRCT) × 1.1 (clearing) = **FOB × 237 DZD/US$** | |
| Landed import, parallel FX | Same formula = **FOB × 428 DZD/US$** | |

---

## 1. Shampoo-cap verdict: what most likely went wrong?

### Takeaway
**There is no evidence of a nationwide cap shortage.** The best-supported explanation is a **mould-cost plus MOQ / short-run problem on a dispensing closure (flip-top or disc-top) that matches one particular bottle neck**:
- the brand would have to fund a dedicated mould (US$2k–15k, 6–10 weeks);
- local molders will only run it if the brand pays for that mould and orders a large first run;
- importing instead means a 10k MOQ, FX and a PPI import file.

Confidence: **WEAK SIGNAL** (inference from indirect evidence). The founder's anecdote itself is unverified and has no public trace. Only an interview can settle it.

### Cause-by-cause scoring

| Candidate cause | Support | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| Nationwide shortage of caps | **Low** | None. No press or social report of a closure shortage in FR or AR searches | SGT makes about 2 bn caps/yr; SIPEM advertises dispensing and pouring caps; Chinese caps are available from 1k–10k MOQ at about US$0.01–0.045 | STRONG SIGNAL against |
| **Mould cost** (needs a new mould for the bottle or cap design) | **High** | SIPEM's ad sells "étude technique … jusqu'à la réalisation des moules", i.e. customer-specific mould projects ([Ouedkniss snippet](https://www.ouedkniss.com/fabrication-des-produits-en-plastique-alger-oued-smar-algerie-services-d22745209?lang=fr)). A flip-top IMC mould costs US$2k–15k from China ([MIC](https://www.made-in-china.com/manufacturers/flip-top-cap-mould.html)) | Not confirmed by the buyer | WEAK SIGNAL |
| **MOQ / unwilling to do short runs** | **High** | Fragmented demand: about 250 Algerian exhibitors at Cosmetica 2026 (Phase 1) and 2,383 soap/toilet-prep firms in D&B. Chinese MOQ is typically 10k per item and colour. Local molders with their own moulds optimise for long runs (ASSUMPTION) | No supplier statement found | WEAK SIGNAL |
| Unusual neck size | **Medium** | No Algerian source states which neck finishes local EBM blowers use. SGT's 11 cap families are beverage and oil necks (29/25, 30/25, 33, 38 mm), not 24/410 or 28/410 ([Algérie360](https://www.algerie360.com/specialisee-dans-la-fabrication-de-preformes-et-de-bouchons-en-polyethylenelentreprise-francaise-sgt-ouvre-une-deuxieme-usine-en-algerie/)) | A standard 24/410 or 28/410 neck would let them buy a stock Chinese flip-top cheaply | UNKNOWN |
| Hinged / dispensing type itself (flip-top or disc-top not made locally) | **Medium–High** | No Algerian flip-top or disc-top producer found in about 37 Phase 2 queries plus Phase 1 | SIPEM *might* make them (it says "bouchons distributeurs/verseurs") | WEAK SIGNAL |
| Colour unavailable | **Low–Medium** | Plausible for small lots | No complaint found; Chinese suppliers offer custom colour at 10k MOQ | ASSUMPTION |
| Quality (leak, hinge failure) | **Low–Medium** | Hinge and IMC are hard to make (patents, Stackteck) | No complaint found | ASSUMPTION |

### Inferences
- The most likely sentence the shampoo maker heard is: "We don't have a mould for that cap. A mould costs X and the minimum is Y."
- That is a **mould-funding and short-run gap**, not a capacity gap. It matches a business model of:
  - stock moulds for 24/410 and 28/410 flip-tops and disc-tops;
  - colour from 5k pcs;
  - optional brand-funded custom moulds.

### Gaps
- The shampoo maker's identity, cap type, neck, volume, and who refused and why.
- SIPEM's real range, MOQ, prices and whether it can do hinged IMC.
- Any DZD price.

---

## 2. Local vs imported, by closure type

| Closure | Local supply evidence | Imported? | Fit for a 100–120 t press (CSV numbers) |
|---|---|---|---|
| Beverage PCO and 38 mm (CL-027) | **Strong**: SGT (Rouiba and Sétif), PTD, Alpha PET, Tap Chihani | Little | Technically fits (16-cav: 74.5 t, 40 g), but incumbents run 32–72-cavity hot runners. Classed as **Requires larger injection press** on economics |
| Flip-top 24/410 (CL-001) | None confirmed. SIPEM is possible | Likely, via traders and bottle-cap sets (WEAK) | **Fits**: 12-cav, 44 t, 48 g shot. An 8-cav mould gives only 32 g, too small for a 120T screw but fine on 100T |
| Flip-top 28/410 (CL-002) | None confirmed | Likely | **Fits**: 12-cav, 55 t, 64.5 g. Part is 4.3 g, Ø30.6 mm ([Berlin](https://berlinpackaging.eu/en-international/products/pp-flip-top-28-410-20-025)) |
| Disc-top 24/410 and 28/410 (CL-005/006) | None found | Likely | **Fits**: 12-cav body, 44–55 t. Needs a second mould for the disc, plus assembly |
| Plain screw 24/410, 28/410, 28/400 (CL-007/008) | Probably general molders and blowers (unconfirmed) | Mixed | **Fits**: 16-cav, 59–74 t |
| Push-pull 28 mm (CL-009) | UNKNOWN | UNKNOWN | **Fits**: 2 moulds plus assembly |
| Laundry measuring cap (CL-010) | UNKNOWN | UNKNOWN | **Fits**: 4-cav, 75 t, 72 g |
| Jerrycan TE 38 mm (CL-011) | SGT has a 38 mm family; blowers probably cap their own | Mostly local (WEAK) | **Fits**: 8-cav, 69 t |
| Jerrycan TE 50–60 mm (CL-012) | UNKNOWN | UNKNOWN | **Fits**: 4-cav, 77.5 t |
| Cosmetic jar lids and jars, hair-gel tubs (CL-014/015/016) | Not researched | Likely imported sets (ASSUMPTION) | **Fits** (lid 6-cav at 85 t; mould width 400 mm is at the tie-bar limit) |
| Pump and trigger overcaps (CL-017), aerosol overcaps (CL-030) | UNKNOWN | Overcaps come with imported pumps | **Borderline**: shot is 35–40 g, so better on 100T |
| Orifice reducers and plugs (CL-013) | SIPEM probable | UNKNOWN | **Borderline**: 21 g shot. Better suited to a 60–80T press |
| Wipes flip lid (CL-022) | UNKNOWN | UNKNOWN | **Borderline**: 4-cav needs 102.6 t |
| Lotion and foam pumps, triggers, fine-mist (CL-023 to 026) | Only SIPEM's claim of "pompettes" (possibly assembly). PAFIX and Ouedkniss traders resell | **Mostly imported** (STRONG SIGNAL for trader resale) | **Other process**: 6–12 moulds, metal springs and balls, automatic assembly |
| HDPE and PET bottles (CL-028/029) | Local EBM blowers (Soloplast, SIPLAST, PAP Plast, HM Plast, Compex); PTD and SGT preforms | Mixed | **Requires blow molding**. These firms are channel partners, not targets |

**Customs.** Line 3923.50.92 (plastic stoppers and lids) carries DD 30%, VAT 19%, TCS 3% and PRCT 2%. **No DAPS appears in the snippet** ([ConformePro](https://conformepro.dz/ar/resources/tarif-douanier/sous-position/39.23.509200/سدادات-وأغطية-بلاستيكية)). GAFTA (ZALE) origin may be exempt from duty. So closures have about 30–35% protection, **not** the 60% DAPS seen on 3923.10. Confirm this with a transitaire.

---

## 3. Price benchmarks

All FOB figures are from Made-in-China and Alibaba listing snippets (WEAK SIGNAL; listings, not quotes). The landed columns are researcher arithmetic. The local unit cost is from the CSV model (ASSUMPTION).

| Item | FOB US$/pc (MOQ) | Landed, official FX (DZD) | Landed, parallel FX (DZD) | Local unit cost (DZD) |
|---|---|---|---|---|
| Flip-top 24/410 | 0.01–0.03 (1k–10k) | 2.4–7.1 | 4.3–12.8 | 2.2 |
| Flip-top 28/410 | 0.012–0.045 (10k typical) | 2.8–10.7 | 5.1–19.2 | 2.75 |
| Disc-top 24/410 and 28/410 | 0.02–0.12 (1k–30k) | 4.7–28.4 | 8.6–51 | 3.1–3.5 |
| Screw caps 20–28 mm | 0.01–0.03 (1k) | 2.4–7.1 | 4.3–12.8 | 1.4–1.75 |
| Push-pull 28 mm | 0.01–0.05 (5k) | 2.4–11.9 | 4.3–21 | 3.1 |
| Laundry measuring cap | 0.03–0.15 (10k–20k) | 7.1–35.6 | 12.8–64 | 7.3 |
| TE cap 38 mm | 0.025–0.03 (10k) | 5.9–7.1 | 10.7–12.8 | 2.6 |
| Jerrycan/lube TE cap | 0.11–0.12 | 26–28 | 47–51 | 6.0 |
| Lotion pump 24/410 | 0.04–0.10 (10k); 0.045 at 1M | 9.5–23.7 | 17–43 | n/a |
| Trigger 28/410 | 0.05–0.18 (about 0.09 at 10k) | 11.9–42.7 | 21–77 | n/a |

**Flip-top mould benchmark** ([MIC](https://www.made-in-china.com/manufacturers/flip-top-cap-mould.html); listings, not quotes):
- 4–16 cavities, with in-mould closing available;
- cycle 10–18 s (about 20 s at 16 cavities);
- 8-cavity from about US$2k, 16-cavity US$8–15k.

Global incumbents run 40–50+ cavities with IMC ([US10926443](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10926443)).

**Economics, in plain words.** Against a brand that imports directly at the official rate, a stock flip-top made locally has little price room: about 2.2–2.75 DZD cost against about 4.7–5.9 DZD landed. The margin is real only in these cases:
- (a) buyers who pay parallel-rate trader prices;
- (b) short runs or colours below the Chinese 10k MOQ;
- (c) urgent or reliable supply with no PPI or domiciliation file;
- (d) brand-funded custom moulds.

**Sell service, not unit price.**

---

## 4. Buyers ranked by likelihood of pain

1. **The founder's shampoo-maker contact.** Name not given to the researcher. This is the only direct pain report (WEAK SIGNAL).
2. **Small and new cosmetic and shampoo brands.** Examples: the Algiers shampoo/shower-gel start-up seeking component suppliers ([Kompass lead](https://fr.kompass.com/lead/0005886583/), WEAK), Farfasha, Volume cosmétique. They buy lots too small for Chinese MOQ and rely on traders (PAFIX, E.C.A Birtouta, HS emballage, Ouedkniss sellers). Pain is highly likely, but volumes are small.
3. **Contract and private-label fillers.** Dermal Group, Laboratoires Sabrinel, Groupe ECI and White Industry (WEAK; locations UNKNOWN). They serve many brands, so they need many SKUs and colours in short runs. This is the **best aggregator** target.
4. **Mid-size Algerian leaders with many SKUs.**
   - Labonedjma (Larbaâ, Blida; 600+ SKUs).
   - Laboratoires Venus/SAPECO (Ouled Yaich). It is reported to make its own packaging, so it may self-supply.
   - Univers Détergent (Aigle/Top; Algiers).
   - ENAD/Shymeca (bleach, liquid soap, surface cleaners).
   - SM2I (Aïn Témouchent).
5. **EBM bottle blowers as a channel.** PAP Plast (Algiers), HM Plast (Blida), Soloplast (El Eulma), SIPLAST (Sétif), Compex (BBA). They sell bottle-and-cap sets, so they are distributors, not end-buyers.
6. **Multinationals.** Henkel (Réghaïa; Gliss shampoo local since Dec 2025), Unilever (Oran), Hayat DHC (Bouinane). They have the largest volumes but the **lowest pain**: global closure contracts and qualification barriers. Approach them later, for measuring caps or TE caps only.

---

## 5. GO / INVESTIGATE / KILL by closure type

| Closure type | Call | Condition to upgrade or kill |
|---|---|---|
| Stock flip-top 24/410 and 28/410 PP, colour from 5k pcs (CL-001/002/003) | **INVESTIGATE → leaning GO** | GO if (a) the shampoo maker confirms a 24/410 or 28/410 dispensing need with at least 50k/yr, **and** (b) SIPEM does not already offer hinged flip-tops at 5–10k MOQ. KILL if 3 or more local suppliers offer them at 5k MOQ at or below about 6 DZD |
| Brand-funded custom flip-top (CL-004) | **INVESTIGATE** (likely the shampoo-maker case) | GO when one brand prepays the mould (US$8–12k) and commits at least 50k pcs |
| Disc-top 24/410 and 28/410 (CL-005/006) | INVESTIGATE (second, after flip-top) | Needs a disc vs flip share from traders |
| Measuring/dosing cap for liquid laundry (CL-010) | INVESTIGATE | Bulky, so freight favours local supply. Needs neck data from Hayat, UD and the "Life" brand owner |
| Push-pull 28 mm (CL-009) | INVESTIGATE (low) | Shelf check of dish-liquid closures |
| Jerrycan TE caps 38 and 50–60 mm (CL-011/012) | INVESTIGATE (low) | Ask blowers. Likely already covered |
| Cosmetic jar lids, jars, hair-gel tubs (CL-014/015/016) | INVESTIGATE later | Not researched. Shelf check first |
| Plain screw caps 24/410, 28/410, 28/400 (CL-007/008) | Range filler only | Commodity |
| Overcaps, plugs, nozzles, roll-on, tube caps, wipes lid, aerosol overcap (CL-013, 017–022, 030) | Park | No buyer evidence |
| Pumps, foam pumps, triggers, fine-mist (CL-023 to 026) | **KILL (phase 1)** | Other process. FOB US$0.04–0.18 |
| Beverage PCO and 38 mm caps (CL-027) | **KILL** | SGT scale |
| Bottles (CL-028/029) | **KILL as product, use as channel** | Blow molding |

---

## 6. Exact questions

### To the shampoo maker (in person; bring a bottle and cap sample home)

1. Which cap exactly? Flip-top, disc-top, push-pull, screw or pump? Can you give us a physical sample and the bottle?
2. Neck finish: 24/410, 28/410, 28/400, or something else? Who blows your bottle, and is the neck their standard or made for you?
3. Annual volume per reference? Lot size per order? How many colours? How many SKUs use this cap?
4. Which local suppliers did you ask (names)? What exactly did each say: "no mould", "mould costs X", "minimum Y pcs", "lead time Z", "can't match colour", or "won't do hinge"?
5. What do you use today? An imported cap (country, supplier, price per 1,000, MOQ, lead time, FX route)? A trader (which one, DZD price)? A different cap you don't like?
6. Any quality problems with current caps: leaks, hinge breaking, lid not staying open or closed, torque, liner?
7. Would you co-fund a mould (US$8–12k) in exchange for a lower price or exclusivity? Or do you only want a stock cap?
8. Target price per cap in DZD, payment terms (cash, cheque, 30/60 days), and how fast you need a first 5k–10k pcs.
9. Do you know other brands with the same problem? (Ask for 3 names.)

### To SIPEM (Oued Smar), posing as a buyer or prospective subcontract client

1. Do you make **hinged flip-top caps** in 24/410 and 28/410? With in-mould closing, or assembled after moulding? Disc-tops? Push-pulls?
2. Stock moulds you own: which neck finishes, how many cavities?
3. MOQ per reference and per colour. Do you colour-match to a sample?
4. Price per 1,000 (DZD, ex-VAT) for a 28/410 flip-top in white, and in a custom colour.
5. Lead time for stock items, and for a new customer mould. Who makes your moulds (in-house, local, China, Turkey)? Typical mould price you quote to clients?
6. Are your "pompettes" (pumps) moulded and assembled in-house, or imported parts?
7. Capacity: number of presses and tonnage. Are you currently full? Would you subcontract overflow?
8. Main customers by segment: cosmetics, detergents, food, pharma.

---

## 7. Gaps and next validation actions

**Gaps**
- No DZD closure prices.
- No current 3923.50 import statistics. The only figure is HS 3923 heading imports from China: US$12.08M in 2017.
- DAPS status on 3923.50.92 is unconfirmed.
- Neck finishes used by Algerian blowers.
- The Cosmetica 2026 exhibitor list has not been obtained (contact Legacy Exhibitions).
- Whether Venus makes its own caps.
- Owners of the Life and Amir Clean brands.

**Next actions, in priority order**
1. Shampoo-maker interview (section 6).
2. SIPEM call.
3. Phone 3 traders for DZD per 1,000 for flip-tops: PAFIX, E.C.A, an Ouedkniss seller.
4. Ask 3 blowers about necks and cap sources: PAP Plast, HM Plast, Soloplast.
5. Supermarket shelf audit: photograph 30 shampoo, dish-liquid and laundry SKUs, noting closure type, neck and "made in" marks.
6. Get a transitaire readout on 3923.50.92 DD and DAPS.
7. Get 2 real Chinese quotes for an 8–12-cavity IMC flip-top mould, with a hinge-life test in the contract.
