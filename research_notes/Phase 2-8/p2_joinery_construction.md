# Phase 2: Joinery (aluminium/PVC) and construction plastic components — product gap discovery

Research date: 2026-10-04. Data files:
- `/home/user/ghanoubenz/data/phase2_joinery_construction_opportunities.csv`: 40 candidates, JC-01 to JC-40. Clamp, shot, unit cost, potential price and margin are computed in every injection row. The formula is written out in `stage_notes`.
- `/home/user/ghanoubenz/data/phase2_joinery_construction_signals.csv`: 23 signals.

**Method caveat (read first).**
- I ran about 46 web searches. WebFetch was blocked by the egress proxy for every target I tried: assly.dz, conformepro.dz and alibaba.com. Phase 1 had already found ouedkniss.com, mabricole and algerie-eco blocked.
- Every Algerian fact below therefore comes from a **search-engine snippet** attributed to the URL shown. I could not open listing pages to confirm dates, pack sizes or brands.
- Facebook pages of accessory sellers were not reachable at all.
- I invented no buyer, price, shortage or contact. Anything I could not source is written UNKNOWN.
- Engineering numbers (part weight, projected area, cycle time, mould cost) are my ASSUMPTIONS for typical geometries. They must be replaced with real samples.

Economic assumptions used in the CSV, all ASSUMPTION:
- **Resin (DZD/kg):** PP 300, HDPE 290, recycled PP/HDPE 180, PA6 700, POM 750, ABS 550, ASA 650, TPE 600. The PP figure is the middle of the 220–350 DZD/kg estimate in `resin_materials.md`.
- **Conversion cost:** machine-hour all-in 2,000 DZD/h at 80% OEE, plus 5% for packaging.
- **Unit cost excludes mould amortisation.** Mould payback in parts is given separately.
- **Import floor:** FOB × 133 DZD/USD × 1.10 freight × 1.30 customs duty (DD). DAPS is excluded because its status for these lines is unknown. VAT is ignored because it is recoverable in B2B.
- **"Potential price":**
  - where a Chinese FOB price exists: landed floor × 1.15;
  - where an Algerian retail price exists: 50% of that retail price, assuming the distributor and retailer together take about 50%.

---

## 1. Who buys these parts, and through which channels?

### Takeaway
- **Joinery.** The buyers are two large PVC window plants (Oxxo/Cevital and Izdihar PVC), at least one named aluminium extruder (SPA Profilés Aluminium du Maghreb, Aïn Defla), and a large number of small aluminium/PVC workshops. The workshops are served by accessory distributors clustered in **Hammedi (Boumerdès)**, of which Leader Aluminium is the named example.
- **Construction.** Consumables reach contractors through quincaillerie e-shops and wholesalers: assly.dz, mabricole.com.dz and Jumia sellers. The two named precast buyers are Cosider Canalisations and Trans-Canal Algeria.
- **No El Eulma wholesaler, formwork contractor or double-glazing (IGU) maker could be named** from desk sources.

### Cited Findings
- **Leader Aluminium (Hammedi, Boumerdès)** distributes door and window opening systems. Its range covers aluminium accessories, PVC caissons, aluminium profiles, EPDM seals and roller-shutter motors. A Hammedi store search returns 29 aluminium-accessory products. — [Ouedkniss store](https://www.ouedkniss.com/store/14372/leader-aluminium/accueil?lang=fr); [Ouedkniss accessoires aluminium category](https://www.ouedkniss.com/accessoires-aluminium_materiaux_equipement-r?lang=fr)
- Phase 1 snippet: the brands "Dubral" and "Alupha" appear at Leader Aluminium. Their origin is unknown. — [Ouedkniss store](https://www.ouedkniss.com/store/14372/leader-aluminium/accueil?lang=fr) (prior notes)
- **Oxxo (Cevital)**, Aïn Taghrout (BBA): 2.1M windows/yr on a 35 ha robotised site; Oxxo Algérie has been on the market since 2014. — [Cevital](https://www.cevital.com/oxxo-increased-its-production-capacity-of-profiles-for-the-window-plant/); [Algérie Eco](https://algerie-eco.com/?p=23714)
- **Izdihar PVC**, Zaaroura (Tiaret): 117,000 units/yr, with a claimed 85% local integration. A metallic quincaillerie factory opened in the same zone. — [Algérie360](https://www.algerie360.com/pvc-lalgerie-mise-sur-2-nouvelles-usines-pour-passer-de-limport-a-lexport/)
- **SPA Profilés Aluminium du Maghreb** (Aïn Defla) manufactures and surface-treats aluminium-alloy building profiles, and exported 130 t to Tunisia. — [Algérie Eco](https://algerie-eco.com/?p=201288)
- **"Alumetal" could not be verified** as an Algerian extruder, and nor could "Algal". D&B counts 12 aluminium production and processing firms in M'sila, but the snippet does not name them. — [D&B M'sila](https://www.dnb.com/business-directory/company-information.alumina_and_aluminum_production_and_processing.dz.wilaya_de_m_sila.html)
- **Turkish PVC profile houses** present in Algeria: Wintech exports to Algeria, and Yapıpen (Penhouse/Baywin) makes window and shutter profiles. So accessories must also match Turkish series. — [Yapıpen](https://bp.b2brazil.com/hotsite/yapipengroup); [TIM delegation PDF](https://delegations.tim.org.tr/storage/uploads/company/75291/EPVXwLEeFBtvdo3sCQg9GTk33B0qWGSu106250hf.pdf)
- **Master Italy** (Italian accessories) exhibited at Batimatec 2019 and says it has distributed in North Africa for more than 20 years. — [Master Italy PR](https://www.masteritaly.com/wp-content/uploads/2019/03/Communiqué-de-presse_FR_Batimatec.pdf)
- **Batimatec 2026** (3–7 May) had exhibitors from 15 countries, including China, Turkey, Italy, Spain and Portugal. Its hardware category covers door/window accessories and aluminium profiles. — [Dzair Tube](https://www.dzair-tube.dz/en/batimatec-2026-to-convene-global-industry-leaders-in-algiers-with-participation-from-15-countries/); [Jufair](https://en.jufair.com/exhibition/batimatec/periodical/)
- **Construction e-shops:**
  - assly.dz lists cales à béton, croisillons and colliers. — [assly cale à béton](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/cale-a-beton/)
  - mabricole.com.dz and a Jumia seller list tile-levelling kits. — [mabricole](https://mabricole.com.dz/autre-outils/systeme-de-nivellement-de-faience-et-carrelage-kit-nivelleur-2mm-100-pcs-3457); [Jumia](https://www.jumia.dz/kit-systeme-nivellement-calle-consomable-pince-jaune-sans-marque-mpg12403.html)
- **Precast plants:**
  - Cosider Canalisations: precast boundary-wall line and double-T slab moulds. — [CPI](https://cpi-worldwide.com/journals/artikel/64708)
  - Trans-Canal Algeria: automated concrete-pipe plant. — [CPI](https://cpi-worldwide.com/journals/artikel/46313)
- **Small joinery workshops** advertise on Ouedkniss in Reghaïa, El Madania, Guelma and Azazga. These are generic service listings and are unnamed in the snippets. — [Ouedkniss Reghaïa](https://www.ouedkniss.com/menuiserie-aluminium-et-pvc-algiers-reghaia-services-d16667767?lang=en); [Ouedkniss Guelma](https://www.ouedkniss.com/guelma-algerie-menuiserie-meubles-bois-aluminium-et-pvc-d24164167?lang=fr)

### Inferences
- The fastest route to joinery buyers is **one field day in Hammedi**, covering Leader Aluminium and its neighbours. Phone calls to Oxxo and Izdihar purchasing should follow.
- Izdihar's claimed 85% integration means a local-content KPI exists. Asking what the remaining 15% is gives a concrete door-opener.
- Profiles in the market come from Oxxo, from Turkish houses and from local aluminium extruders, so system-specific accessories (stops, caps, corner keys) split into many SKUs. Universal consumables (packers, drainage caps, fly-screen corners) avoid this.

### Gaps
- No El Eulma or East Algiers quincaillerie wholesaler could be named; the search returned only foreign results.
- No Algerian roller-shutter assembler, formwork contractor or rental firm, IGU/double-glazing maker, or ETICS contractor was found.
- The Batimatec 2026 exhibitor list was not retrievable.
- The Izdihar sister hardware plant was not named.

---

## 2. Is there evidence of sourcing pain (shortage, MOQ, delay, custom size, quality, colour, cash tied in imports)?

### Takeaway
**No.** French, Arabic and English searches found no Algerian text in which a named buyer reports a shortage, MOQ problem, import delay, quality failure or colour problem for any product in scope. The only pain-adjacent signal is generic: quincaillerie owners report shortages after import bans, but for taps and copper goods, not for these parts. Every `pain_type` in the CSV is therefore `none_found`. Pain remains a hypothesis to be tested by interview.

### Cited Findings
- A hardware-store owner says import bans caused shortages and price rises: copper goods were scarce and taps "introuvable". This is not joinery or construction plastics. — [Maghreb Emergent](https://maghrebemergent.news/fr/algerie-baisse-des-importations-la-penurie-s-installe/)
- Phase 1 found raw materials for aluminium joinery taxed more heavily than imported finished products. — [Algérie Eco tag](https://algerie-eco.com/tag/menuiserie/) (prior notes)
- When 851 products were suspended (about 2018), finished aluminium joinery was pulled from the list while PVC joinery stayed suspended. — [Algérie Eco](https://algerie-eco.com/?p=25944)
- Arabic queries ("إكسسوارات الألمنيوم الجزائر", "مباعد حديد التسليح بلاستيك الجزائر", "لوازم الألمنيوم والبي في سي واد كنيس") returned only customs-tariff pages, Egyptian firms or steel news. They surfaced no Algerian buyer content. — e.g. [conformepro](https://conformepro.dz/ar/resources/tarif-douanier/sous-position/76.09.009100/autres-filetes)

### Inferences
- The **structural** case for pain is plausible but unproven:
  - (a) Accessories are imported in many small SKUs, so distributors carry cash in slow stock.
  - (b) Colour-matched caps for local profile colours may be hard to get in small lots.
  - (c) The PPI import-forecast regime (see `policy_regulatory.md`) adds friction for small importers.
  None of these is evidenced for our parts.
- Construction consumables (spacers, tile clips) show **no sign of scarcity**: several e-shops list them in stock with prices. The opportunity there is **margin capture**, because retail sits far above the landed import floor. It is not about relieving a shortage.

### Gaps
- Interview questions to answer the pain gap: stock-outs in the last 12 months, MOQ imposed by the importer, lead time, colours unavailable, custom rebate widths, and the cash cycle on imported accessories. Ask them at Leader Aluminium, 3–5 Hammedi shops, Oxxo and Izdihar purchasing, 3 quincaillerie wholesalers, and Cosider/Trans-Canal.

---

## 3. Price ladder: Chinese import floor versus Algerian shelf price

### Takeaway
- **Construction consumables have a large gap between landed import cost and Algerian retail.**
  - Rebar spacers: 5.6–22.5 DA/pc retail against about 2–10 DA landed.
  - Tile-levelling clips: 7.8 DA/pc retail against about 1–2 DA landed.
- **Joinery accessories have no Algerian price at all.** Only FOB benchmarks were found: packers $0.015–0.045, formwork cones $0.02–0.30, shutter caps $0.40–4.5. Joinery economics therefore rest on the import floor, not on observed local prices.

### Cited Findings

| Product | Algerian price (snippet) | Chinese FOB (snippet) | Landed floor DZD/pc (my calc: FOB × 190.2) |
|---|---|---|---|
| Rebar spacer, round 30/8-14 | 13,600 DA / 1,000 = **13.6 DA/pc** ([assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/cale-a-beton/)) | $0.01–0.15/pc; 10k+ orders $0.01–0.015 ([alibaba](https://www.alibaba.com/showroom/concrete-spacer.html)) | 1.9–28.5 (basic: 1.9–9.5) |
| Rebar spacer, vertical 25/6-12 | 840 DA / 150 = **5.6 DA/pc** (another snippet says the bag is 1,000 pcs) ([assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/cale-a-beton/)) | as above | as above |
| Rebar spacer, horizontal 40-8/24 and 50-8/24 | 13,500 DA / 600 = **22.5**; 10,600 / 500 = **21.2 DA/pc** ([assly](https://www.assly.dz/product/cale-d-armature-plastique-horizontale-40-8-24-sac-600pcs-ref-3040/)) | heavy chairs $0.19–1.59 | — |
| Tile-levelling clips 2 mm | kit of 100 = 780 DA (**7.8 DA/pc**); kit with pliers 4,890 DA ([mabricole](https://mabricole.com.dz/autre-outils/systeme-de-nivellement-de-faience-et-carrelage-kit-nivelleur-2mm-100-pcs-3457); [Jumia](https://www.jumia.dz/kit-systeme-nivellement-calle-consomable-pince-jaune-sans-marque-mpg12403.html)) | $0.55–1.10 per bag of 100; $0.60–0.65 at MOQ 1,000 bags ([made-in-china](https://ykhaomai.en.made-in-china.com/product/AdhfRrCbstGp/China-Plastic-Tile-Leveling-System-Clips-and-Wedges-Ceramic-Tile-Leveling-Install-Tools-Tile-Leveling-System-Spacer.html)) | 1.05–2.09 |
| Reusable levelling wedges | 100 pcs 680 DA or 1,100 DA (**6.8–11 DA/pc**) ([mabricole](https://mabricole.com.dz/fr/autre-outils/cales-reutilisables-en-plastique-100-pcs-pour-systeme-de-nivellement-de-faience-et-carrelage-3458)) | UNKNOWN | — |
| Tile crosses 2.5 mm | 200 pcs 100 DA (**0.5 DA/pc**) ([assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/croisillon-faience/)) | bag $0.20–0.35, pack size unknown (prior notes) | — |
| Pipe clip "collier atlas d.12" | 100 pcs 1,021 DA (**10.2 DA/pc**; the item type is uncertain) ([assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/les-collier/collier-de-serrage/)) | UNKNOWN | — |
| Glazing packers (flat / U-shaped) | **UNKNOWN** | $0.016–0.045 (MOQ 5k); U-shape $0.0223 / $0.0193 / $0.0153 at 1k / 5k / 10k+ ([alibaba](https://www.alibaba.com/showroom/plastic-frame-packers.html); [made-in-china](https://dgelehk.en.made-in-china.com/product/yaCYDVvHbrWx/China-Elehk-Glazing-Packers-Window-Flooring-Glass-Glazing-Packer-Shims-Spacers-Flat-Plastic-Frame-Flat-Glazing-Packer.html)) | 2.9–8.6 |
| Formwork cone (tie rod) | **UNKNOWN** | $0.02 (MOQ 10k); $0.05 (MOQ 1k); $0.15–0.30 (MOQ 1k); reusable $0.20–0.30 ([alibaba](https://www.alibaba.com/showroom/plastic-tie-rod-cone.html)) | 3.8–57 |
| Roller-shutter end caps | **UNKNOWN** | $0.40–1.00 and $1.50 (MOQ 100); 70 mm $2–4.5; PA66 from $2.88 (MOQ 20). Mostly box or axle caps ([made-in-china](https://www.made-in-china.com/products-search/hot-china-products/Roller_Shutter_End_Cap.html)) | 76–856 |
| Slat end cap set (US retail, reference only) | — | $0.28 Alugix-55 set ([steelandpipes](https://store.steelandpipes.com/products/alugix-55-slat-end-cap-set)) | — |

- **Customs:**
  - 3926.90.99.90 ("other plastic articles") carries **30% customs duty**. The snippet does not state DAPS. — [conformepro](https://conformepro.dz/resources/tarif-douanier/sous-position/39.26.909990/مصنعات-أخرى-من-اللدائن-البلاستيك)
  - A neighbouring Chapter 39 line, 3926.20.12 (plastic gloves), carries **DD 30% + DAPS 60% + TVA 19% + TCS 3%**. So DAPS does apply to some Chapter 39 articles. — [conformepro](https://conformepro.dz/resources/tarif-douanier/sous-position/39.26.201200/قفازات-بلاستيكية-للاستخدام-المتعدد)
  - Lines 3925.20 (doors/windows), 3925.30 (shutters and parts) and 3925.90 (other building articles) exist in the HS. — [WCO](https://www.wcotradetools.org/en/harmonized-system/2012/fr/07392520)
  - The Algerian DD/DAPS rates for the 3925 lines were **not retrieved**, because conformepro was blocked to fetch.

### Inferences
- If DAPS (e.g. 60%) applies to a line, the import floor rises by 60% and every margin in the CSV improves. This is the most valuable single desk check left: open conformepro for 3925.30, 3925.90 and 3926.90 in a normal browser.
- Retail prices for spacers and tile clips sit 3–7× above the landed floor. The local molder's competitor is therefore the **importer's and distributor's margin**, not the Chinese factory. Selling direct to wholesalers at about 50% of retail still leaves 50–70% gross margin over variable cost (see the CSV).

### Gaps
- Wholesale (not retail) DZD per 1,000 for every item.
- Any Algerian price for packers, shutter parts, drainage caps, fly-screen corners, formwork cones and plugs, or drywall anchors.
- DAPS by line for 3925.xx and 3926.90.

---

## 4. Technical fit on a 100–120 t servo press and unit economics

### Takeaway
- **31 of the 36 injection candidates fit 120 t confidently.** The exceptions:
  - Borderline because the shot is under the 45 g practical minimum, or near the clamp limit: JC-01 flat packers, JC-23, JC-37 and JC-38.
  - Too large: roller-shutter box cheeks (JC-06) need about 207 t.
- **Four items are not injection at all** and are KILLed: EPDM gaskets, shutter slats, linear spacers and PVC spacer tubes.
- **Economics are positive** wherever a price anchor exists, with gross margin before mould of 50–80%. There are three exceptions:
  - reusable tile wedges are negative at 50% of the lowest retail;
  - tile crosses earn only about 0.1 DA/pc;
  - high chairs earn about 26%.

### Cited Findings
- Machine-fit rules and reference presses: [OPPORTUNITY_SCHEMA.md](/home/user/ghanoubenz/data/OPPORTUNITY_SCHEMA.md).
- Mould price ranges (8-cavity small clip US$4k–10k, Chinese multi-cavity US$5k–15k+): [molds_sourcing_shipping.md](/home/user/ghanoubenz/research_notes/Algeria%20injection%20molding%20feasibility/molds_sourcing_shipping.md), which cites [Haizol](https://www.haizol.com/news/china-injection-molding-industry-report-2026) and [Boxu Mold](https://www.boxumold.com/blog/plastic-mold-pricing-guide).
- Resin estimate of 220–350 DZD/kg: [resin_materials.md](/home/user/ghanoubenz/research_notes/Phase%201%20Algeria%20reality%20map/resin_materials.md).

### Inferences
Selected computed rows (full detail in the CSV):

| ID | Part | Cavities | Shot g | Clamp t | Fit | Unit cost DZD | Potential DZD | Margin |
|---|---|---|---|---|---|---|---|---|
| JC-26 | Horizontal spacer chair 40-8/24 | 6 | 82.8 | 54.6 | Fits | 5.25 | 11.0 | 52% |
| JC-24 | Rebar wheel 30 mm | 8 | 67.2 | 92.7 | Fits | 3.37 | 6.8 | 50% |
| JC-34 | Tile-levelling clip | 16 | 60.0 | 33.1 | Fits | 1.61 | 3.9 | 59% |
| JC-30 | Formwork cone | 12 | 86.4 | 39.7 | Fits | 3.04 | 17.5 (FOB-based, wide range) | 83% |
| JC-01 | Flat glazing packer | 8 | 40.0 | 86.1 | Borderline (low shot) | 2.76 | 6.6 | 58% |
| JC-03 | U-shaped frame packer | 12 | 45.0 | 89.4 | Fits | 1.88 | 4.4 | 57% |
| JC-13 | Drainage slot cover | 32 | 62.4 | 46.4 | Fits | 0.81 | UNKNOWN | — |
| JC-06 | Shutter box cheek | 2 | 154 | 207 | Requires larger | 62 | 328 | — |

- Several parts are tiny (packers, caps, clips), so the **binding constraint is the minimum shot, not the clamp**. Specify the press with the smaller screw option (Ø30–35 mm), or design moulds with enough cavities to reach 45 g or more.
- The mould is the main investment per family: about US$7k–12k, paid back in roughly 200k–1M parts at official FX. In the spacer and tile-clip families, one base mould with interchangeable inserts covers the variants.

### Gaps
- Part weights, projected areas and cycle times are estimates. Weigh real samples bought in Hammedi and on assly/mabricole.
- The machine-hour rate (2,000 DZD/h) is not validated by any local quote.

---

## 5. Verdict per product family: GO / INVESTIGATE / KILL

### Takeaway
- **GO, subject to an interview gate:**
  - rebar spacers (JC-24/25/26 first; JC-40 later);
  - tile-levelling clips (JC-34);
  - universal joinery consumables: glazing and frame packers (JC-01/03), drainage covers (JC-13), fly-screen corners and clips (JC-16/17).
- **INVESTIGATE:**
  - formwork cones and plugs (JC-30/31);
  - roller-shutter small parts kit (JC-04/05/07/08/10/11);
  - PVC window cover caps for the Oxxo/Izdihar integration push (JC-19);
  - IGU corner keys (JC-20);
  - profile end caps (JC-12);
  - precast custom spacers and recess formers (JC-29/39);
  - pipe clips (JC-36);
  - high chairs (JC-27), sliding stops (JC-15), bridge packers (JC-02), insulation fixings (JC-38).
- **KILL:** extrusion items (JC-21/22/28/32), shutter box cheeks (JC-06), sliding wheels (JC-14), alignment corner keys (JC-18), tile crosses (JC-33), drywall self-drill anchors (JC-37), strap guides (JC-09), brush end plugs (JC-23), and stand-alone reusable wedges (JC-35).

### Cited Findings
- Spacer and tile-clip price anchors: Section 3 ([assly](https://www.assly.dz/product-category/fixation-mecanique-boulonerie/chevilles-et-cales/cale-a-beton/); [mabricole](https://mabricole.com.dz/autre-outils/systeme-de-nivellement-de-faience-et-carrelage-kit-nivelleur-2mm-100-pcs-3457)).
- Branded Italian incumbents for technical hardware: [Master Italy](https://www.masteritaly.com/wp-content/uploads/2019/03/Communiqué-de-presse_FR_Batimatec.pdf).
- Integration push at Izdihar: [Algérie360](https://www.algerie360.com/pvc-lalgerie-mise-sur-2-nouvelles-usines-pour-passer-de-limport-a-lexport/).

### Inferences
| Family | Verdict | Reason / kill reason |
|---|---|---|
| Rebar spacers (wheel, vertical, horizontal chair) | **GO** (gate: 3 wholesaler calls) | Strongest local price anchors (5.6–22.5 DA/pc). Bulky, so freight protects local supply. Recycled PP is acceptable. Simple 6–12 cavity tools well inside 120 t. No pain evidence, so the angle is margin and availability, not shortage. |
| Tile-levelling clips (+ wedges as kit) | **GO** (gate: 3 tile-shop calls) | 7.8 DA/clip retail against about 1–2 DA landed. Simple 16-cavity tool. Quality risk is the break-off neck. Wedges alone are KILL (negative margin at 6.8 DA retail) and are sold only in a kit. |
| Glazing and frame packers | **GO-candidate** (gate: Hammedi visit) | Universal across alu and PVC systems; FOB $0.015–0.045. No Algerian price was found, so this needs a field price. The flat packer shot is low: use the small screw or 10 cavities. |
| Drainage covers, fly-screen corners and clips | **GO-candidate** | Cheap 24–32 cavity tools. Selling angle is colour and seasonal availability, which is a hypothesis. No price found. |
| Formwork cones and tie plugs | **INVESTIGATE** | FOB spread $0.02–0.30 is too wide. Need to know which tie system Algerian contractors use, and whether plugs are used at all. |
| Roller-shutter small parts | **INVESTIGATE** | Fragmented across slat profiles (37/39/42/55 mm), so tooling only makes sense once 2–3 dominant profiles are known. Motorisation is rising (many motor listings on Ouedkniss). |
| PVC window caps (hinge/screw covers) | **INVESTIGATE** | Concentrated buyers (Oxxo, Izdihar) on a local-integration agenda. But the parts are specific to the hardware brand. |
| IGU spacer corner keys | **INVESTIGATE** | New buyer group (glass processors) that has not been mapped yet. |
| Profile end caps / sliding stops | **INVESTIGATE** | Series-specific. Overlaps with the furniture tube-cap family. |
| Precast custom spacers / recess formers | **INVESTIGATE** | Only worth pursuing if Cosider or Trans-Canal confirm a need. |
| Pipe clips | **INVESTIGATE** | 10.2 DA/pc anchor, but the item identity is uncertain and local electrical molders may already supply. Coordinate with the electrical researcher. |
| Shutter box cheeks | **KILL** | Needs about 207 t (2-cavity ASA, about 150 cm² each); many cheeks are aluminium anyway. |
| Sliding wheels, structural corner keys | **KILL** | Technical, brand-led (Master Italy and others), need bearing/metal assembly or system approval. |
| Tile crosses | **KILL** | 0.5 DA/pc retail; absolute margin about 0.1 DA; a 128-cavity tool needs more than 10M parts to pay back. |
| Drywall self-drilling anchors | **KILL** (for start) | Unscrewing mould, PA drying, pull-out testing; no demand evidence. |
| EPDM gaskets, shutter slats, linear spacers, PVC spacer tubes | **KILL** | Extrusion, not injection. |

**Next validation actions, in priority order:**
1. Spend one day in Hammedi: Leader Aluminium plus 4 neighbouring shops. Buy samples of packers, drainage caps, fly-screen corners and shutter caps. Record origin, DZD per 100/1,000, monthly volume and stock-outs.
2. Call 3 quincaillerie wholesalers (East Algiers, El Eulma, Sétif) for spacer and tile-clip wholesale prices and monthly quantities.
3. Call Oxxo and Izdihar purchasing about packers, caps and integration gaps.
4. Call Cosider Canalisations and Trans-Canal about spacers for pipes and slabs.
5. Run a manual conformepro check of DD/DAPS for 3925.30, 3925.90 and 3926.90.

### Gaps
- Every GO above rests on price gaps, not on demonstrated pain. A GO should be downgraded if the interviews show abundant cheap stock with no stock-outs and wholesale prices near the landed floor.
