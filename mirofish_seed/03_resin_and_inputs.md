# Seed 03 — Algeria: resin, masterbatch and recycled-material supply for a PP/HDPE injection start-up (as of 2026-10-04)

**Context.** Raw material is the largest variable cost of a small injection molder. This document lists who supplies PP, HDPE, masterbatch and regrind in Algeria, what prices are known, and the history of supply shocks. Seed document for a multi-agent simulation.

**Evidence tags.** `[VERIFIED date · source]` = seen in search-engine snippets of the named source (no page read in full). `[STRONG SIGNAL]`, `[WEAK SIGNAL]`, `[UNKNOWN]` as usual; `[ASSUMPTION]` only in the last section. Source notes: `Phase 1 Algeria reality map/resin_materials.md` (P1-RES), `Algeria injection molding feasibility/resin_supply.md` (F-RES), `cost_inputs_market_prices.md` (F-COST), `Phase 2-8/p2_irrigation_furniture_agri.md` (P2-IF), `reports/Algeria injection molding feasibility.md` (report), `model/economics.py`, `data/signals.csv`. Resin customs duties are in seed 01.

---

## 1. Local polymer production

- Algeria has no local PP production. The Arzew PDH-PP project (550 kt/yr, STEP, near Oran) is reported both as "launched Sep 2024, completion planned 2027" (Maghreb Émergent, 2026) and as stalled with works stopped and no restart date (Ecofin). The sources conflict. [STRONG SIGNAL, conflicting · P1-RES §2]
- Sonatrach had earlier said the Arzew PP plant would "enter production in 2025" and cover all national PP needs, which are currently imported. [VERIFIED n.d. · sonatrach.com; F-RES]
- CP2K Skikda produced 34,198 t of HDPE in 2024 (+101% y/y) against 130 kt/yr nameplate (~26% utilisation). [VERIFIED 2025-12-03 · Algérie Eco on Sonatrach 2024 annual report; P1-RES §2]
- CP2K installations are described as aging, with recurrent shutdowns. [WEAK SIGNAL · search context; data/signals.csv] Its grade slate and whether small buyers can get it via distributors are not known. [UNKNOWN · P1-RES §2]
- Algeria produced about 3% of its raw-plastic needs; imports rose from 304 kt (2007) to 817 kt (2015); raw-plastic consumption was ~USD 2 bn/yr in 2019. [STRONG SIGNAL · AlgeriaInvest, Radio Algérie 2019; P1-RES §2]
- Imports of plastic raw materials and products were ~USD 2.98 bn in 2025 (+6.8%); agrifood packaging depends almost entirely on imported granules. [STRONG SIGNAL · Maghreb Émergent, El Djazair El Djadida; P1-RES §2]

## 2. Distributors and producers of inputs

- PP/HDPE distributors in all three northern regions: Polychimical SARL (Skikda; PEBD, PEHD, PP, PPR, PS, PVC, PET, PA), Distripol SARL (Zéralda, Algiers; PP, PS, PE), AB Polymers SARL (Es Senia, Oran; injection-grade PEHD, PP homo and copolymer — the only one explicitly citing injection-grade HDPE). [VERIFIED n.d. (seen 2026-10-04) · Kompass, adresse-algerie, Pages Jaunes; P1-RES §1]
- Other raw-material listings: OHDO Plastique (Khemis El Khechna), Himaplast (Bou Ismaïl), Dadi Plastique (ZI Sétif), Plast Afrique (Ghardaïa); Kompass lists ~47 synthetic-resin firms. [VERIFIED n.d. · Pages Jaunes, Kompass; P1-RES §1]
- No appointed Algerian distributor of SABIC, Borouge or another brand was found; Ravago, Ultrapolymers and Resinex show no Algeria office. [UNKNOWN · P1-RES §1]
- An Algerian buyer (Groupe Med Dora) posted a request for SABIC polypropylene. [WEAK SIGNAL · data/signals.csv]
- No Algerian stockist of ABS, POM, PC, TPE or TPU was found; Polychimical lists "PA" of unspecified type. [UNKNOWN / WEAK SIGNAL · P1-RES §2]
- Colour masterbatch makers (thin base): Himaplast (Bou Ismaïl), Decoplast (El Bouni, Annaba), BRUM Algérie (Bir El Djir, Oran; also recycled PP/PEHD and pallets), Smart Polymer Colors (Boghni, Tizi Ouzou; to spec), Taif Master Batch (Beni Tamou, Blida). Tapidor (Es Senia) makes masterbatch for its own lines. [STRONG SIGNAL · Kompass, dzentreprise, tapidor.com; P1-RES §1]
- UV/additive masterbatch was not found locally; film maker Plastedj (Blida) uses Italian reference masterbatches. Polytec (UAE) and EuP (Egypt) market masterbatch directly to Algeria. [STRONG SIGNAL · plastedj.dz, polytecmb.com, eupegypt.com; P1-RES §1]
- Recyclers: El Kader Plast (Oggaz, Mascara) — announced as Algeria's largest PP/PEHD recycler, 2,000 kg/h line, 70% of granules sold, 30% used for pallets; opening announced for Sep 2022, current status not verified. [STRONG SIGNAL · Algérie Eco 2022-09-13; P1-RES §1] Unnamed recyclers on EspaceAgro offer PET, PVC, PEHD and PP regrind and granules from 20 t/week to 1,000 t/month. [WEAK SIGNAL · EspaceAgro; P1-RES §1]
- Recytech (Bouira) recycles tyres, not thermoplastics. [VERIFIED n.d. · recytech-dz.com; P1-RES §1]
- Phone numbers, MOQs and grade lists for AB Polymers, Distripol, Himaplast, Decoplast, BRUM and Taif were not retrieved. [UNKNOWN · P1-RES §1]

## 3. Prices

- No 2025–2026 Algerian DZD/kg quote for any virgin resin was found. [UNKNOWN · P1-RES §2]
- World prices after the 2026 Strait of Hormuz closure: PE ~1,176 USD/t, PP ~1,288 USD/t. [STRONG SIGNAL · El Watan 2026; P1-RES §2]
- PE +37% and PP +38% on world markets; Hormuz transits down >70%. [STRONG SIGNAL · El Djazair El Djadida 2026; P1-RES §3]
- Europe: PP rose from ~1,300 to ~2,500 EUR/t and PET by ~60% to ~1,850 USD/t between Feb and Apr 2026. [STRONG SIGNAL · Maghreb Émergent; P1-RES §3]
- 2021 crisis: raw plastic rose from 170 to 520 DZD/kg (>300%); recycled plastic from 100 to 250 DZD/kg. [VERIFIED c.2021 · Echorouk, Maghreb Émergent; P1-RES §3]
- Regrind and waste: industrial transparent PEHD broyé listed at 110 DZD/kg (undated); clean PEHD waste 25–35 DZD/kg; plastic waste 15–20 DZD/kg from associations and 30–50 DZD/kg from firms/traders (academic, undated). [WEAK SIGNAL · EspaceAgro listing, ASJP/CERIST; P1-RES §2]
- Official FX ~133 DZD/USD and ~155 DZD/EUR vs parallel ~240 DZD/USD and ~276 DZD/EUR (2026); see seed 06. [VERIFIED 2026 · F-COST §1]

## 4. Shortage history and 2026 risk

- 2020–21 shock was policy-driven: import licensing halted supply, many plants stopped for months; importers then received licences with imports expected in 30–45 days. [VERIFIED c.2021 · Echorouk; P1-RES §3]
- 2026 shock is global: after the Feb–Mar 2026 war, Hormuz maritime traffic fell ~97% and naphtha, ethylene and polyolefin exports were almost paralysed. [STRONG SIGNAL · El Watan; P1-RES §3]
- Algerian transformers face "rising prices that signal an approaching raw-material supply crisis". [STRONG SIGNAL · Maghreb Émergent 2026; P1-RES §3] No Algerian-specific 2026 report of plants stopped or rationing was found. [UNKNOWN · P1-RES §3]
- French packaging federation Elipso denounced "abusive force majeure" declarations by resin suppliers citing Hormuz; a counter-signal says European output ran flat out and shortage risk stayed limited. [STRONG SIGNAL (Elipso) · WEAK SIGNAL (counter-signal) · L'Usine Nouvelle; P1-RES §3]
- In the ONS Q2-2025 survey, 30% of private industrial bosses said raw-material supply was below demand. [STRONG SIGNAL · TSA; P2-IF §2]
- The government is accelerating a ~USD 7 bn naphtha/LPG-based petrochemical portfolio after Hormuz. [STRONG SIGNAL · Maghreb Émergent; data/signals.csv]
- The Hormuz status and Algerian distributor stock levels in Sep–Oct 2026 are not known. [UNKNOWN · P1-RES §3]

---

## Assumptions (not facts)

- Distributor ex-VAT price for virgin PP or HDPE in Q3–Q4 2026 is likely 220–350 DZD/kg (CFR 1,180–1,290 USD/t × 133 ≈ 157–171 DZD/kg, plus 10–15% duty/logistics and 10–25% distributor margin; high end for small lots or parallel-rate pricing). Pre-shock project estimate was 180–250 DZD/kg. [ASSUMPTION · P1-RES §2; F-RES]
- Cost models in the project use resin at 220, 264, 285, 290 or 300 DZD/kg depending on the note; a sensitivity at 220/300/400 DZD/kg is recommended. [ASSUMPTION · P1-RES §4; model/economics.py]
- Virgin resin is about 50–70% of the ex-works cost of a simple PP/HDPE part; a ±30% resin swing can erase the margin on commodity products. [ASSUMPTION · P1-RES §2]
- By Oct 2026 material is probably available at a price rather than physically absent. [ASSUMPTION · P1-RES §3]
- Commodity distributors resell Gulf (SABIC, Borouge), Turkish or European grades without formal appointment; engineering resins are bought on order through generalist importers or as regrind, with long lead times and 25 kg-bag premiums. [ASSUMPTION · P1-RES §1]
- Distributors sell by 25 kg bag; best prices at 1 t (40 bags) or more; 100–500 kg can usually be bought from stock at a premium. [ASSUMPTION · F-RES]
- Recommended first stock: PP homopolymer (MFR 10–25), PP impact copolymer (MFR 10–20), HDPE injection (MFR 5–20), black and white masterbatch plus 2–3 colours, UV/HALS masterbatch for outdoor parts, in-house regrind plus one qualified recycled source; buffer 4–8 weeks of consumption (~2–5 t for one 110 t press on two shifts). [ASSUMPTION · P1-RES §4]
- Masterbatch at 600 DZD/kg and 2% let-down. [ASSUMPTION · report §8.2]
- Saudi Red Sea (Yanbu), Egypt (GAFTA) and Turkey/EU origins avoid Hormuz, so asking distributors for lot origin reduces exposure. [ASSUMPTION · P1-RES §3]
- Product ideas that depend on small lots of PC, POM, TPU/TPE or ABS, commodity products whose margin disappears at ~300+ DZD/kg resin, and any plan assuming Arzew PP before 2028 should be treated as kill triggers. [ASSUMPTION · P1-RES §4]
