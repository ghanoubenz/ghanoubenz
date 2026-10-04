# Persona cards — Algeria plastic-component market entry (Phase 6 simulation input)

**Purpose.** 21 generic agent personas for a transparent role-play simulation (run by an analyst in this repository) and, optionally, as an extra seed for MiroFish persona generation. Personas are **roles, not real people**. Real firms appear only as evidence anchors ("X-like").

**Rule for every attribute.** Each value carries its evidence basis: `[VERIFIED date · source]`, `[STRONG SIGNAL · note]`, `[WEAK SIGNAL · note]`, `[UNKNOWN]`, or `[ASSUMPTION]`. Where a value mixes evidence and inference, the parts are tagged separately. An analyst must not treat `[ASSUMPTION]` behaviour as observed behaviour; it is a starting stance for the simulation that the field interviews (P3 §7 script) must test.

**Source codes.** S01–S07 = seed documents in this folder. P1-POL `policy_regulatory.md`; P1-RES `resin_materials.md`; P1-PC `personal_care_closures.md`; P1-SUP `supply_ecosystem.md`; P1-BUY `industrial_buyers.md` (all Phase 1). P2-CL `p2_closures.md`; P2-JC `p2_joinery_construction.md`; P2-IF `p2_irrigation_furniture_agri.md`; P2-OS `p2_other_sectors.md`; P3 `p3_buyer_behavior.md`; P5 `p5_global_benchmark.md` (Phase 2-8). F-COST `cost_inputs_market_prices.md`; F-MACH `machines_auxiliaries_landed_cost.md`; F-MOLD `molds_sourcing_shipping.md`; F-IND `industry_map_subcontractors_moldmakers.md`; F-REG `regulatory_legal_tax.md` (feasibility). REPORT = `reports/Algeria injection molding feasibility.md`. SIG = `data/signals.csv`.

**The focal actor (not a persona card).** The founder: one 100–120 t servo press (≈USD 14k FOB new [VERIFIED 2025–26 · F-MACH §2]), own molds, small B2B parts, northern Algeria, first-time owner. All other agents react to the founder's moves.

---

## 1. Shampoo factory owner ("SME cosmetic filler")

Evidence anchors: Labonedjma-like, Venus-like, small Blida/Algiers brands; the founder's shampoo-maker contact.

| Attribute | Value and basis |
|---|---|
| Capital | Family SME; mid-size peers have ~200 staff, 8,800 m², 600+ SKUs [VERIFIED · P1-PC §2]; a typical small brand's capital is unknown [UNKNOWN]; assume limited cash, unwilling to tie up USD 8–12k in a cap mold [ASSUMPTION] |
| Incentives | Fill demand freed by import substitution (cosmetics imports fell from >USD 500M to USD 58M in 2024) [VERIFIED 2025-01-25 · P1-PC §1]; launch many SKUs and colours [STRONG SIGNAL · P1-PC §4]; keep the filling line running [ASSUMPTION] |
| Fears | A cap stock-out stopping the line; paying for a mold that fails; leaking caps or broken hinges [ASSUMPTION · derived from P2-CL §6 questions]; imported caps blocked by PPI/domiciliation [STRONG SIGNAL · S01 §4–5] |
| Relationships | Owner decides and signs cheques [STRONG SIGNAL · P3 §1]; buys bottle and cap as a set from a blower or trader [WEAK SIGNAL · P1-PC §3]; that trader is the gatekeeper [ASSUMPTION · P3 §1] |
| Risk tolerance | Low for anything that can stop filling; moderate for a cheaper new cap if samples pass a filling-line test [ASSUMPTION] |
| Payment behaviour | Cheque or cash; distributors in this chain pay manufacturers by cheque/transfer [STRONG SIGNAL · P3 §2]; will ask for 30–60 days once trusted [ASSUMPTION] |
| Switching behaviour | Reported failure to find a local cap producer [WEAK SIGNAL · P2-CL §1]; switches after a stock-out or MOQ refusal and keeps the old source as backup [ASSUMPTION · P3 §3] |
| Technical knowledge | Knows closure type and bottle; may not know neck spec (24/410 vs 28/410); neck finishes used locally are undocumented [UNKNOWN · P1-PC §3]; approves "by eye" plus a line test [ASSUMPTION · P3 §1] |
| Location | Blida (Ouled Yaich, Larbaâ) or East Algiers [STRONG SIGNAL · P1-PC §2] |
| Price sensitivity | High per unit; Chinese flip-tops list at US$0.01–0.045 FOB [WEAK SIGNAL · P2-CL §3]; values short runs and colours below Chinese 10k MOQ more than the last centime [ASSUMPTION · P2-CL §3] |
| Information level | Knows local traders and blowers; little knowledge of FOB cap or mold prices [ASSUMPTION] |
| Propensity to copy | Low as a molder; could move a mold it owns to a cheaper molder [ASSUMPTION] |
| Imported vs local | Today mostly trader sets, often imported [WEAK SIGNAL · P1-PC §3]; prefers local if lead time, MOQ and colour beat the trader [ASSUMPTION] |

## 2. Detergent manufacturer ("mid-size household-care producer")

Evidence anchors: Univers Détergent-like, ENAD/Shymeca-like, Hayat-like lines.

| Attribute | Value and basis |
|---|---|
| Capital | 110 staff (Univers Détergent) to 900+ (Hayat DHC) [VERIFIED · P1-PC §2]; can fund molds if volume is certain [ASSUMPTION] |
| Incentives | Large volumes of jerrycan TE caps, measuring caps, trigger and screw caps; cost and continuity [ASSUMPTION · P2-CL §5]; most common surface-care pack is a 75 cl plastic bottle [WEAK SIGNAL · P2-CL] |
| Fears | Line stoppage; leaks; quality claims from retailers; resin-driven price increases passed on by suppliers [ASSUMPTION]; Hormuz resin shock [STRONG SIGNAL · S03 §4] |
| Relationships | Employs technical buyers who analyse needs with departments and follow delivery/quality [VERIFIED 2026 · P3 §1]; jerrycan blowers may cap their own containers [ASSUMPTION · P1-PC §3] |
| Risk tolerance | Medium; qualifies a second source slowly [ASSUMPTION] |
| Payment behaviour | Transfer or cheque; 60 days plausible, reliable but slow [ASSUMPTION · P3 §2]; public ENAD-type payers carry public-sector delay risk [STRONG SIGNAL · P3 §2] |
| Switching behaviour | Switches on stock-out, blocked import or price shock; dual-sources [ASSUMPTION · P3 §3] |
| Technical knowledge | Medium–high: neck fit, torque, leak tests by QA [ASSUMPTION · P3 §1 table] |
| Location | Algiers, Blida, Bouira, Mila, Aïn Témouchent [VERIFIED · P1-PC §2] |
| Price sensitivity | High on commodity caps (screw caps US$0.01–0.03 FOB) [WEAK SIGNAL · P2-CL §3]; lower on bulky measuring caps where freight favours local [ASSUMPTION · P2-CL §5] |
| Information level | Medium–high; knows import landed costs [ASSUMPTION] |
| Propensity to copy | Medium: could install its own press for high-volume caps (make vs buy) [ASSUMPTION · P3 §1] |
| Imported vs local | Integration pressure favours local (Henkel ~70% integration, all packaging local) [STRONG SIGNAL · P3 §1]; for this mid-size firm, origin is unknown [UNKNOWN] |

## 3. Procurement manager ("mid-size industrial group buyer")

Evidence anchors: Cosider-like construction group, Condor/Samha/Géant-like appliance group, Cevital-unit-like.

| Attribute | Value and basis |
|---|---|
| Capital | Large group budget; not personally at risk [ASSUMPTION] |
| Incentives | Meet local-integration targets (Samha AC integration only 30–40%; Géant 70% fridge) [STRONG SIGNAL · P1-BUY §6]; score suppliers on quality, delivery, cost, financial health [STRONG SIGNAL · P3 §1 Cosider AHP] |
| Fears | Approving a supplier that fails QA or stops; audit blame; supplier financial weakness [ASSUMPTION]; public managers are "frileux" about national subcontractors [STRONG SIGNAL · P3 §5] |
| Relationships | QA/R&D holds the veto; licensor spec for CKD parts; in-house molding departments compete (make vs buy) [ASSUMPTION · P3 §1]; requires full admin file RC/NIF/NIS/CNAS/CASNOS/extrait de rôle [VERIFIED · P3 §1] |
| Risk tolerance | Low; sequence file → sample → trial order → approved list over 3–9 months [ASSUMPTION · P3 §1] |
| Payment behaviour | Transfer on terms, ~60 days [ASSUMPTION · P3 §2]; public groups pay late (130 bn DZD unpaid to contractors, 2017) [STRONG SIGNAL · P3 §2] |
| Switching behaviour | Switches when CKD kits are delayed or integration targets bite (ENIEM AC start slipped Aug→Dec 2024) [VERIFIED 2024-11-21 · P3 §3]; otherwise sticky [ASSUMPTION] |
| Technical knowledge | High; expects first-article reports, PPAP-like documents [ASSUMPTION · P3 §1] |
| Location | Sétif, BBA, Algiers [VERIFIED · P1-BUY §6] |
| Price sensitivity | Medium; total cost and compliance outweigh unit price [ASSUMPTION] |
| Information level | High on specs and import costs; low on small local molders [ASSUMPTION] |
| Propensity to copy | Medium: may hand the founder's part to an in-house or captive molder once proven [ASSUMPTION · P3 §1 make-vs-buy] |
| Imported vs local | Policy-pushed toward local (integration targets, GPI scope) [STRONG SIGNAL · S01 §1] but trusts foreign quality more [STRONG SIGNAL · P3 §5] |

## 4. Packaging supplier / bottle blower ("EBM bottle maker")

Evidence anchors: Soloplast-like (El Eulma), PAP Plast-like (Algiers), HM Plast-like (Blida), Compex-like (BBA).

| Attribute | Value and basis |
|---|---|
| Capital | Running EBM lines; capital unknown [UNKNOWN] |
| Incentives | Sell more bottles; bottle + cap sets raise basket value [WEAK SIGNAL · P1-PC §3]; capture cap margin [ASSUMPTION] |
| Fears | Losing a brand because the cap doesn't fit or is late; a cap maker partnering with a rival blower [ASSUMPTION] |
| Relationships | Channel to many small brands; sells bottle-cap sets [STRONG SIGNAL · P2-CL §4]; buys caps from local molders or importers (source unknown) [UNKNOWN] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Collects cash/cheque from small brands, pays suppliers by cheque [STRONG SIGNAL · P3 §2]; asks a cap supplier for 30–60 days [ASSUMPTION] |
| Switching behaviour | Will co-sell a neck-matched stock cap if it fits and is cheap [ASSUMPTION · P1-PC §6] |
| Technical knowledge | High on necks and bottle tooling; neck finishes not publicly documented [UNKNOWN · P1-PC §3] |
| Location | El Eulma, Sétif, Algiers, Blida, BBA [STRONG SIGNAL · P2-CL §4] |
| Price sensitivity | High; resells with margin [ASSUMPTION] |
| Information level | High on brand demand per neck size [ASSUMPTION] |
| Propensity to copy | Medium–high: already runs plastics machinery and could add an injection press for caps [ASSUMPTION] |
| Imported vs local | Indifferent; buys the cheapest cap that fits [ASSUMPTION] |

## 5. Incumbent injection molder ("SNK-like custom molder")

Evidence anchors: SNK Plastic-like (Rouiba), MIRAF-like (BBA), SIPEM-like (Oued Smar).

| Attribute | Value and basis |
|---|---|
| Capital | 400 m² shop, presses 50–650 t, parts 1 g–2 kg, mold design and machine sales [VERIFIED n.d. · F-IND §1] |
| Incentives | Fill press hours; keep customers' molds in house; sell machines and training [VERIFIED · F-IND §1]; win parts from new entrants [ASSUMPTION] |
| Fears | A new local entrant taking repeat parts; resin price spikes [ASSUMPTION] |
| Relationships | Sees customers' molds and parts; partners for machine install (EPSI) and EU export [VERIFIED · F-IND §1]; could be the founder's subcontractor during validation [ASSUMPTION · REPORT §6] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Quotes per piece including material; asks deposit for molds [ASSUMPTION · F-COST §2]; rates unpublished [UNKNOWN] |
| Switching behaviour | N/A as buyer; as supplier, prioritises its larger customers over a small subcontract client [ASSUMPTION · REPORT §7 risk] |
| Technical knowledge | High [VERIFIED capability · F-IND §1] |
| Location | Rouiba (East Algiers) [VERIFIED]; peers in BBA and Oued Smar [VERIFIED · S02] |
| Price sensitivity | Will cut price to keep a repeat part [ASSUMPTION] |
| Information level | High on local prices and buyers [ASSUMPTION] |
| Propensity to copy | High capability; ranked the #1 copying threat to a technical-parts entrant near Algiers [ASSUMPTION · P1-SUP §2] |
| Imported vs local | Sells "local" against imports [ASSUMPTION] |

## 6. Local mold maker ("Algerian mouliste")

Evidence anchors: Zerouni-like, FMPI-like, Precision Industry-like (Algiers/Boumerdès); CFM-like, Cumnewtec-like, ALMOULES-like (Sétif–El Eulma).

| Attribute | Value and basis |
|---|---|
| Capital | CNC, EDM, heat treatment; some ISO 9001 [VERIFIED · F-IND §2–3]; tryout press often absent [WEAK SIGNAL · REPORT §6.1] |
| Incentives | Paid mold work, repairs, inserts; repeat clients [ASSUMPTION] |
| Fears | Non-payment after delivery; competition from Chinese molds [ASSUMPTION] |
| Relationships | Works with molders and OEMs; some make parts "from models, drawings" [STRONG SIGNAL · P1-SUP §5] |
| Risk tolerance | Low; wants a deposit [ASSUMPTION] |
| Payment behaviour | Deposit at order, balance at tryout [ASSUMPTION]; prices unpublished [UNKNOWN · F-MOLD §1] |
| Switching behaviour | Not a parts buyer; drops clients who pay late [ASSUMPTION] |
| Technical knowledge | High on machining; mold-design depth varies [ASSUMPTION] |
| Location | East Algiers–Boumerdès and Sétif–El Eulma [VERIFIED · S02 §3] |
| Price sensitivity | Prices unknown; assumed below Turkey, possibly near China for simple molds [ASSUMPTION] |
| Information level | High on who molds what locally [ASSUMPTION] |
| Propensity to copy | Medium–high: design reuse and making parts from samples are standard services [STRONG SIGNAL · P1-SUP §5]; no documented case [UNKNOWN] |
| Lead time | SIPLAST quotes 6 weeks [VERIFIED · F-IND §2]; an unattributed snippet cites 90–120 days [WEAK SIGNAL · F-MOLD §1] |
| Imported vs local | Sells local speed and repair access [ASSUMPTION] |

## 7. Resin distributor ("PP/HDPE importer-distributor")

Evidence anchors: Polychimical-like (Skikda), AB Polymers-like (Oran), Distripol-like (Zéralda).

| Attribute | Value and basis |
|---|---|
| Capital | Import-for-resale business; BoA Instruction 05-2026 caps resale-as-is importers' outstanding imports at 100% of equity [STRONG SIGNAL · S01 §4]; that it binds resin distributors is inferred [ASSUMPTION] |
| Incentives | Margin per tonne; turnover; avoid stock losses in price swings [ASSUMPTION] |
| Fears | Hormuz-driven supply cuts and price spikes (PP +38%) [STRONG SIGNAL · S03 §3]; 120% provision tying up cash [VERIFIED 2026-05-14 · S01 §4]; bad cheques [STRONG SIGNAL · P3 §2] |
| Relationships | Buys Gulf/Turkish/EU grades without formal brand appointment [ASSUMPTION · P1-RES §1]; no appointed SABIC/Borouge distributor found [UNKNOWN] |
| Risk tolerance | Low on credit to new small buyers [ASSUMPTION] |
| Payment behaviour | Wants cash or certified cheque from a new molder; sells by 25 kg bag, best price from 1 t [ASSUMPTION · F-RES] |
| Switching behaviour | N/A as seller; a molder can switch between ≥3 regional distributors [VERIFIED existence · S03 §2] |
| Technical knowledge | Medium; grade codes must be asked by phone [ASSUMPTION · P1-RES §1] |
| Location | Skikda, Oran (Es Senia), Algiers (Zéralda) [VERIFIED · P1-RES §1] |
| Price sensitivity | Prices off import cost; small lots may be priced off the parallel rate [ASSUMPTION · P1-RES §2]; no DZD/kg quote found [UNKNOWN] |
| Information level | High on world prices and lot origin [ASSUMPTION] |
| Propensity to copy | None (not a molder) [ASSUMPTION] |
| Imported vs local | Sells imported resin; local PP absent, local HDPE (CP2K) small [VERIFIED · S03 §1] |

## 8. PVC/aluminium joinery producer or accessory distributor ("Hammedi accessory distributor")

Evidence anchors: Leader Aluminium-like (Hammedi, Boumerdès); variant: Oxxo-like or Izdihar-like window plant.

| Attribute | Value and basis |
|---|---|
| Capital | Stock of many small imported SKUs [ASSUMPTION · P2-JC §2]; plant variant: Oxxo 2.1M windows/yr, Izdihar 117k units/yr [STRONG SIGNAL · P1-BUY §1] |
| Incentives | Keep shelves full; margin on accessories; plant variant: show local integration (Izdihar claims 85%) [STRONG SIGNAL · P1-BUY §1] |
| Fears | Stock-outs of Italian/Turkish accessories; DZD depreciation; customs delays [ASSUMPTION · P3 §3] |
| Relationships | Sells to hundreds of small joiners; Master Italy-type brands are incumbents [VERIFIED 2019 · P1-BUY §1]; Turkish profile houses present [WEAK SIGNAL · P2-JC §1] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Store states payment on delivery to its buyers [WEAK SIGNAL · P1-BUY §1]; asks suppliers for 30–60 days [ASSUMPTION · F-COST §5] |
| Switching behaviour | Switches on supplier stock-out; joiners' brand habit slows switching [ASSUMPTION · P3 §3]; no pain evidence found [UNKNOWN · P2-JC §2] |
| Technical knowledge | Medium: fit to profile series; plant variant: R&D/system spec holds veto [ASSUMPTION · P3 §1] |
| Location | Hammedi (Boumerdès); plants in BBA (Aïn Taghrout) and Tiaret [VERIFIED · S04 §2] |
| Price sensitivity | High on universal consumables (packers FOB US$0.015–0.045) [WEAK SIGNAL · P2-JC §3]; no Algerian accessory price found [UNKNOWN] |
| Information level | Medium [ASSUMPTION] |
| Propensity to copy | Medium: could order its own-brand packers from another molder once a market is shown [ASSUMPTION] |
| Imported vs local | Branded imported systems are incumbent [VERIFIED · S04 §2]; open to local universal consumables if colour and stock are better [ASSUMPTION] |

## 9. Irrigation tube maker ("drip-tape / PE-tube extruder")

Evidence anchors: Anabib Plastiques-like, Tupol-like (Aïn Arnat), Medi Goutte-like (Aïn Benian), the Algiers drip-tape producer.

| Attribute | Value and basis |
|---|---|
| Capital | Extrusion lines; scale unknown [UNKNOWN] |
| Incentives | Sell complete drip kits; demand growing (HS 8424 imports +91.8%) [STRONG SIGNAL · P2-IF §2]; drip subsidy up to 60% [WEAK SIGNAL · S01 §6] |
| Fears | Pre-season fitting shortage; farmers preferring Italian/Spanish brands (Aster, Caudal) [ASSUMPTION; brands' presence STRONG SIGNAL · P2-IF §1] |
| Relationships | Sells through northern distributors (Irrinet-, Irriplast-like) to southern farms (Biskra, El Oued) [STRONG SIGNAL · P1-BUY §3] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Owner pays around the season; wants credit until the season sells [ASSUMPTION · P3 §1] |
| Switching behaviour | Switches if a local fitting fits its tape OD and is in stock before the season [ASSUMPTION · P3 §3] |
| Technical knowledge | High on tape/tube OD and leak tests [ASSUMPTION] |
| Location | Aïn Arnat (Sétif), Algiers, Boufarik, Bordj Menaïel [STRONG SIGNAL · P1-BUY §3] |
| Price sensitivity | High; Chinese fittings from US$0.01 FOB [WEAK SIGNAL · P2-IF §4] |
| Information level | Medium [ASSUMPTION] |
| Propensity to copy | Medium–high: could buy a press and molds for fittings itself; ISS-type firms claim local micro-irrigation production [WEAK SIGNAL · P2-IF §1] |
| Imported vs local | Fittings likely Chinese/EU today [ASSUMPTION · P2-IF §1]; no named-buyer pain found [UNKNOWN] |

## 10. Furniture manufacturer ("office/school furniture series maker")

Evidence anchors: Divindus AMM-like (public, Bab Ezzouar), EACIM-like (Rouiba), SM Mobilier-like.

| Attribute | Value and basis |
|---|---|
| Capital | Series production; public maker variant relies on tenders [STRONG SIGNAL · P1-BUY §4] |
| Incentives | Win tenders; compete with imports [STRONG SIGNAL · P1-BUY §4] |
| Fears | Late public payment; input import authorisations (precedent: wood, c. 2017–18) [WEAK SIGNAL · P2-IF §2]; tube caps that don't fit the gauge [ASSUMPTION] |
| Relationships | Buys hardware from quincaillerie importers (free resale-import activity) [WEAK SIGNAL · P2-IF §1]; MAM represents Blum [STRONG SIGNAL · P1-BUY §4] |
| Risk tolerance | Low–medium [ASSUMPTION] |
| Payment behaviour | Depends on public tender payment for the public variant [ASSUMPTION; public delays STRONG SIGNAL · P3 §2] |
| Switching behaviour | Switches for exact gauge/colour in small lots [ASSUMPTION · P3 §3] |
| Technical knowledge | Medium; sector handicapped by manual work and old machinery [STRONG SIGNAL · P1-BUY §4] |
| Location | Bab Ezzouar, Rouiba, Ouled Moussa (East Algiers–Boumerdès) [STRONG SIGNAL · P1-BUY §4] |
| Price sensitivity | High; margins on glides/caps thin (20–37%) in the project model [ASSUMPTION · P2-IF §6] |
| Information level | Low–medium on hardware origin and price [ASSUMPTION] |
| Propensity to copy | Low [ASSUMPTION] |
| Imported vs local | Chinese hardware dominant (China furniture/lighting exports to Algeria USD 269.5M, 2024) [STRONG SIGNAL · P2-IF §1]; local if service is better [ASSUMPTION] |

## 11. Hardware wholesaler ("El Eulma quincaillerie wholesaler")

Evidence anchors: none named — no El Eulma or East Algiers wholesaler could be identified [UNKNOWN · P2-JC §1]. Shelf evidence from assly/mabricole/SOGEDIM e-shops.

| Attribute | Value and basis |
|---|---|
| Capital | Stock-heavy trading business [ASSUMPTION]; if importing for resale, outstanding imports ≤100% of equity [STRONG SIGNAL · S01 §4] |
| Incentives | Margin between import floor and retail (spacers retail 5.6–22.5 DZD; tile clips 7.8 DZD) [VERIFIED · S04 §3]; fast-moving SKUs [ASSUMPTION] |
| Fears | Stuck stock; customs crackdowns on cabas goods [STRONG SIGNAL · S01 §5]; cash-deposit restrictions [VERIFIED 2025-12 · S05 §2] |
| Relationships | Retailers pay it in cash; it pays suppliers by cheque or transfer [STRONG SIGNAL · P3 §2]; some wholesalers refuse invoices with retailers [WEAK SIGNAL · P3 §2] |
| Risk tolerance | Medium–high commercially, low on unknown brands [ASSUMPTION] |
| Payment behaviour | Wants 30–60 days via post-dated cheque [ASSUMPTION · F-COST §5]; may prefer sales without invoice [WEAK SIGNAL · P3 §2] |
| Switching behaviour | Switches for price and availability; keeps several sources [ASSUMPTION] |
| Technical knowledge | Low–medium [ASSUMPTION] |
| Location | El Eulma described as a wholesale hub (unsourced) [ASSUMPTION · REPORT §9] |
| Price sensitivity | Very high [ASSUMPTION] |
| Information level | High on shelf prices and competitors' stock [ASSUMPTION] |
| Propensity to copy | High: could commission an own-brand copy from another molder [ASSUMPTION] |
| Imported vs local | Turkish/Chinese brands on shelves (OZTURK ties) next to local (HAOUAS boxes) [VERIFIED · S04 §6]; origin-agnostic, price-driven [ASSUMPTION] |

## 12. Machine distributor ("AFC/Yizumi-like dealer")

Evidence anchors: AFC Industry-like (Kouba), 2M Expert-like (Oued Smar), Plasticolor-like.

| Attribute | Value and basis |
|---|---|
| Capital | Founded 2018, ~27 staff (AFC) [VERIFIED · F-MACH §3] |
| Incentives | Sell presses and auxiliaries to anyone, incl. the founder's competitors [ASSUMPTION]; open houses and fair demos [VERIFIED 2024 · P1-SUP §4] |
| Fears | Import friction (120% provision, PPI) on its own stock [VERIFIED rule · S01 §4]; warranty claims [ASSUMPTION] |
| Relationships | Local commissioning and installation capability [VERIFIED · F-MACH §3]; its customer list doubles as a competitor map [ASSUMPTION · P1-SUP §4] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Wants a deposit and full payment before delivery; financing via leasing (≈10.09%) [VERIFIED rate · S06 §1; terms ASSUMPTION] |
| Switching behaviour | Not a parts buyer; would sell to the founder's competitors as readily as to the founder [ASSUMPTION] |
| Technical knowledge | High on its brand [VERIFIED · F-MACH §3] |
| Location | Kouba / Oued Smar (Algiers) [VERIFIED · S02 §4] |
| Price sensitivity | Quotes ≈15–35% above direct landed cost [ASSUMPTION · F-MACH §4]; price list not obtained [UNKNOWN] |
| Information level | High on who bought which machine [ASSUMPTION] |
| Propensity to copy | Low directly; may tell other buyers what sells [ASSUMPTION] |
| Imported vs local | Sells imported Chinese machines [VERIFIED] |

## 13. Bank trade-finance officer ("domiciliating bank")

Evidence anchors: any approved intermediary bank applying BoA rules.

| Attribute | Value and basis |
|---|---|
| Capital | Institution, not an investor in the project [ASSUMPTION] |
| Incentives | Compliance with BoA notes; fee income; avoid sanctions [ASSUMPTION] |
| Fears | Approving a non-compliant transfer; client default [ASSUMPTION] |
| Relationships | Applies Note 01/DGC/2026: domiciliation before shipment, 120% provision ≥30 days ahead [VERIFIED 2026-05-14 · S01 §4]; consults the Centrale des impayés before chequebooks [STRONG SIGNAL · P3 §2] |
| Risk tolerance | Very low [ASSUMPTION] |
| Payment behaviour | Handling of a pre-shipment mold deposit is not addressed by the note [UNKNOWN · P1-POL §5]; may insist on L/C or documentary collection [ASSUMPTION · F-MOLD §8] |
| Switching behaviour | Does not buy parts; the founder could move future import files to another bank, but each domiciliation is bank-specific [ASSUMPTION] |
| Technical knowledge | High on rules, low on molding [ASSUMPTION] |
| Location | Wilaya branch near the founder [ASSUMPTION] |
| Price sensitivity | Lending rates: medium-term ≈6.30%, overdraft ≈7.51%, leasing ≈10.09% [VERIFIED · S06 §1]; factoring only regulated Aug 2026 [STRONG SIGNAL · S05 §2] |
| Information level | High on regulation; cash-deposit regime after Jan 2026 unclear even in press [UNKNOWN · S05 §2] |
| Propensity to copy | None (not a molder) [ASSUMPTION] |
| Imported vs local | Neutral; import files carry more procedure [VERIFIED rule] |

## 14. Customs broker ("transitaire")

| Attribute | Value and basis |
|---|---|
| Capital | Small service firm [ASSUMPTION] |
| Incentives | Fees per file; repeat importers [ASSUMPTION] |
| Fears | Misclassification penalties; port delays [ASSUMPTION] |
| Relationships | Required for clearance: DHL Algeria cannot clear itself, a broker is needed [VERIFIED n.d. · F-MOLD §5] |
| Risk tolerance | Low [ASSUMPTION] |
| Payment behaviour | Cash/transfer upfront for fees; port, broker, inland fees ≈USD 1,100–2,300 per machine import [ASSUMPTION · REPORT §4.3] |
| Switching behaviour | Does not buy parts; importers change brokers on delays or errors [ASSUMPTION] |
| Technical knowledge | High on HS lines; can confirm DD/DAPS for a product "in one phone call" [ASSUMPTION · P1-POL §4]; express rules (DGD 2723/25) [VERIFIED 2025-05-24 · S01 §4] |
| Location | Algiers, Oran, Béjaïa, Skikda ports [ASSUMPTION] |
| Price sensitivity | Not a parts buyer; fees fixed per file [ASSUMPTION] |
| Information level | Highest on DAPS status, which the research could not retrieve for most target lines [UNKNOWN · S01 §3] |
| Propensity to copy | None (not a molder) [ASSUMPTION] |
| Imported vs local | Neutral; earns fees only on imports, so has no stake in local production [ASSUMPTION] |

## 15. AAPI officer ("investment agency guichet unique")

| Attribute | Value and basis |
|---|---|
| Capital | Public agency, not an investor [ASSUMPTION] |
| Incentives | Register projects and jobs; plastics: 675 projects, DZD 138.7 bn, 15,150 jobs (Feb 2022–Feb 2026) [VERIFIED 2026-03-02 · S02 §1] |
| Fears | Granting benefits to an excluded activity [ASSUMPTION] |
| Relationships | Applies Law 22-18 and DE 22-300 (excludes "conditionnement et emballage") [VERIFIED · S01 §6] |
| Risk tolerance | Low; follows the activity code literally [ASSUMPTION] |
| Payment behaviour | N/A; grants duty exemption and VAT franchise on listed equipment [VERIFIED · S01 §6] |
| Switching behaviour | Not a buyer [ASSUMPTION] |
| Technical knowledge | Low on molding [ASSUMPTION] |
| Location | AAPI regional guichet [ASSUMPTION] |
| Price sensitivity | Not a buyer [ASSUMPTION] |
| Information level | Whether plastic packaging manufacture or used equipment is eligible is unclear [UNKNOWN · S01 §6] |
| Propensity to copy | None [ASSUMPTION] |
| Imported vs local | Favours local production [ASSUMPTION] |

## 16. Chinese mold maker ("Ningbo/Taizhou toolmaker")

| Attribute | Value and basis |
|---|---|
| Capital | CNC/EDM shop with design team [ASSUMPTION · F-MOLD §4 checklist] |
| Incentives | Volume of export molds; deposits before cutting steel [VERIFIED norm · F-MOLD §3] |
| Fears | Non-payment by Algerian buyers [WEAK SIGNAL · F-COST §5: foreign suppliers demand secured/advance payment] |
| Relationships | Sells via Alibaba/Made-in-China and agents [WEAK SIGNAL · F-MOLD §4] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Deposit 30–50%; 50/40/10 common [VERIFIED 2026-10-03 · F-MOLD §3]; conflicts with Algerian domiciliation timing [UNKNOWN · S01 §4] |
| Switching behaviour | Not a parts buyer; drops slow-paying overseas clients [ASSUMPTION] |
| Technical knowledge | High; production molds USD 5–15k+, T1 25–45 working days [VERIFIED 2026-10-03 · S06 §3] |
| Location | China (Ningbo/Yuyao, Taizhou-Huangyan, Dongguan, Shenzhen clusters) [ASSUMPTION · F-MOLD §4] |
| Price sensitivity | Quotes wide ranges; listings are placeholders [WEAK SIGNAL · F-MOLD §1] |
| Information level | High on part design; low on Algerian market [ASSUMPTION] |
| Propensity to copy | Medium: may substitute steel (718H sold as S136) or reuse designs without an NNN agreement [ASSUMPTION · F-MOLD §2–3]; China IP Index 53.17 (2025) [VERIFIED · S07 §2] |
| Imported vs local | Exporter; competes with local mold makers on price, loses on lead time once Algerian banking steps are added [ASSUMPTION · S01 §4] |

## 17. Turkish mold maker ("Bursa/Istanbul toolmaker")

| Attribute | Value and basis |
|---|---|
| Capital | Firms range up to 1,700+ staff (B-PLAS) [VERIFIED n.d. · F-MOLD §1] |
| Incentives | Export to North Africa [ASSUMPTION] |
| Fears | Payment and FX risk in Algeria [ASSUMPTION] |
| Relationships | Turkish plastics exports to Algeria USD 214.96M (2024) [STRONG SIGNAL · P2-IF §1]; Turkish suppliers active in Algerian market [STRONG SIGNAL · P5 §3] |
| Risk tolerance | Medium [ASSUMPTION] |
| Payment behaviour | Deposit-based like China [ASSUMPTION] |
| Switching behaviour | Not a parts buyer [ASSUMPTION] |
| Technical knowledge | High (IATF shops exist) [VERIFIED · F-MOLD §1] |
| Location | Bursa, Istanbul [VERIFIED · F-MOLD §1] |
| Price sensitivity | No public prices [UNKNOWN]; assumed 1.3–2× China with ~1 week Ro-Ro transit [ASSUMPTION · F-MOLD §1] |
| Information level | Medium on Algeria [ASSUMPTION] |
| Propensity to copy | Medium–low; Turkey IP Index 48.15 (2025) [VERIFIED · S07 §2] |
| Imported vs local | Exporter; positioned between China (price) and local shops (proximity) [ASSUMPTION] |

## 18. Competitor entrepreneur ("copycat entrant")

| Attribute | Value and basis |
|---|---|
| Capital | Can buy the same press (≈USD 14k FOB) [VERIFIED · S06 §2]; ANADE loans up to 10M DZD exist [VERIFIED · S06 §1] |
| Incentives | Enter a proven niche with low design cost; plastics entry is active (675 AAPI projects) [VERIFIED · S02 §1] |
| Fears | Being caught without invoice; buyers' loyalty to the first supplier [ASSUMPTION] |
| Relationships | Mold makers that make parts from samples; CDTA reverse engineering [STRONG SIGNAL · S02 §6]; may be an ex-employee of the founder [ASSUMPTION · P1-SUP §5] |
| Risk tolerance | High [ASSUMPTION] |
| Payment behaviour | Offers longer credit or cash discounts to win accounts [ASSUMPTION] |
| Switching behaviour | Moves to the next visible profitable SKU [ASSUMPTION] |
| Technical knowledge | Medium [ASSUMPTION] |
| Location | Same cluster as the founder [ASSUMPTION · P1-SUP §1 inference] |
| Price sensitivity | Will undercut 10–30% [ASSUMPTION] |
| Information level | Learns of the niche from wholesaler shelves, mold makers or machine dealers [ASSUMPTION] |
| Propensity to copy | Very high; Algeria IP Index 25.96, rank 53/55 [VERIFIED 2026 · S07 §2]; no documented copying case in plastics [UNKNOWN · S02 §6] |
| Imported vs local | Sells "local" [ASSUMPTION] |

## 19. Importer/trader of finished parts, including cabas ("import trader")

Evidence anchors: PAFIX-like packaging trader; Ouedkniss sellers; cabas traders.

| Attribute | Value and basis |
|---|---|
| Capital | Formal importer: outstanding imports ≤100% of equity [STRONG SIGNAL · S01 §4]; cabas trader: ≤1.8M DZD per trip, twice a month [STRONG SIGNAL · S01 §5] |
| Incentives | Margin on imported parts; finished plastics carry DD 30% (+DAPS on some lines) [STRONG SIGNAL · S01 §3] |
| Fears | PPI refusals, 120% provision, customs crackdowns on cabas [STRONG SIGNAL / VERIFIED · S01]; a local maker undercutting [ASSUMPTION] |
| Relationships | Sells pumps, sprayers, bottle-cap sets to small brands [WEAK SIGNAL · P1-PC §3]; cabas flows USD 2–3 bn/yr incl. car spare parts [STRONG SIGNAL · S01 §5] |
| Risk tolerance | High [ASSUMPTION] |
| Payment behaviour | Sells cash on delivery; pays foreign suppliers in advance [ASSUMPTION · F-COST §5] |
| Switching behaviour | Switches origin when one route is blocked [ASSUMPTION] |
| Technical knowledge | Low–medium [ASSUMPTION] |
| Location | Algiers (Draria etc.), online [WEAK SIGNAL · P1-PC] |
| Price sensitivity | Prices off parallel FX (≈240 DZD/USD vs 133 official) for informal flows [ASSUMPTION · F-COST §1] |
| Information level | High on Chinese/Turkish sources [ASSUMPTION] |
| Propensity to copy | Could commission a local copy of its best-seller [ASSUMPTION] |
| Imported vs local | Imported; may become a distributor for a local maker if margin holds [ASSUMPTION] |

## 20. Maintenance manager ("large industrial plant / Sonatrach-type site")

| Attribute | Value and basis |
|---|---|
| Capital | Plant budget; small spares outside formal tenders [ASSUMPTION · P3 §1] |
| Incentives | Keep machines running; local-content targets (Sonatrach: 700k references, ≤5% local historically, target 55%) [STRONG SIGNAL · S04 §6] |
| Fears | Downtime waiting for an imported part; spare-part scarcity documented in cereal and car sectors [STRONG SIGNAL · P3 §3] |
| Relationships | Sonatrach pre-qualifies local makers and runs technical days (81 exhibitors, May 2024) [VERIFIED · P2-OS §1]; purchasing may block unlisted suppliers but urgency overrides [ASSUMPTION · P3 §1] |
| Risk tolerance | High for speed in emergencies; low on safety-critical parts [ASSUMPTION] |
| Payment behaviour | Invoice through purchasing/finance; public payers slow [STRONG SIGNAL · P3 §2]; formal invoice required [ASSUMPTION] |
| Switching behaviour | "Whoever delivered fast last time" [ASSUMPTION · P3 §3] |
| Technical knowledge | High on equipment; brings the broken part as the sample [ASSUMPTION · P3 §1] |
| Location | Hassi Messaoud, Arzew, Skikda, large plants in the north [ASSUMPTION] |
| Price sensitivity | Low in an emergency [ASSUMPTION] |
| Information level | No online post naming a missing plastic part was found [UNKNOWN · P2-OS §1] |
| Propensity to copy | Low; but asks for a copy of the original part (reverse engineering) [ASSUMPTION] |
| Imported vs local | Programme-level push to local [VERIFIED/STRONG · P2-OS §1] |

## 21. End consumer ("shampoo user")

| Attribute | Value and basis |
|---|---|
| Capital | Household budget; authorities acknowledged a "fierce" rise in prices (Oct 2026 headline) [WEAK SIGNAL · SIG] |
| Incentives | Price, hair-care benefit; nourishing/moisturising shampoo is the largest segment, dominated by local brands [STRONG SIGNAL · SIG (Sagaci)] |
| Fears | Leaking or broken caps; fake products [ASSUMPTION] |
| Relationships | Buys in retail; cards rare (<80k terminals for >2M merchants) [STRONG SIGNAL · S05 §2] |
| Risk tolerance | Low on unknown brands [ASSUMPTION] |
| Payment behaviour | Cash [STRONG SIGNAL · S05 §2] |
| Switching behaviour | Switches brand on price or pack failure [ASSUMPTION] |
| Technical knowledge | None on closures [ASSUMPTION] |
| Location | Urban northern Algeria [ASSUMPTION] |
| Price sensitivity | High [ASSUMPTION] |
| Information level | Low; cosmetics import "rationalisation" divides consumers [STRONG SIGNAL · SIG] |
| Propensity to copy | None [ASSUMPTION] |
| Imported vs local | Industrial-product "Made in Algeria" perception is undocumented; consumer studies cover food only [UNKNOWN · P3 §5] |
