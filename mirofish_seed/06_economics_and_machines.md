# Seed 06 — Algeria: cost inputs, machines, molds and unit economics for a one-press (100–120 t) molder (as of 2026-10-04)

**Context.** Sourced cost inputs (energy, labour, finance, FX), machine and mold prices, freight and lead times, followed by the project's cost model, which is entirely assumption-based and is therefore in the assumptions section. Seed document for a multi-agent simulation.

**Evidence tags.** `[VERIFIED date · source]` = figure seen in search-engine snippets of the named source (no page read in full; most price sources are vendor or forwarder marketing). `[STRONG SIGNAL]`, `[WEAK SIGNAL]`, `[UNKNOWN]` as usual; `[ASSUMPTION]` only in the last section. Source notes: feasibility `cost_inputs_market_prices.md` (F-COST), `machines_auxiliaries_landed_cost.md` (F-MACH), `molds_sourcing_shipping.md` (F-MOLD), `regulatory_legal_tax.md` (F-REG); `reports/Algeria injection molding feasibility.md` (report); `model/economics.py`; Phase 2 notes (P2-*). Duties and banking rules are in seed 01; resin prices in seed 03.

---

## 1. Operating cost inputs

| Input | Value | Tag |
|---|---|---|
| Business electricity | 4.680 DZD/kWh (residential 5.650) | [VERIFIED 2025-12 · GlobalPetrolPrices; F-COST §1] |
| Industrial electricity (aggregator) | ≈5.5 DZD/kWh | [VERIFIED 2026-03 · Afrotools; F-COST §1] |
| MT tariff 41 | fixed 38,673.35 DZD/month; power 25.85 DZD/kW/month; energy 1.1615 DZD/kWh | [VERIFIED n.d. · AAPI "coût des facteurs", infoelec.dz; F-MACH §7] |
| MT tariff 44 | fixed 515.65 DZD/month; power 38.70 DZD/kW/month; energy 1.8058 DZD/kWh | [VERIFIED n.d. · same; F-MACH §7] |
| New indirect tax on Sonelgaz bills | from Jan 2025, amount not extracted | [WEAK SIGNAL · Algérie360; F-COST §1] |
| Minimum wage (SNMG) | 24,000 DZD gross/month from 1 Jan 2026 (one guide still quotes 20,000) | [VERIFIED 2026 · Mercans, TSA; F-COST §1] |
| Employer social charges | 24–26% of gross (25% + 0.5% social-works fund most cited); employee 9% | [VERIFIED n.d., sources conflict · Africarrières, Mercans; F-COST §1; F-REG] |
| Public manufacturing operator pay | average net 32,026 DZD/month (ONS year not stated) | [VERIFIED n.d. · Journal du Net; F-COST §1] |
| Mold-setter (régleur) wage | not found | [UNKNOWN · F-COST §1] |
| Workshop rent (any wilaya) | no usable figure; Sétif hangar snippets ambiguous on unit and term | [UNKNOWN · F-COST §1] |
| Packaging, road transport per pallet/km | not found | [UNKNOWN · F-COST §1] |
| Policy rate | 2.50% from 7 Jan 2026 | [VERIFIED 2026-01-07 · BoA Note 01 TEG S1 2026; F-COST §1] |
| Average effective rates, H2 2025 | overdraft 7.51%; short-term 6.87%; medium-term 6.30%; long-term 5.82% | [VERIFIED 2026 · TSA, Le Matin d'Algérie; F-COST §1] |
| Leasing | average effective rate 10.09% (H1 2026) | [VERIFIED 2026-06-29 · Algérie Eco; F-COST §1] |
| SME investment credit (guide) | 5.25–6.25% | [WEAK SIGNAL · ZoomAlgérie; F-COST §1] |
| ANADE micro-project finance | up to 10 M DZD: 70% bank / 25% ANADE interest-free / 5% own funds | [VERIFIED n.d. · UpGrowth; report §7] |
| Official FX | USD 133.2 DZD (26 Jul 2026); EUR 154.9 DZD (31 Aug 2026) | [VERIFIED 2026 · Algérie360, ObservAlgérie; F-COST §1] |
| Parallel FX | USD ≈240 DZD (11 Jul 2026); EUR 274–282 DZD (Feb–Sep 2026) | [VERIFIED 2026 · Algérie360, ObservAlgérie; F-COST §1] |

## 2. Machines

- New Haitian MA1200/370 servo (120 t): USD 14,200 (1–2 sets), USD 13,700 (3+) FOB; MA1200/370G USD 14,700–15,000. [VERIFIED 2025–26 · Alibaba, noble-machine listings; F-MACH §2]
- A "2026 second-generation" MA1200 at USD 9,000–9,500 is probably refurbished. [WEAK SIGNAL · made-in-china listing; F-MACH §2]
- Used Haitian MA1200 ex-China: USD 7,300–8,300 with 1-year core-parts warranty; others USD 9,999–13,800. Used Borche BS120 (2018) €22,500 in Europe. Import of used presses is restricted to ≤5 years old (seed 01). [VERIFIED n.d. · usedhaitian.com, geerpower, resale.info; F-MACH §2]
- New 30–100 t Chinese machines cost about USD 10,000–30,000. [VERIFIED 2025 · Daoben price guide (vendor); F-COST §2]
- Haitian Mars III tie-bar spacing: MA900III 360×360 mm; MA1200III 410×410 mm; MA1600III 470×470 mm; PS shot weights 188–395 g across these models depending on screw. MA1200II: 1,200 kN, 360 mm opening stroke. [VERIFIED n.d. · Scribd Haitian Mars III/II spec sheets; F-MACH §1]
- Full datasheets for Haitian, Yizumi, LK, Borche, Chen Hsong, Tederic were not read. [UNKNOWN · F-MACH §1]
- Ouedkniss machine listings: HWAMDA 400 t "360", FOHONG 140 t servo "400", "LOG" machine 5,000,000 DZD (unit of "360/400" not stated). [WEAK SIGNAL · F-MACH §2]
- Distributor price lists (AFC/Yizumi, 2M Expert/Cosmos) were not obtained. [UNKNOWN · F-MACH §4]
- Auxiliaries (China listings): hopper dryers USD 150–2,000 (sets 300–1,200); dehumidifying 3-in-1 dryers USD 5,000–10,000; chillers USD 998–26,000, mid-range air-cooled 1,300–8,900. [VERIFIED 2025 · made-in-china/Alibaba; F-MACH §6]
- Sea freight 40 ft Shanghai→Algiers USD 2,900–5,100 (China→Algeria 2,700–5,600); CMA CGM FAK to Algeria from 15 Jun 2026 USD 9,200 + 1,800 PSS; China–Med index ≈USD 4,388/FEU (May 2026). Transit 38–45 days. [VERIFIED 2026 · Dantful, docshipper, tidesignalnews; F-MACH §4]
- Duty is computed on CIF value; VAT 19% on CIF plus duty. [VERIFIED n.d. · FreightAmigo, trade.gov; F-MACH §4]

## 3. Molds

- China: prototype single-cavity USD 1,000–3,000; production multi-cavity USD 5,000–15,000+; Chinese prices 30–60% below EU/NA; T1 lead time 25–45 working days (simple designs ~2 weeks). [VERIFIED 2026-10-03 · Haizol 2026, RapidDirect (vendor blogs); F-MOLD §1]
- Steel premiums over P20: 718H +15–25%, S136 +40–60%; P20/718H for 100k–500k shots. A 4-cavity mold costs 150–200% more than a 1-cavity base; hot runner adds USD 3,000–15,000; a "medium" mold base is USD 8,000–25,000. [VERIFIED 2026-10-03 · Boxu Mold blog; F-MOLD §1]
- Cap-mold listings: 6-cavity cold runner USD 800–8,000; 8-cavity PET cap USD 2,000–5,000; typical lead 40–45 days. Flip-top molds: 8-cavity from ≈USD 2,000, 16-cavity USD 8,000–15,000, cycle 10–18 s; industrial incumbents run 40–50+ cavities with in-mold closing. [WEAK SIGNAL · made-in-china listings (placeholders, not quotes); F-MOLD §1; P2-CL §3]
- SPI classes: 101 >1M cycles (cavity ≥48 HRC); 102 500k–1M; 103 <500k (≥28 HRC); 104 <100k; 105 <500. [VERIFIED n.d. · Texas Injection Molding, Plastikon; F-MOLD §2]
- Mill test reports cost about USD 200–500 per steel order. Third-party inspection (V-Trust): USD 268/man-day inspection, USD 398/man-day factory audit. [VERIFIED 2026-10-03 · Boxu, V-Trust; F-MOLD §2, §4]
- Payment norms: deposit ≤30–50% with ≥30% held until T1 approval; common split 50/40/10. [VERIFIED 2026-10-03 · RJC Mold, NewBuyingAgent; F-MOLD §3]
- Moldflow USD 2,000–5,000 (5–15 days); DFM USD 500–2,000 or free, catching 60–80% of issues. [VERIFIED 2026-10-03 · Boxu, RJC Mold; F-MOLD §6]
- Mold freight China→Algiers: air USD 4.20–7.00/kg (9–11 days), one quote USD 7.90/kg for 1,000 kg+ (Apr 2026); LCL USD 90–210/CBM base, 38–45 days + 3–7 days handling. [VERIFIED 2026 · Sino-Shipping, DocShipper, Dantful; F-MOLD §5]
- Turkish mold makers exist (B-PLAS, Polymetal, Sema, Eramold, ATA, PQMold, Plaspar) but no public prices were found; no Algerian mold prices were found; SIPLAST quotes a 6-week mold lead time. [VERIFIED (names) / UNKNOWN (prices) · F-MOLD §1; seed 02]

## 4. Conversion-rate benchmarks

- An old North-American survey of 47 molders gave USD 9.07–35/h for 25–100 t presses. [VERIFIED n.d. · PlasticsToday; F-COST §2]
- Labour: China USD 3–8/h, USA 25–50/h, Europe 30–60/h. [WEAK SIGNAL · Rayleap (vendor); F-COST §2]
- No Algerian machine-hour or subcontract rate was found. [UNKNOWN · F-COST §2]

---

## Assumptions (not facts)

**Machine and landed cost**
- One 120 t new servo press at USD 14k FOB lands at ≈USD 23–30k all-in without exemptions, ≈19–25k with AAPI; an Algerian distributor quote is ≈15–35% above direct landed (≈USD 27–38k) but includes commissioning, warranty and parts; a used local 120–150 t press sells for ≈2.5–5 M DZD (≈USD 19–37k). [ASSUMPTION · F-MACH §4; report §4.3]
- Day-1 auxiliaries (chiller rated for 43 °C, loader, hopper dryer, granulator, mixer, softener, QC tools, pallet truck, spares) ≈USD 6–12k FOB; no dehumidifying dryer needed for PP/HDPE. Plan 60–80 kVA, 3-phase 400 V/50 Hz; a new MT post costs several million DZD and months. [ASSUMPTION · F-MACH §6–7; report §4.6]
- Practical PP shot on a 120 t press 45–200 g (30–80% of PS-rated shot × 0.85–0.9); mold width limited by 410 mm tie-bars; clamp ≈ projected area × cavities × 1.15 × factor × 1.2. For many tiny parts the binding constraint is minimum shot, not clamp. [ASSUMPTION · F-MACH §1; data/OPPORTUNITY_SCHEMA.md; P2-JC §4]
- Servo energy ≈0.4–0.6 kWh/kg vs 0.8–1.2 for fixed pump; energy ≈1–2 DZD/kg of PP, negligible against resin. [ASSUMPTION · F-MACH §1, §7]
- European presses (Engel, Arburg) cost €60–150k+ for 100 t. [ASSUMPTION · F-MACH §2]

**Molds**
- Chinese molds for small parts: 2-cavity box USD 4–9k; 4-cavity cap USD 5–12k (+3–6k hot runner); 8-cavity clip USD 4–10k; 4-cavity PA66 cable tie USD 8–20k; first-product molds budgeted USD 4–10k each; landed ≈1.2–1.25× FOB. [ASSUMPTION · F-MOLD §1; report §15; model/economics.py]
- Turkish molds ≈1.3–2× China with ≈1 week Ro-Ro transit. [ASSUMPTION · F-MOLD §1]
- Air freight for a mold pays off when ~30–35 days saved × daily contribution exceeds the USD 1–3k air premium. [ASSUMPTION · F-MOLD §6]
- Recommended export-mold payment: 30% deposit / 30% at T1 / 40% after final approval and inspection; typical simple molds need 2–3 trial rounds of 1–2 weeks each. [ASSUMPTION · F-MOLD §3, §6]

**Own-press cost model (report §8, model/economics.py)**
- Fixed costs, own 120 t cell, 2 shifts (DZD/month): depreciation 55k (USD 35k over 7 years); labour 173k (2 operators at 36k gross + 1 régleur at 65k gross, ×1.26); rent 120k; admin 60k; interest 12k (50% debt at 6.3%); maintenance 19k; electricity ≈31k (18 kW average × 5 DZD/kWh) → ≈470k; with founder and overhead 120k → ≈595k. [ASSUMPTION · report §8.2, §15.9]
- Productive hours: 2 shifts × 8 h × 25 days × 85% OEE ≈340 h/month. Machine-hour rate ≈1,383 DZD/h (≈USD 10.4) at full 2-shift use; ≈2,670 DZD/h at 50% utilisation; ≈2,410 DZD/h on one shift. [ASSUMPTION · report §8.2]
- Phase 2 opportunity files used other press-hour rates: 700 DZD/h (closures), 1,400 DZD/h (irrigation/furniture), 2,000 DZD/h (joinery/other sectors). [ASSUMPTION · P2-CL; P2-IF §5; P2-JC; P2-OS]
- Unit cost = material + conversion + mold amortisation + packaging/transport (3% + 3%) + selling (5%); resin 220 DZD/kg + masterbatch 600 DZD/kg at 2%; 3% loss + 3% reject; molds amortised over 2 years of planned volume. [ASSUMPTION · report §8.2]
- Worked unit costs at full utilisation: 5 g packer 8-cav/18 s ≈2.73 DZD; 10 g spacer 8-cav/20 s ≈4.46 DZD; 20 g chair spacer ≈9.33 DZD; 50 g small box ≈25.03 DZD (vs 40 DZD retail for a 100×100 box: no room); 100 g cover ≈52.15 DZD. [ASSUMPTION · report §8.3]
- Contribution per machine-hour: spacers ≈5,100 DZD/h, glazing packers ≈8,300, drip fittings ≈11,300 at assumed wholesale prices of 8 / 3.5 / 12 DZD. Own-press break-even ≈48–107 machine-h/month (≈0.7–1.04 M DZD revenue/month). [ASSUMPTION · report §8.3, §15.10]
- Utilisation matters ≈4× more than resin price for small parts: +10% resin adds ≈0.24 DZD to a 10 g part; 50% instead of 100% utilisation adds ≈1 DZD. [ASSUMPTION · report §8.3]

**Subcontract vs own press**
- Subcontract rate 2,000 / 3,000 / 4,000 DZD/h → buy-vs-subcontract break-even ≈227 / 147 / 109 h/month on 2 shifts. Rule used by the project: buy the press when signed recurring orders exceed ≈150 machine-hours/month; subcontract for 6–9 months first. [ASSUMPTION · report §6.3, §15.7]
- Under subcontract (3,000 DZD/h, resin 264 DZD/kg): spacers ≈18% margin, packers ≈42%, drip fittings ≈56% after 10% selling costs. [ASSUMPTION · report §6.3]

**Capital and first-year model**
- Budget scenarios: USD 5k validation only; USD 10–25k subcontract with 1–2 families (recommended start ≈USD 20k); USD 50k minimum viable one-press factory. [ASSUMPTION · report §7]
- Year-1 model (subcontract months 4–9, press producing from month 10; spacers 8, packers 3.5, drip 12 DZD; collections 50% cash / 50% at 60 days): revenue ≈16.6 M DZD, EBITDA ≈4.2 M DZD, peak cash need ≈6.2 M DZD (≈USD 46k) in Q3, press utilisation ≈66% in month 12. Prices −30% and volume −50% together make the press lose money. [ASSUMPTION · report §15.20]
- Closure cost model: landed import = FOB × 237 DZD/USD (official) or × 428 (parallel); press 700 DZD/h, OEE 75%. [ASSUMPTION · P2-CL]
- model/economics.py stress grid: resin 220/300/400 DZD/kg × utilisation 50/70/90% × credit 30/60/90 days at 8% annual cost of credit; "KILL" if margin <0 at resin 400 and 50% utilisation, "FRAGILE" if <15%. [ASSUMPTION · model/economics.py]
