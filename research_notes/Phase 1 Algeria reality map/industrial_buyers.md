# Phase 1: Industrial buyers other than personal care and detergents (demand-side map)

Research date: 2026-10-04. Data files: `/home/user/ghanoubenz/data/phase1_buyers_entities.csv` (84 entities) and `/home/user/ghanoubenz/data/phase1_buyers_signals.csv` (43 signals).

**Method caveat (read first).** WebFetch was blocked by the egress proxy for **every** domain I tried: ouedkniss.com, kompass.com, dnb.com, algerie-eco.com, tsa-algerie.com, dzair-tube.dz, radioalgerie.dz, algerie360.com, observalgerie.com, teamfrance-export.fr, managers.tn, maxtruder.com and cpi-worldwide.com. The session's shared web-search budget then ran out partway through the furniture searches. As a result:
- Everything below comes from search-engine snippets or from sourced items in the earlier notes (`customer_prospects.md`, `cost_inputs_market_prices.md`). Those items are marked "(prior notes)".
- Searches aimed at pain signals did not reach any Algerian forum, Ouedkniss or Facebook content. This applied to the French, English and Arabic queries ("pièces introuvable", MOQ, customs delays, "مستلزمات الألمنيوم", "لوازم السقي بالتقطير").
- I invented no company, contact or price. Rows that rest on background knowledge only (Alfapipe, Tosyali's pipe business, Sonatrach) are labelled ASSUMPTION in the CSV.

---

## 1. Aluminium/PVC joinery: who buys accessories and where is the pain?

### Takeaway
PVC joinery is industrialising fast. Cevital's Oxxo (BBA) can make 2.1M windows a year, and Izdihar PVC (Tiaret) opened in July 2025 with 117k units a year. Accessories are sold through Ouedkniss-active distributors such as Leader Aluminium (Boumerdès), against imported Italian and Turkish systems. This is the strongest structural fit for a 100–120 t press: glazing packers, end caps, drainage caps, corner keys. However, no unit-price or shortage evidence could be captured.

### Cited Findings
- **Oxxo (Cevital)**, Aïn Taghrout, BBA: 2.1M windows/yr (about 400k homes), 23 KraussMaffei twin-screw extruders on 19 profile lines, about 3,000 staff, and a target of 50% export revenue by 2025. — [Cevital: Oxxo capacity](https://www.cevital.com/oxxo-increased-its-production-capacity-of-profiles-for-the-window-plant/); [Algérie360](https://www.algerie360.com/oxxo-filliale-du-groupe-cevital-une-capacite-de-production-de-21-millions-de-fenetres/)
- **Izdihar PVC**, Zaaroura, Tiaret: PVC doors and windows, 117,000 units/yr, 712 MDA private investment, about 87 jobs, and a *claimed* 85% integration rate. A **metallic-hardware (quincaillerie) factory** was inaugurated the same day in the same zone; its name was not in the snippet. — [Algérie360](https://www.algerie360.com/pvc-lalgerie-mise-sur-2-nouvelles-usines-pour-passer-de-limport-a-lexport/); [La Nouvelle Tribune, Jul 2025](https://lanouvelletribune.info/2025/07/maghreb-un-pays-mise-sur-des-usines-pour-tourner-la-page-des-importations-de-pvc/)
- **Leader Aluminium**, Hammedi, Boumerdès (wilaya 35): Ouedkniss store selling door and window opening systems, aluminium accessories (the snippet names the brands "Dubral" and "Alupha"), PVC profiles, EPDM curtain-wall gaskets and false ceilings, with payment on delivery. Visible prices include 695 DA and 5,950 DA, but the items could not be identified. — [Ouedkniss store](https://www.ouedkniss.com/store/14372/leader-aluminium/accueil?lang=fr)
- **Master Italy**, an Italian maker of aluminium-joinery accessories since 1986, exhibited at Batimatec 2019 and says it has distributed in North Africa for more than 20 years. Branded imported systems are therefore the incumbent. — [Master Italy Batimatec PR](https://www.masteritaly.com/wp-content/uploads/2019/03/Communiqué-de-presse_FR_Batimatec.pdf)
- Import-policy history: when 851 products were suspended, finished aluminium joinery was pulled from the list at the last minute while PVC joinery stayed suspended. — [Algérie Eco](https://algerie-eco.com/?p=25944) (snippet; probably the 2018 measures)
- **Pain (weak):** a report says raw materials for aluminium joinery were taxed more than imported finished products. — [Algérie Eco, tag menuiserie](https://algerie-eco.com/tag/menuiserie/)
- Turkish PVC-extrusion line maker Maxtruder promoted its presence at Batimatec 2026 (3–7 May). — [Maxtruder news](https://maxtruder.com/en/news/details/113-03-05-2026-batimatec-expo-algeria)
- Secondary demand: Procamp advertises aluminium-joiner jobs in the energy/mining category ([Emploitic](https://emploitic.com/entreprises/procamp/offres-d-emploi/energie-mines-matiere-premiere/menuisier-aluminium-e07dde42915a959315c1c13d)). OTA tendered for joinery materials in June 2025 ([DZtenders](https://www.dztenders.com/en/archive/460131/fourniture-de-materiaux-de-menuiserie-bois-metallique-aluminium-et-vitrage)).
- A Saudi/UAE (CPC/Alumco) aluminium extrusion JV, 50,000 t/yr, was announced in 2008. I found no evidence that it was built. — [TradeArabia](https://www.tradearabia.com/news/IND_148917.html)

### Inferences
- **Verdict: GO, subject to field validation.** Glazing packers, profile end caps, drainage-slot covers and roller-shutter end caps are low-complexity, multi-cavity parts that suit a 100–120 t servo press. Buyers run from 1–2 large plants (Oxxo, Izdihar) down to hundreds of small joiners, who are reached through distributors like Leader Aluminium.
- The risk is **system-specificity**: accessories must fit specific profile series, whether local, Turkish or Italian. Start with universal consumables (packers, shims) before system-specific caps.
- Oxxo is probably locked into foreign system hardware. Treat it as a test buyer for packers, not as the anchor customer.

### Gaps
- No unit prices, MOQs or stated shortages for joinery accessories were found, because Ouedkniss and Facebook are blocked. An interview with Leader Aluminium and 3–5 Boumerdès/Algiers distributors is needed.
- I could not find a verified list of Algerian aluminium extruders or of the Izdihar sister hardware plant.
- The 2026 duty and DAPS status of joinery accessories is unknown.

---

## 2. Construction products and precast concrete

### Takeaway
The demand evidence is indirect. Precast and pipe plants exist (Cosider Canalisations, Trans-Canal Algeria), Holcim El-Djazaïr has entered ready-mix concrete, and online hardware stores sell spacers at 5.6–22.5 DA/pc retail. Rebar spacers remain the best freight-protected product, but no named spacer buyer has confirmed demand.

### Cited Findings
- **Cosider Canalisations** added a precast boundary-wall line and double-T slab moulds. — [CPI worldwide](https://cpi-worldwide.com/journals/artikel/64708) (snippet, 2019)
- **Trans-Canal Algeria** runs highly automated concrete-pipe manufacturing. — [CPI worldwide](https://cpi-worldwide.com/journals/artikel/46313) (title only)
- **Holcim El-Djazaïr** launches a concrete (béton) activity. — [Algérie Eco](https://algerie-eco.com/?p=239450) (headline only; date approximately 2026)
- Retail spacer prices on Algerian e-shops: 150 vertical spacers for 840 DA (about 5.6 DA/pc), 1,000 round 30/8-14 for 13,600 DA, and 600 horizontal 40-8/24 for 13,500 DA (about 22.5 DA/pc). — (prior notes) [mabricole.com.dz](https://mabricole.com.dz) / [assly.dz](https://www.assly.dz)
- Batimatec 2026 ran 3–7 May in Algiers, with exhibitors from about 15 countries and 40 start-ups. — [Algérie Eco](https://algerie-eco.com/?p=239715)

### Inferences
- **Verdict: GO for rebar spacers and formwork cones/plugs, sold through quincaillerie distributors and direct to precast plants.** Spacers are bulky and cheap per kg, so imports carry a high freight-to-value ratio, and retail prices leave headroom. The precast plants (Cosider) are direct buyers that need custom cover sizes, a plausible custom-dimension niche.
- The search turned up no buyer-pain signal in construction.

### Gaps
- No named precast element makers outside the Cosider group were found, and no named wholesale quincaillerie hubs (e.g. El Hamiz) were sourced.
- The Batimatec exhibitor list could not be retrieved.

---

## 3. Irrigation and agriculture

### Takeaway
The channel is fragmented and mostly made of distributors. Kompass lists PE-tube and hose distributors in Boufarik (Blida), Bordj Menaïel (Boumerdès), Algiers and Aïn Arnat (Sétif), plus a few declared drip makers (Anabib Plastiques, Medi Goutte, ISS, SIFAT for hoses). Imported branded drip products (Aster, Caudal, Irritec) are the incumbent. Fittings (start connectors, couplings, end plugs, hose connectors) are the natural B2B entry, sold as private label to distributors and tape extruders.

### Cited Findings
- Kompass irrigation listings: **Anabib Plastiques EURL** (Aïn Arnat; plastic irrigation elements and drip systems), **DripGlobe SARL** (Draria), **Irrinet SARL** (Boufarik; hoses and drip systems distributor), **Irriplast SARL** (Bordj Menaïel; PE tube distributor), **AITECH EURL** (Sidi M'Hamed), **SIFAT SARL** (Dar El Beïda; rubber-hose producer), **Tupol** (Aïn Arnat; PE tubes) and **Medi Goutte SARL** (Aïn Benian; "fabrication de tout type d'irrigation goutte à goutte"). — [Kompass irrigation](https://dz.kompass.com/a/materiel-d-irrigation-et-d-arrosage/48140/); [Kompass drip](https://dz.kompass.com/a/systemes-d-irrigation-goutte-a-goutte-pour-l-agriculture/4814010/); [Pagesmaghreb](https://www.pagesmaghreb.com/entreprise/medi-goutte-sarl-353437/alger-4/algerie)
- An Algiers-based producer has offered drip tape (1,500 m and 3,050 m rolls, 10/20 cm spacing) since April 2014. — [Espaceagro](https://www.espaceagro.com/gaine-goutte-a-goutte/expGB-gaine-goutte-a-goutte.html)
- **Groupe Chiali** (Sidi Bel Abbès) exports PE tubes and rebar to Mauritania. — [Algérie Eco, 22 Aug 2024](https://algerie-eco.com/2024/08/22/sidi-bel-abbes-exportation-de-tubes-de-polyethylene-et-de-rond-a-beton-vers-la-mauritanie/)
- Foreign incumbents trading in Algeria: **Aster** (Italy), whose exhibitor profile says it trades in Algeria ([GreenTech](https://www.greentech.nl/amsterdam/exhibitors/aster-s-r-l)), and **Caudal** (Spain) ([GreenTech](https://www.greentech.nl/amsterdam/exhibitors/caudal)).
- AGM began producing the first Algerian centre pivot in May 2024 ([Radio Algérie](https://news.radioalgerie.dz/fr/node/45427)), and Condor has a solar pivot pilot in El Oued ([Team France Export](https://www.teamfrance-export.fr/infos-sectorielles/14979/14979-pivot-solaire-pour-lirrigation-made-in-algeria-by-groupe-condor)). (prior notes)
- SIPSA-Filaha 2026 (18–21 May) had 850 exhibitors from 40 countries and about 250 international brands, with more than 40,000 visitors expected. — [Radio Algérie](https://news.radioalgerie.dz/fr/node/86446)
- Drip-line price reference: 12 mm PE with integrated emitters every 30 cm costs 93.63 DA/m (CYPE estimator). — (prior notes) [prix-construction](http://www.algerie.prix-construction.info/renovation/VRD_et_amenagements_exterieurs/Espaces_verts_et_mobilier_urbain/Arrosage/Tuyauterie_d_arrosage_goutte-a-goutte.html)

### Inferences
- **Verdict: GO / INVESTIGATE.** Start connectors, couplings, tees, end plugs, hose connectors and greenhouse clips are simple PP/PE parts suited to 8–32-cavity tools on a 100–120 t press. The buyers are tape/tube extruders (Anabib, Tupol, the Algiers tape maker, SIFAT for hoses) and distributors (Irrinet, Irriplast).
- **Clusters:** Mitidja (Boufarik), East Algiers/Boumerdès (Dar El Beïda, Bordj Menaïel) and Sétif–Aïn Arnat. The end demand is in Biskra and El Oued (see prior notes), but the channel buyers sit in the north.
- Do not build emitters (labyrinth or pressure-compensating) at first. They need precision tooling and compete with Italian and Spanish brands.
- Sales are seasonal and peak before planting campaigns.

### Gaps
- No DZD prices were found for drip fittings and no shortage signals, because Ouedkniss and Facebook were unreachable.
- I could not confirm which Kompass-listed firms actually extrude or mold, versus distribute.
- No greenhouse builders were found (the search returned only French firms).

---

## 4. Furniture (office, school, home)

### Takeaway
I identified named makers (Kompass and company sites): Divindus AMM (public, Bab Ezzouar, series furniture for administrations and schools), SM Mobilier and Dhikra Office (Boumerdès), EACIM (Rouiba, metal and office furniture), Louai Meuble, Vecor Design (Algiers) and MAM (Blum's representative). The sector is growing against imports but has low mechanisation. Glides, tube end caps, cam covers and levelling feet fit the press well. The search budget ran out before Tizi Ouzou, Bordj Menaïel, Blida/Beni Mered or Sétif could be covered.

### Cited Findings
- **Divindus AMM** (Bab Ezzouar) makes industrial furniture and joinery in series for administrations, local authorities and educational institutions. **SM Mobilier** (Ouled Moussa) makes office, kitchen and storage furniture. **Dhikra Office Manufacturing** (Ouled Heddadj) makes high-end office furniture. **EACIM Algérie** (Rouiba) does metal fabrication and office furniture. Also listed: DESKTRO, MEUBLEA, IAAMAR Equipement and NEWTECH PRO. — [Kompass office furniture](https://dz.kompass.com/a/mobilier-de-bureau/15320/); [Kompass producers](https://dz.kompass.com/x/producer/a/mobilier-de-bureau/15320/)
- **Louai Meuble** calls itself the largest furniture maker in Algeria and has an office range. — [louaimeuble.com](https://www.louaimeuble.com/Bureautique)
- **Vecor Design** (founded 2005, Algiers) makes all types of furniture. — [vecordesign.com](https://vecordesign.com/)
- **MAM – Manufacture Algérienne du Meuble** makes kitchens, dressing rooms and bathrooms, and is Blum's representative in Algeria. — [mam-algeria.com](https://mam-algeria.com/societe/)
- Local furniture is gaining against imports, but the sector is handicapped by manual work and old machinery. — (prior notes) [Algérie360](https://www.algerie360.com/le-meuble-local-a-la-conquete-dun-marche-domine-par-la-concurrence-etrangere-une-activite-florissante/)

### Inferences
- **Verdict: GO, through a distributor and direct to the 5–10 largest makers.** School and administration furniture (Divindus-type tender volumes) and metal office furniture (EACIM) need chair tips, tube plugs and glides in volume. Colour-matched cam covers are a local-service advantage.
- The many small workshops likely buy hardware from quincailleries; this is an inference that needs an interview.

### Gaps
- No sourced evidence for the Tizi Ouzou, Bordj Menaïel, Beni Mered or Sétif clusters. No hardware wholesaler names and no "patin" or "embout" DZD prices.

---

## 5. Electrical (accessories, cables, wholesalers, panel builders)

### Takeaway
Cable and transformer makers (ENICAB in Biskra, ENEL in Azazga, Sitel) and online wholesalers (SOGEDIM, Elecmarket, Mabricole) are identified. Electrical boxes are already molded locally (HAOUAS brand) and cable ties are Turkish imports. The new state molder GPI explicitly lists cable-industry components in its scope.

### Cited Findings
- ENICAB makes about 20,000 t/yr of copper cable and 2,000 t/yr of rail cable, and has export plans. — [Dzair Tube, 13 Jun 2025](https://www.dzair-tube.dz/en/enicab-boosts-rail-sector-with-2000-tons-of-annual-cable-production-eyes-regional-export-expansion)
- ENEL Azazga becomes 100% Sonelgaz-owned from Q1 2026. — [Algérie Eco](https://algerie-eco.com/?p=231616) (prior notes)
- Shelf origin: OZTURK (Turkish) cable ties at 450 DZD per 100, and local HAOUAS boxes next to Spanish FAMATEL. — (prior notes) [mabricole](https://mabricole.com.dz/fr/fixation/jeu-de-colliers-de-serrage-en-plastique-100-200mm-250pcs-onsite-1845)
- GPI's scope includes cable-industry components, fridges and air conditioners. — [Algérie360](https://www.algerie360.com/gpi-tissemsilt-pieces-plastiques-industrie-auto/); [Algérie Eco](https://algerie-eco.com/?p=327988)
- Cevital is partnering with a Brazilian group to make electric motors in Algeria (headline only). — [TSA](https://www.tsa-algerie.com/cevital-sassocie-avec-un-groupe-bresilien-pour-produire-des-moteurs-electriques-en-algerie/)

### Inferences
- **Verdict: INVESTIGATE.** Commodity boxes and ties are already contested by local and Turkish supply. Niches still open are cable end caps and reel parts for ENICAB and Sitel, cable glands (higher tooling difficulty), conduit saddles, and private label for online wholesalers.

### Gaps
- Panel builders, the El Eulma wholesale cluster and AMC-type meter makers could not be searched before the budget ran out.

---

## 6. Appliances and HVAC

### Takeaway
The demand is large and integration-driven, and it sits in the BBA and Sétif clusters: Condor, Condor–Hisense (2M ACs a year planned), Géant (fridge integration 70%), Samha (AC integration target only 30–40%), Samsung/Sinova and Brandt. But the big OEMs mold in-house (Condor, Brandt), and GPI now targets appliance parts. ENIEM shows the clearest pain (stockouts, CKD delays), but also the highest payment risk.

### Cited Findings
- **ENIEM** signed Turkish (heaters, more than 60% integration by June 2025) and Chinese (ACs, a CKD order for 30,000 units) partnerships. The AC start slipped from August to December 2024 because of admin and Red Sea logistics delays, and the 2025 integration target is 80%. — [Algérie Eco, 21 Nov 2024](https://www.algerie-eco.com/2024/11/21/leniem-a-signe-des-accords-avec-deux-entreprises-chinoise-et-turque/)
- ENIEM earlier made a technical stop because of raw-material stockouts in all workshops and a lack of bank credit (1,700 staff sent on leave), and production fully stopped in 2023. Wages went unpaid from Oct 2023 to Jan 2024 and debt is about 5 bn DA. — [Algérie Eco](https://algerie-eco.com/?p=115716); [TSA](https://www.tsa-algerie.com/leniem-a-larret-retour-sur-la-debacle-dun-ex-fleuron-de-lindustrie-algerienne/). The minister pledged its revival in Oct 2025. — [Dzair Tube](https://www.dzair-tube.dz/en/minister-ali-aoun-affirms-commitment-to-eniems-revival-during-tizi-ouzou-visit)
- **Géant** is adding two units (ACs, fridges) to its six in BBA, with 70% fridge integration and 263 products. — [Dzair Tube](https://www.dzair-tube.dz/en/geant-electronics-expands-production-with-two-new-units-for-air-conditioners-and-refrigerators-in-january). The snippet dates are ambiguous: the page header says 2026 and the content says Jan 2024.
- **Condor–Hisense** plans 2M ACs a year in BBA, 80% for export, with USD 200M investment. — [Algérie Eco](https://algerie-eco.com/?p=211059)
- **Samha** (Guedjel, Sétif) has about 4,000 staff and 5M units/yr capacity, with an AC integration target of 30–40%. — [Algérie Eco](https://algerie-eco.com/?p=183402); [Algérie360](https://www.algerie360.com/lusine-de-samha-a-setif-produira-bientot-des-smart-tv-et-3d/). Samsung and Sinova planned an AC unit in Sétif. — [Radio Algérie](https://news.radioalgerie.dz/fr/node/37607)
- Raylan (Annaba) is described as an importer of Hitachi and Electrolux products. — [AroundDeal](https://www.arounddeal.com/c/raylan-algrie/v2hrycjcxa). I found no source on Stream System.

### Inferences
- **Verdict: INVESTIGATE, as secondary supplier.** Target the purchasing and local-integration managers at Géant, Samha/Sinova and ENIEM for small parts (knobs, clips, condensate fittings, cable clamps, heater parts) and for AC-installer consumables. With ENIEM, insist on advance payment.
- AC-installer consumables (condensate pump parts, wall-duct covers, drain fittings) may be an easier aftermarket channel than the OEMs. I found no source for them.

### Gaps
- Stream System, AC installer networks and appliance spare-parts shortages remain unverified.

---

## 7. Automotive (noted only), solar, oil & gas, food and industrial

### Takeaway
In automotive, the state has pre-assigned local plastics: GPI Tissemsilt was inaugurated on 24 Sep 2026, and imports of auto plastic parts it can make are banned from 1 Jan 2027. In solar, module plastics arrive embedded in Chinese imports. In oil & gas, demand for thread protectors is plausible but **unverified**. For food processors I found no evidence.

### Cited Findings
- GPI (Holding ACS) in Khemisti, Tissemsilt: 251,000 parts/yr for about 200,000 vehicles, 40% integration rising to 70%, and 300 direct jobs. — [ObservAlgérie, 25 Sep 2026](https://observalgerie.com/2026/09/25/economie/lalgerie-annonce-la-fin-de-limportation-des-pieces-plastiques-pour-voitures/); [Horizons, Apr 2026](https://www.horizons.dz/2026/04/sifi-ghrieb-a-tissemsilt-la-relance-de-lindustrie-automobile-saccelere/)
- Stellantis Tier-1s (SAREL, Sigit/Siplast in Sétif, IDE-NET, Formfleks, Ghazal, Megnouche) were covered in the prior notes. — [Team France Export: Sigit–ENPC Sétif](https://www.teamfrance-export.fr/infos-sectorielles/39583/39583-partenariat-sigit-enpc-creation-dun-groupement-industriel-a-setif)
- Algeria imported 850 MW of Chinese PV panels in H1 2025. — [Algérie Eco](https://algerie-eco.com/2025/08/10/algerie-850-mw-de-panneaux-solaires-chinois-importes-au-premier-semestre-2025/). Local module makers are Zergoun (Ouargla) and Aurès Solaire (Batna) (prior notes).
- A search for Algerian thread protectors ("protecteur filetage", Alfapipe) returned only patents.

### Inferences
- **Automotive: KILL for now.** GPI plus Tier-1 incumbents, IATF-type requirements and the state-champion preference leave little room. Reconsider Tier-2 clips and grommets only after 2027.
- **Solar: INVESTIGATE (low).** The only fits are cable clips and MC4 dust caps for EPCs, and the volume is unclear.
- **Oil & gas thread protectors: INVESTIGATE.** API-spec protectors are usually supplied with the pipe, which is an assumption. Call the pipe mills (Alfapipe, Tosyali; existence only) before investing in tooling.
- **Food-processor spares: no evidence; KILL as a lead segment.** Treat it as an opportunistic custom-part service.

### Gaps
- No evidence on EPC/installer names, Sonatrach protector sourcing, food-plant maintenance buyers or industrial equipment makers beyond HydroTech DZ (Algiers start-up, [VC4A](https://vc4a.com/ventures/hydrotech-dz-industrial/)).

---

## 8. Cross-sector summary: GO / INVESTIGATE / KILL

### Takeaway
GO: joinery consumables, rebar spacers and formwork parts, drip and hose fittings, furniture glides and caps. INVESTIGATE: appliance secondary supply, electrical niches, oil & gas protectors, solar clips. KILL: automotive (near term), food spares, closures. The biggest unknown everywhere is **field-level pain and price**, which online research could not reach.

### Cited Findings
- State policy favours integration and import substitution, delivered through state champions (GPI) and through integration targets at private OEMs. — [Radio Algérie: Rekkache on subcontracting](https://news.radioalgerie.dz/fr/node/79508); [ObservAlgérie](https://observalgerie.com/2026/09/25/economie/lalgerie-annonce-la-fin-de-limportation-des-pieces-plastiques-pour-voitures/)
- Fairs that serve as target lists: Batimatec (May; [Algérie Eco](https://algerie-eco.com/?p=239715)), SIPSA-Filaha (May; [Radio Algérie](https://news.radioalgerie.dz/fr/node/86446)), and ALGEST/SANIST (prior notes).

### Inferences
- Interview priority for Phase 2: Leader Aluminium and two other Boumerdès/Algiers joinery accessory distributors; Irrinet (Boufarik), Irriplast (Bordj Menaïel), Anabib/Tupol (Aïn Arnat) and SIFAT; Divindus AMM, EACIM and SM Mobilier; two or three quincaillerie wholesalers for spacers; purchasing at Géant and Samha.
- Questions to ask in each interview: current origin (China, Turkey, Italy, local), unit price in DZD, lead time and MOQ pain, any stock-outs in the last 12 months, custom-dimension needs, and payment terms.

### Gaps
- No pain or price evidence could be gathered from Ouedkniss, Facebook or forums. A further desk pass needs either fetch access or a larger search budget. Otherwise, phone and field interviews are required.
