# Phase 7: Field validation plan (calls, visits, samples, measurements, GO/WAIT/KILL rules, 4-week itinerary)

Prepared 2026-10-04 from repository files only. No new web research was done.

**Sources used**
- `data/entities.csv`
- `data/funnel_scores.csv` (stages TOP20 / TOP50)
- `data/top20_economics.csv`
- `data/machine_comparison.csv`
- `data/opportunities_master.csv`
- `model/economics.py`, used only to compute the top-50 thresholds with the same formula as the top-20 file
- `research_notes/Phase 2-8/p2_*.md` and `p3_buyer_behavior.md`
- `research_notes/Phase 1 Algeria reality map/*.md`
- `research_notes/Algeria injection molding feasibility/industry_map_subcontractors_moldmakers.md`, `resin_supply.md` and `customer_prospects.md`

**Ground rules for the founder (read first)**
1. **Every contact below was copied exactly as recorded in the files.** All of them came from search-engine snippets of directories or company pages. None has been dialled. Re-dial and confirm each one, and correct the files if a number is wrong. Where the files hold no phone or email, the entry says **"no public contact found"**. In that case, use the directory or Facebook/Ouedkniss page named in the files, or ask for an introduction.
2. **No company in this plan was invented.** Where a cluster has no named firm in the files (El Eulma wholesalers, Hammedi neighbours, Beni Mered furniture-hardware shops, Biskra dealers, car-parts traders), the plan gives the street or zone type and says **"names to be collected on site"**.
3. **Interview method.** Use the 16-question behavioral interview in `p3_buyer_behavior.md` §7 (EN/FR/darja): questions 1–8 are the core, and 9–16 are asked if time allows. The 3–5 company-specific questions below are **added** to that script; they do not replace it. Score every interview with the p3 rule:
   - **Hot:** they hand over a part or drawing, give a unit price and annual quantity, report a stock-out in the last 12 months, and name who pays and who approves.
   - **Warm:** they describe pain, but there is no part or quantity yet.
   - **Cold:** opinions only.

   Always record **who can veto** and **how they pay**.
4. **Record every answer** in the database fields:
   - known_buyers, current_supply_source, country_of_origin, pain_type, pain_confidence;
   - observed_price_dzd (with price basis: per pc / per 100 / per 1,000, ex- or incl. VAT, retail or wholesale);
   - moq, lead_time, demand_frequency;
   - next_validation_action.

   A price written down from a visible invoice, price tag or e-shop listing = **VERIFIED**. A price someone states = **STRONG SIGNAL**. A price someone guesses = **WEAK SIGNAL**.
5. **Bring to every visit:**
   - the supplier administrative file (RC, NIF, NIS, article d'imposition, extrait de rôle, CNAS, CASNOS), which p3 §1 and §5 give as the standard file;
   - a photo or video of the intended press and molds, if any;
   - a tape, a caliper and numbered zip bags.
6. **Product IDs** follow `funnel_scores.csv`. TOP20 = the 20 lead products. TOP50 = the 18 further candidates still alive.

### Product legend (TOP20 first, then the key TOP50 items used below)

| ID | Product | Stage | Min press (t) |
|---|---|---|---|
| JC-26 | Horizontal rebar spacer chair 40-8/24, 50-8/24 | TOP20 | 100 |
| JC-24 | Rebar spacer wheel 30 mm cover, rebar 8–14 | TOP20 | 120 |
| JC-40 | Mesh clip-on spacer ("étoile") | TOP20 | 120 |
| JC-34 | Tile-levelling clips (consumable) | TOP20 | 100 |
| JC-02 | Glazing bridge packer with drainage channel | TOP20 | 120 |
| JC-16 | Fly-screen frame corner 7×17 / 10×20 | TOP20 | 80 |
| JC-36 | Pipe clip "collier atlas" Ø12–40 | TOP20 | 80 |
| JC-13 | Drainage slot cover, colour-matched | TOP20 | 80 |
| JC-30 | Formwork cone for 22 mm tie-rod tube | TOP20 | 80 |
| OS-002 | IRL conduit coupler 16–25 mm | TOP20 | 80 |
| OS-010 | Plasterboard butterfly anchor 8 mm (PA6) | TOP20 | 100 |
| CL-003 | Colour-matched short-run flip-top service 24/410 & 28/410 | TOP20 | 120 |
| IF-39 | Round tube insert / chair-leg cap 22/25 mm | TOP20 | 80 |
| IF-40 | Square/rect tube insert 20×20, 25×25, 20×40 | TOP20 | 80 |
| IF-07 | Figure-8 end closure 16 mm | TOP20 | 100 |
| IF-08 | End plug 16 mm (tape & dripline) | TOP20 | 100 |
| OS-009 | Hammer-fix anchor sleeve 8×80 (PA6) | TOP20 | 100 |
| OS-084 | Body blanking plugs / grommets | TOP20 | 80 |
| IF-01 | Drip-tape start connector 16/17 mm (body) | TOP20 | 80 |
| IF-04 | Barbed straight coupling 16 mm | TOP20 | 80 |
| JC-17 | Fly-screen spring/fixation clips | TOP50 | 80 |
| IF-02 / IF-03 / IF-05 / IF-06 / IF-20 | Lock nut / tape-tape coupling / barbed tee / barbed elbow / layflat take-off | TOP50 | 80–100 |
| IF-42 / IF-46 / IF-47 / IF-48 / IF-49 | Nail-on glide / cam cover / screw cover / shelf pin / bed-slat holder | TOP50 | 80–100 |
| CL-001 / CL-007 / CL-013 | Flip-top 24/410 stock / plain screw cap 24/410 / orifice reducer | TOP50 | 80–100 |
| OS-039 / OS-051 / OS-052 | Split-AC condensate elbow / push-over pipe end cap / threaded protection cap | TOP50 | 80–100 |
| JC-07 | Shutter guide-rail entry funnel | TOP50 | 80 |

---

## A. Call list: 50 companies

### How the list is ordered
- **Wave 1 (Week 0, 5–8 Oct): calls 1–36.** These are the buyers with the highest expected pain, plus the services that unlock buyer lists. Book field meetings from these calls.
- **Wave 2 (same week, in parallel): calls 37–50.** These are the suppliers, mold makers, machine dealers, the customs broker and the bank.

### Index

| # | Company | City / wilaya | Type | Contact as recorded |
|---|---|---|---|---|
| 1 | Founder's shampoo-maker contact | UNKNOWN (not given to researchers) | buyer | via founder; no public contact found |
| 2 | SARL SIPEM | ZI Oued Smar (El Harrach), Algiers | competitor / supplier | no public contact found (Ouedkniss ad only) |
| 3 | Farfasha cosmétique Algérie | UNKNOWN | buyer | Facebook page https://www.facebook.com/farfasha1616/ |
| 4 | Volume cosmétique Algérie | UNKNOWN | buyer | Facebook page https://www.facebook.com/VolumeAlgerie/ |
| 5 | Algiers shampoo/shower-gel start-up seeking component suppliers (company name not shown in files) | Algiers | buyer | Kompass lead https://fr.kompass.com/lead/0005886583/ |
| 6 | Labonedjma | Larbaâ, Blida | buyer | no public contact found |
| 7 | Dermal Group | UNKNOWN | buyer (contract filler) | no public contact found |
| 8 | Laboratoires Sabrinel | UNKNOWN | buyer (contract filler) | no public contact found |
| 9 | Univers Détergent (Aigle, Top) | Algiers (HQ) | buyer | no public contact found |
| 10 | PAFIX emballage | Draria, Algiers | supplier / competitor (trader) | Facebook page https://www.facebook.com/people/PAFIX-emballage/100075973279239/ |
| 11 | SARL PAP PLAST Emballages | Algiers | service / channel (bottle blower) | Facebook page https://www.facebook.com/PAP.PLAST.EMBALLAGES/posts |
| 12 | Anabib Plastiques EURL | Aïn Arnat, Sétif | buyer (drip maker) | no public contact found (Kompass listing only) |
| 13 | Medi Goutte SARL | Aïn Benian, Algiers | buyer (drip maker) | no public contact found (Pagesmaghreb listing https://www.pagesmaghreb.com/entreprise/medi-goutte-sarl-353437/alger-4/algerie) |
| 14 | DripGlobe Systèmes d'Irrigation SARL | Draria, Algiers | buyer (drip maker) | no public contact found (Kompass listing only) |
| 15 | SARL Union B et CH Plastique (brand ISS) | UNKNOWN | competitor / buyer | website contact page https://agro-iss.com/contact/ |
| 16 | Irrinet SARL | Boufarik, Blida | buyer (distributor) | no public contact found (Kompass listing only) |
| 17 | Irriplast SARL | Bordj Menaïel, Boumerdès | buyer (distributor) | no public contact found (Kompass listing only) |
| 18 | Groupe STPM Chiali | Zone Industrielle Voie A, Sidi Bel Abbès | buyer / competitor | tel. +213 (0)48 55 11 90, info@stpm-chiali.com (directory snippet, "re-check"); www.stpm-chiali.com |
| 19 | Leader Aluminium | Hammedi, Boumerdès (35) | buyer (joinery distributor) | Ouedkniss store (payment on delivery) https://www.ouedkniss.com/store/14372/leader-aluminium/accueil?lang=fr |
| 20 | Oxxo (Cevital group) | Aïn Taghrout, Bordj Bou Arréridj | buyer | website https://www.cevital.com/oxxo-2/ (no phone recorded) |
| 21 | Izdihar PVC | Zaaroura industrial zone, Tiaret | buyer | no public contact found |
| 22 | Cosider Canalisations | UNKNOWN | buyer (precast) | no public contact found |
| 23 | Trans-Canal Algeria | UNKNOWN | buyer (concrete pipe) | no public contact found |
| 24 | SOGEDIM | UNKNOWN (e-shop) | buyer (wholesaler) | e-shop https://sogedim.net |
| 25 | Mabricole | UNKNOWN (e-shop) | buyer (wholesaler/e-shop) | e-shop https://mabricole.com.dz |
| 26 | Assly | UNKNOWN (e-shop) | buyer (wholesaler/e-shop) | e-shop https://www.assly.dz |
| 27 | EACIM Algérie SARL | Rouiba, Algiers | buyer | no public contact found (Kompass listing only) |
| 28 | Divindus AMM | Bab Ezzouar, Algiers | buyer (public) | no public contact found (Kompass listing only) |
| 29 | SM Mobilier (Salhi Mohamed Mobilier) | Ouled Moussa, Boumerdès | buyer | no public contact found (Kompass listing only) |
| 30 | Sonatrach (spare-parts localisation / local-supplier pre-qualification) | Algiers HQ; Hassi Messaoud ops | buyer | no public contact found |
| 31 | Sonelgaz group (local content; owner of ENEL Azazga) | Algiers HQ | buyer | no public contact found |
| 32 | Sider El Hadjar, seamless-tube unit (TSS) | El Hadjar, Annaba | buyer | no public contact found |
| 33 | Samha Home Appliance | Guedjel, Sétif | buyer | no public contact found |
| 34 | Legacy Exhibitions (organiser, Cosmetica North Africa) | SAFEX, Pins Maritimes, Algiers | service | Ashraf Ziri +213 561 576 339; ashraf@legacyexb.com (published by JETRO/fair listings) |
| 35 | BASTP (Bourse Algérienne de Sous-traitance et de Partenariat) | Algiers | service (ALGEST co-organiser) | website algest.dz (no phone recorded) |
| 36 | SNK Plastic | Rouiba, Algiers | competitor / service (subcontract molding) | +213 784 20 31 86; contact@snkplastic.com |
| 37 | POLYCHIMICAL SARL | Z.A.C partie 02 portion 28, Hamadi Krouma, Skikda | supplier (resin) | tel/fax +213 38 93 18 34; mobile 0660 57 14 36; commercial@polychimical.com (from search snippet; not called) |
| 38 | AB POLYMERS SARL | Es Senia, Oran | supplier (resin) | no public contact found |
| 39 | DISTRIPOL SARL | Zéralda, Algiers | supplier (resin) | no public contact found |
| 40 | HIMAPLAST SARL | Bou Ismaïl, Tipaza | supplier (masterbatch, fillers) | no public contact found |
| 41 | SARL TAIF MASTER BATCH | Zone d'activité Beni Tamou, Blida | supplier (masterbatch) | no public contact found (dzentreprise.net listing) |
| 42 | ZEROUNI MOLDS / Ets Zerouni El Hadj | Rue Sidi Abbad, Tassala El Merdja, Algiers | service (mold maker) | +213 551 67 91 45 |
| 43 | FMPI (Fabrication de Moules et Pièces Industrielles) | Khemis El Khechna (site) / Kouba (office) | service (mold maker) | +213 559 268 303; info@fmpi-dz.com |
| 44 | Precision Industry (SARL) | Ouled Moussa, Boumerdès | service (mold maker) | contact@precisionindustry-dz.com; +213 563 05 40 19; 0770 00 44 66 / 0770 00 44 88 (directory) |
| 45 | CFM Engineering | El Eulma, Sétif | service (mold maker) | no public contact found (website https://cfm-engineering.com/ only) |
| 46 | AFC Industry Algérie (SARL), Yizumi | Cité ZHUN, Jolie Vue, Kouba, Algiers | supplier (machine dealer) | Ouedkniss store 8607; Facebook AFC.Industry.Algerie; LinkedIn (no phone/email recorded) |
| 47 | Plasticolor Group, Chen Hsong | Algiers | supplier (machine dealer) | contact person listed on Chen Hsong service-network page (chenhsong.com/service-network); no phone/email recorded |
| 48 | 2M Expert Algeria, Cosmos | ZI Oued Smar, Voie CW118, Algiers | supplier (machine + raw-material dealer) | algerie@2m-expert.com; 023 93 02 98; 0550 65 00 75 |
| 49 | Customs broker (transitaire): request for a tariff readout | to be chosen; no broker is named in the files | service | no public contact found. Get a referral from #46 or #48 (both import machines) or from #50 |
| 50 | Founder's domiciliation bank | name not in files | service (bank) | no public contact found (founder's own bank) |

**Reserve list (call if a slot frees up):**
- Groupe ECI and White Industry (contract fillers, WEAK).
- Tupol (Aïn Arnat, Kompass).
- HM PLAST (Guerouaou, Blida; Facebook https://www.facebook.com/HM.PLAST.BLIDA/).
- SOLOPLAST (El Eulma).
- Laboratoires SPIC (Mohammadia; Kompass).
- Elecmarket-dz (https://elecmarket-dz.com).
- Holcim El-Djazaïr.
- Géant Electronics and Condor–Hisense (BBA).
- ENICAB (Biskra).
- EURL Eurowin (Ouedkniss store https://www.ouedkniss.com/store/10992/eurl-eurowin/).
- MIRAF Industrie (+213 550 41 90 77; contact@miraf.dz).
- Cumnewtec (contact@cumnewtec.com; +213 552 19 67 54).
- BRUM Algérie and El Kader Plast (recycled PP/HDPE).

### A.1 Personal care and closures (calls 1–11)

**1. Founder's shampoo-maker contact.** Buyer. Products: CL-003, CL-001, CL-007, CL-013.
- **Purpose:** settle the only direct pain report in the whole project. Was it a mold-cost, MOQ, neck, colour or hinge problem? Bring home the bottle and its cap.
- **Questions** (p2_closures §6):
  1. Which closure exactly: flip-top, disc-top, push-pull or screw? Can I take a physical sample with its bottle?
  2. Which neck finish (24/410, 28/410, 28/400, other)? Who blows the bottle, and is the neck their standard or made for you?
  3. Annual volume per reference? Lot size per order? Number of colours? How many SKUs use this cap?
  4. Which local suppliers did you ask (names)? What exactly did each say: "no mould", "mould costs X", "minimum Y", "can't match colour" or "won't do hinge"?
  5. What do you use today, at what price per 1,000, MOQ and lead time? Would you co-fund a mould (US$8–12k) for exclusivity or a lower price? Target DZD price and payment terms?

**2. SARL SIPEM** (Oued Smar). Competitor / supplier. Products: CL-003, CL-001, CL-007, CL-013.
- **Purpose:** the KILL test for closures. Does the only local maker that claims dispenser caps already offer hinged flip-tops at 5–10k MOQ? Call as a prospective buyer.
- **Questions:**
  1. Do you make hinged flip-tops in 24/410 and 28/410, with in-mould closing or post-mould closing? Disc-tops? Push-pulls?
  2. Which stock moulds do you own (neck finishes, cavities)? MOQ per reference and per colour; can you colour-match to a sample?
  3. Price per 1,000 ex-VAT for a 28/410 flip-top in white, and in a custom colour? Lead time for stock items and for a new customer mould?
  4. Are your "pompettes" moulded and assembled in-house, or imported? Who makes your moulds, and at what price?
  5. Presses and tonnage? Are you full, and would you subcontract overflow?

**3. Farfasha cosmétique.** Buyer (small brand). Products: CL-003, CL-001, CL-013.
- **Purpose:** test small-brand MOQ and colour pain, and willingness to pay.
- **Questions:**
  1. Last closure lot bought: type, neck, supplier (trader, blower or import), price per 1,000, MOQ?
  2. Do you buy bottle and cap as a set from one supplier?
  3. Last stock-out or colour you could not get, and what did it cost you?
  4. Would you pay +30–50% over the China price for a 5k MOQ colour-matched cap delivered in 10 days? (This is the funnel's next action.)
  5. Payment: cash, cheque or 30 days?

**4. Volume cosmétique.** Buyer (small brand). Products and purpose as #3.
- **Questions:** the same five as #3. In addition, list every closure SKU you use and the neck of each.

**5. Algiers shampoo/shower-gel start-up (Kompass lead 0005886583).** Buyer. Products: CL-003, CL-001.
- **Purpose:** the only public "seeking component suppliers" lead in the files.
- **Questions:**
  1. Which components are you still looking for, and why have you not found them locally?
  2. Neck finish, volume per year and colours?
  3. What quotes have you received (who, price, MOQ)?
  4. Who decides and who pays? What first trial lot size?

**6. Labonedjma** (Larbaâ). Buyer, 600+ SKUs. Products: CL-003, CL-001, CL-007, CL-013.
- **Purpose:** a mid-size leader with many SKUs, so many colours and short runs.
- **Questions:**
  1. How many closure references do you use, and which necks and types?
  2. Which closures are imported, and from which country and supplier?
  3. Smallest lot per colour that suppliers accept? Last stock-out?
  4. Who approves a new closure (QA test, line trial), and how long does it take?
  5. Payment terms with packaging suppliers?

**7. Dermal Group.** Buyer (contract filler). Products: CL-003, CL-001, CL-013.
- **Purpose:** an aggregator of small brands, and the best potential volume pool for colour short runs.
- **Questions:**
  1. Who supplies closures for client brands: you or the client?
  2. How many brands and colours per year? Typical lot per colour?
  3. Where do flip-tops come from today, at what price per 1,000 and lead time?
  4. Would you stock a local stock-mould flip-top range?

**8. Laboratoires Sabrinel.** Buyer (contract filler / hair care). Products, purpose and questions as #7.
- Also ask: which hair-oil necks need orifice reducers (CL-013), and where do the reducers come from?

**9. Univers Détergent.** Buyer; has an "acheteur technique". Products: CL-007, CL-013 (and CL-010 measuring cap, which is outside the top 50).
- **Purpose:** a detergent maker with a formal buyer, to learn the group qualification path.
- **Questions:**
  1. Closure types per product line, and the neck of each?
  2. Which are imported, and from where? Last import delay?
  3. Where do measuring/dosing caps come from?
  4. What must a new local closure supplier submit (file, samples, tests), and who signs off (QA or purchasing)?
  5. Payment days by transfer?

**10. PAFIX emballage.** Trader of imported cosmetic packaging. Products: CL-001, CL-003, CL-007, CL-013.
- **Purpose:** get the first DZD price ladder for closures. No DZD closure price exists anywhere in the files.
- **Questions:**
  1. Price per 1,000 for 24/410 and 28/410 flip-tops, disc-tops and plain screw caps, in white and in colour?
  2. MOQ, origin and lead time?
  3. Best-selling references and recent stock-outs?
  4. Would you resell a local flip-top, and at what buy price?

**11. PAP PLAST Emballages.** Channel (EBM bottle blower). Products: CL-001, CL-003, CL-007.
- **Purpose:** find out the necks actually blown in Algeria and the cap source behind bottle+cap sets.
- **Questions:**
  1. Which neck finishes do you blow (24/410, 28/410, 28/400, own)?
  2. Do you sell caps with bottles? Who makes or imports them, and at what price?
  3. Which closure requests can you not fill?
  4. Would you co-sell a neck-matched local cap?

### A.2 Irrigation (calls 12–18)

**12. Anabib Plastiques EURL** (Aïn Arnat). Buyer (drip tape/elements maker). Products: IF-01, IF-02, IF-03, IF-04, IF-05, IF-06, IF-07, IF-08, IF-20.
- **Purpose:** find out whether tape makers bundle imported fittings, and whether they run short before the season.
- **Questions** (funnel next action):
  1. Which fittings do you sell with your tape? Origin, DZD per 1,000, MOQ?
  2. When did you last run out, and of which size?
  3. Your order months for fittings, and payment terms?
  4. Tape OD and wall (16/17 mm), and any fit problems with imported fittings?
  5. Would you take private-label fittings, and in what yearly quantity?

**13. Medi Goutte SARL** (Aïn Benian). Buyer. Products as #12.
- **Questions:** the same as #12. In addition: do you mould any fittings yourself?

**14. DripGlobe SARL** (Draria). Buyer. Products as #12.
- **Questions:** the same as #12. In addition: which colours and sizes are missing from importers?

**15. SARL Union B et CH Plastique (ISS).** Competitor / buyer. Products: IF-01, IF-04, IF-07, IF-08.
- **Purpose:** measure local competition in drip fittings.
- **Questions:**
  1. Which fittings do you mould locally, and which do you import?
  2. Capacity and lead time?
  3. Price per 1,000 for start connectors and end plugs?
  4. Would you buy overflow or outsource tooling?

**16. Irrinet SARL** (Boufarik). Buyer (distributor). Products: IF-01, IF-04, IF-07, IF-08, IF-03, IF-02.
- **Purpose:** distributor stock-outs and seasonal cash tied up.
- **Questions:**
  1. Top 10 fittings by volume, with origin and DZD per 1,000?
  2. Last stock-out: which month and which size?
  3. When do you place pre-season orders, and how much cash is tied up?
  4. Do you already sell a local brand?
  5. Can I buy 10 of each fitting today as samples?

**17. Irriplast SARL** (Bordj Menaïel). Buyer (PE tube distributor). Products and questions as #16.
- Also ask: which fittings customers ask for that you cannot supply.

**18. Groupe STPM Chiali** (Sidi Bel Abbès). Buyer / competitor. Products: IF-01 to IF-08, OS-051.
- **Purpose:** find out whether the large pipe group already moulds small fittings, and whether it buys end caps for pipe ends.
- **Questions:**
  1. Which injected fittings do you make in-house?
  2. Do you buy small drip fittings or end plugs for your irrigation contracts?
  3. Do you cap pipe ends for shipping (OS-051)? Size range and yearly quantity?
  4. Supplier registration and payment terms?

### A.3 Joinery (calls 19–21)

**19. Leader Aluminium** (Hammedi). Buyer (distributor). Products: JC-02, JC-13, JC-16, JC-17, JC-07, IF-40 (JC-12 profile end caps are merged into it).
- **Purpose:** the first price and pain readings for joinery consumables. No Algerian price exists for packers, drainage caps or fly-screen parts.
- **Questions:**
  1. For packers, drainage caps and fly-screen corners and clips: origin and brand (the snippet cites "Dubral", "Alupha"), DZD per 100 and per 1,000, monthly quantity?
  2. Any stock-outs in the last 12 months? Colours you cannot get (RAL)?
  3. Which fly-screen profiles dominate (7×17, 10×20)? Which roller-shutter slat profiles dominate (37/39/42/55)?
  4. MOQ your importer imposes, and lead time?
  5. Would you stock a local range under your label, at what buy price and on what payment terms?

**20. Oxxo (Cevital)** (Aïn Taghrout). Buyer. Products: JC-02, JC-13, IF-40.
- **Purpose:** group purchasing path, and which accessories are still imported.
- **Questions:**
  1. Which glazing packers and bridge packers does your profile system require, and who supplies them now?
  2. Are drainage caps or their colours ever short?
  3. What is on your list of imported accessories that you want localised?
  4. What does supplier approval require (file, QA sample, trial lot)?
  5. Payment days?

**21. Izdihar PVC** (Zaaroura, Tiaret). Buyer. Products: JC-02, JC-13, JC-16.
- **Purpose:** it claims 85% integration. Ask about the other 15%.
- **Questions:**
  1. Which accessories are still imported, and from where?
  2. Yearly volume of packers and drainage caps?
  3. Does the hardware plant next door (its name is not in the files) make any plastic parts?
  4. Approval steps and payment terms?

### A.4 Construction (calls 22–26)

**22. Cosider Canalisations.** Buyer (precast). Products: JC-24, JC-26, JC-40, JC-30.
- **Purpose:** precast spacer demand and custom covers. The company applies formal AHP supplier scoring.
- **Questions:**
  1. Which spacer types and covers do you use for pipes, double-T slabs and walls?
  2. Monthly quantity, current supplier and origin, DZD per 1,000?
  3. Any need for non-standard covers?
  4. How do you register suppliers (criteria, file)? Payment cycle?

**23. Trans-Canal Algeria.** Buyer (concrete pipe). Products: JC-24, JC-26, JC-40.
- **Questions:** the same as #22. In addition: which spacer works on your pipe cages, and how many per pipe?

**24. SOGEDIM.** Buyer (wholesaler / e-shop). Products: OS-010, OS-009, OS-002, JC-36.
- **Purpose:** wholesale anchors for the only GO-candidate in electrical. Today's evidence is retail of 55 DZD for a butterfly anchor and 15 DZD for a hammer-fix sleeve.
- **Questions:**
  1. Purchase price per 100 and per 1,000 for butterfly, hammer-fix and nylon anchors, IRL couplers 16–25 and pipe clips?
  2. Monthly volume and origin?
  3. Stock-outs in the last 12 months?
  4. Is the HAOUAS brand local, and who makes it?
  5. Would you take private label, and on what payment terms?

**25. Mabricole.** Buyer (e-shop). Products: JC-34, JC-24, JC-26, JC-36, OS-009, OS-010.
- **Questions:**
  1. Monthly sales of tile-levelling kits (100-clip kit retails at 780 DA) and of spacers?
  2. Your purchase price per 1,000 and your importer?
  3. Stock-outs and lead time?
  4. Interest in a local clip at a stated price?

**26. Assly.** Buyer (e-shop). Products: JC-24, JC-26, JC-40, JC-36, OS-009, OS-010.
- **Questions:**
  1. Bags sold per month for each spacer reference (the round 30 mm comes in bags of 1,000; the horizontal 40-8/24 in bags of 600)?
  2. Purchase price per bag, and the importer?
  3. Stock-outs?
  4. Does the "collier atlas d.12" mean a PVC/PER pipe snap clip?
  5. Payment terms with suppliers?

### A.5 Furniture (calls 27–29)

**27. EACIM Algérie** (Rouiba). Buyer (metal and office furniture). Products: IF-39, IF-40, IF-42.
- **Purpose:** tube-cap demand, and which gauges dominate.
- **Questions:**
  1. Which tube sizes and walls do you use (round 22/25; square 20×20, 25×25; rectangular 20×40)? Yearly pieces?
  2. Where do your caps, inserts and glides come from? DZD per 100, MOQ?
  3. Missing colours or sizes, or stock-outs?
  4. Tender seasonality and payment terms?

**28. Divindus AMM** (Bab Ezzouar). Buyer (public, school/admin furniture). Products: IF-39, IF-40, IF-42, IF-46, IF-47, IF-48.
- **Questions:** the same as #27. In addition:
  - How does tender payment timing affect supplier payment?
  - Are local-content rules written into the tenders?

**29. SM Mobilier** (Ouled Moussa). Buyer (office, kitchen and storage furniture). Products: IF-46, IF-47, IF-48, IF-49, IF-42.
- **Questions:**
  1. Board colours used, and whether cam covers and screw covers match them?
  2. Pieces per year?
  3. Origin and price of shelf pins, glides and slat holders?
  4. Smallest lot you can buy per colour?

### A.6 Energy, heavy industry and appliances (calls 30–33)

**30. Sonatrach** (spare-parts localisation). Buyer. Products: OS-051, OS-052, and the custom-spares service (OS-098 family, outside the top 50).
- **Purpose:** the only named-buyer, programme-level demand for local spares (700k references; at most 5% local historically).
- **Questions:**
  1. How does a molder pre-qualify as a local spare-parts supplier, and with which file?
  2. Can we get the list of imported plastic spares and caps (references, yearly quantities)?
  3. When are the next technical days (the May 2024 Hassi Messaoud edition had 81 exhibitors)?
  4. Payment terms for local suppliers?

**31. Sonelgaz group.** Buyer. Products: OS-051, OS-052, OS-002.
- **Questions:**
  1. Is there a local-content or supplier-development unit for plastic spares?
  2. Do ENEL Azazga or the group buy plastic terminal covers, plugs or caps?
  3. How do suppliers register?
  4. Payment cycle?

**32. Sider El Hadjar TSS** (seamless tubes). Buyer. Products: OS-051, OS-052, and OS-068 (4½–5½ in thread protectors, outside the top 50; the larger sizes need 200–450 t).
- **Purpose:** the one named OCTG buyer with verified volume: 1,000 km of casing for Sonatrach, 2024–2026.
- **Questions** (p2_other_sectors §11):
  1. Protector type, origin, unit price and quantity by size?
  2. API or licensor requirements?
  3. Are used protectors recycled or reused?
  4. Who buys them: TSS purchasing, or are they specified by Sonatrach?

**33. Samha** (Guedjel). Buyer (appliances; AC integration target only 30–40%). Product: OS-039.
- **Purpose:** find which small plastics are still in the CKD kits.
- **Questions** (funnel next action):
  1. Which small plastics (feet, clamps, condensate elbows) still come in CKD kits?
  2. Volumes per year?
  3. Target price?
  4. First-article and QA process, and payment days?

### A.7 Services and competitor checks (calls 34–36)

**34. Legacy Exhibitions** (Cosmetica North Africa). Service. Products: CL-003, CL-001.
- **Purpose:** get the Cosmetica 2026 exhibitor list (about 250 Algerian firms), the best single buyer list for closures.
- **Questions:**
  1. Can we get the 2026 exhibitor list with contacts?
  2. Which exhibitors were packaging suppliers?
  3. 2027 dates and B2B programme?

**35. BASTP** (ALGEST co-organiser). Service. Products: all.
- **Purpose:** register for ALGEST, 23–25 Nov 2026 at SAFEX, and its B2B matchmaking.
- **Questions:**
  1. Visitor or exhibitor registration and cost; how B2B meetings are booked?
  2. Which large buyers (donneurs d'ordre) post subcontracting needs, and can we get the list?
  3. Membership terms and the national subcontractor directory?
  4. SANIST 2027 dates?

**36. SNK Plastic** (Rouiba). Competitor / service. Products: all, for subcontract trial runs.
- **Purpose:** (a) a fallback to run the first molds before buying a press; (b) a competition check. p3 ranks SNK as threat #1.
- **Questions:**
  1. Hourly rate for a 100–120 t press, with and without operator?
  2. Minimum run, setup charge, and mold storage terms?
  3. Will you sign confidentiality and non-use of customer molds?
  4. Do you already make spacers, drip fittings, tube caps or flip-tops for your own sale?
  5. Lead time to slot a 20k-piece run?

### A.8 Resin and masterbatch suppliers (calls 37–41)

**37. POLYCHIMICAL SARL** (Skikda). Supplier. Products: all PP/PE parts; PA6 for OS-009 and OS-010.
- **Purpose:** replace the 220–350 DZD/kg resin estimate with a written quote. The files call this "the single most important missing input".
- **Questions:**
  1. Grades in stock: PP homopolymer injection MFR 10–25, PP impact copolymer, HDPE injection, LDPE, and PA6 (type)? Grade codes and producers?
  2. DZD/kg ex-VAT at 100 kg, 1 t and 5 t; MOQ; lead time; price validity?
  3. Current origin (Gulf, so Hormuz-exposed, or Egypt, Turkey, EU)? Do you stock CP2K HDPE?
  4. Do you provide TDS, SDS and a CoA per lot?
  5. Payment terms?

**38. AB POLYMERS SARL** (Es Senia). Supplier. The same questions as #37.
- This is the only distributor that explicitly cites injection-grade HDPE.

**39. DISTRIPOL SARL** (Zéralda). Supplier. The same questions as #37.

**40. HIMAPLAST SARL** (Bou Ismaïl). Supplier (colour masterbatch, fillers). Products: CL-003, JC-13, IF-46, IF-47, JC-36.
- **Questions:**
  1. Do you colour-match to a sample (RAL/Pantone), and how fast?
  2. MOQ per colour, price per kg, and let-down ratio?
  3. Carrier compatible with PP and with HDPE? UV and black/white masterbatch?
  4. CaCO3 filler masterbatch price (for spacers)?

**41. SARL TAIF MASTER BATCH** (Beni Tamou). Supplier (masterbatch). The same questions as #40.

### A.9 Mold makers (calls 42–45)

Send each one the same 3 drawings or samples: IF-01 (start connector, 16-cav), JC-24 (spacer wheel, 8-cav) and IF-39 (22/25 cap, 16-cav). That gives directly comparable quotes.

**42. ZEROUNI MOLDS** (Tassala El Merdja). Service (mold maker; CNC, EDM, heat treatment).
- **Questions:**
  1. Price and lead time for the three molds above (steel grade, cavities, cold or hot runner, ejection)?
  2. Do you have a press for T1 tryout? How many warranty shots?
  3. Will you sign an NDA and a no-design-reuse clause?
  4. Payment schedule? Repair and maintenance rates?

**43. FMPI** (Khemis El Khechna / Kouba). Service. The same questions as #42.
- Also ask about CAD/DFM support from samples (reverse engineering).

**44. Precision Industry** (Ouled Moussa). Service. The same questions as #42.
- Also ask: do you run injection presses for tryout?

**45. CFM Engineering** (El Eulma). Service. The same questions as #42.
- Also ask: experience with 24–32-cavity small-part molds and with hinge (flip-top) molds?

### A.10 Machine dealers (calls 46–48)

**46. AFC Industry Algérie** (Yizumi). Supplier.
- **Questions:**
  1. Quote a 100 t and a 120 t servo press, each with the small-screw option (Ø30–35). Shot range, tie-bar distance (target 380 and 410 mm), mold height?
  2. Price, lead time, warranty, commissioning, local spares and technician response time?
  3. Two reference customers I can visit?
  4. Help with the AAPI duty exemption and with domiciliation?

**47. Plasticolor Group** (Chen Hsong). Supplier. The same questions as #46.
- This gives a competing quote.

**48. 2M Expert Algeria** (Cosmos). Supplier. The same questions as #46.
- 2M Expert also distributes raw materials, so ask for PP/HDPE prices too. Ask which transitaire handles its machine imports, for call #49.

### A.11 Customs broker and bank (calls 49–50)

**49. Customs broker (transitaire).** Service.
- **Purpose:** the duty and DAPS readout that the files list as the most valuable desk check left.
- **Request:** a written readout of DD, DAPS, TVA, TCS and PRCT for these lines:
  - 3923.50.92 (closures);
  - 3925.30, 3925.90, 3926.90.99.90, 3926.30, 3917.40;
  - 8424.90, 8436.80/99;
  - 8480.71 (molds; files say 5% DD);
  - 8477.10 (injection machines).
- **Also ask:**
  - GAFTA-origin treatment;
  - clearance time and cost for one LCL mold shipment (300–500 kg) and for one 120 t press;
  - the AAPI exemption steps;
  - the documents needed for the PPI and for prior domiciliation.

**50. Founder's domiciliation bank.** Service.
- **Questions:**
  1. Domiciliation under Note 01/DGC/2026: a 120% provision at least 30 days before shipment. Can 50/40/10 mold payments and a press deposit be advanced, or only paid against documents?
  2. Investment credit (files: about 5.8–6.9%) and leasing (about 10%) for a 100–120 t press?
  3. Do you discount or endorse (avaliser) customer traites?
  4. Can you check a new customer against the Centrale des impayés?
  5. Do you offer a factoring product under Regulation 26-03 (Aug 2026)? Current rules on cash deposits into commercial accounts?

---

## B. Factory visit list: 30 plants most likely to expose component shortages

### What to look for at every plant
- **On the line:** plastic parts in cartons or bags marked Made in China, Turkey or Italy, or with foreign labels.
- **In stores:** empty bins, substitute parts, and parts modified by hand (cut, taped or drilled).
- **Off the line:** reject bins, and colour mismatches between the part and the product.
- **Ask:** "Which plastic part stopped or slowed you last year?"
- **Photograph** (with permission) the label of every imported plastic part you see.
- **Ask for one sample** of each.

Plants with no recorded contact are approached through a phone call first (section A), or at ALGEST.

| # | Plant | Wilaya / zone | Why it is on the list (evidence in files) | What to look for | Products |
|---|---|---|---|---|---|
| 1 | Oxxo (Cevital) | Aïn Taghrout, BBA | 2.1M windows/yr; robotised assembly; accessories probably tied to foreign systems | Packer bins at glazing stations (thicknesses, colours, origin); drainage caps by profile colour; end caps; what is fitted by hand | JC-02, JC-13, IF-40 |
| 2 | Izdihar PVC, plus the hardware plant next door (name not in files) | Zaaroura, Tiaret | Claims 85% integration; opened Jul 2025 | The non-integrated 15%: imported plastic accessories in stores; stock-out history | JC-02, JC-13, JC-16 |
| 3 | SPA Profilés Aluminium du Maghreb | Aïn Defla | Aluminium extruder; exported 130 t to Tunisia | End caps and accessories its customers ask for; protective plastic parts used in packing profiles | IF-40, JC-13, JC-16 |
| 4 | Condor–Hisense AC complex | BBA | 2M ACs/yr planned (operational status 2026 not confirmed) | CKD kit contents: condensate elbows, clamps, feet, grommets still imported | OS-039, OS-084 |
| 5 | Géant Electronics | BBA | New AC and fridge units; 70% fridge integration | Small plastics in kits; which are bought locally | OS-039 |
| 6 | Condor Electronics | BBA | Captive injection (make-vs-buy competitor); conflicting "bankruptcy" headline | What they do not mould themselves; check status and payment health | OS-039, OS-051 |
| 7 | Samha | Guedjel, Sétif | AC integration target only 30–40% | CKD kit plastics; feet, clamps, condensate parts | OS-039 |
| 8 | Brandt Algérie (Cevital) | Sétif | Moulds most parts in-house | Overflow or small parts they buy in; presses idle or full | OS-039, OS-084 |
| 9 | Iris (SATEREX) | Sétif | Electronics complex; no sourcing info | Small plastic clips, feet and grommets in kits | OS-084 |
| 10 | ENIEM | Oued Aïssi, Tizi Ouzou | Documented raw-material stock-outs; CKD AC start slipped; payment risk | Stock-out evidence; imported kit plastics. **Advance payment only** (p3) | OS-039, OS-084 |
| 11 | Electro-Industries (ENEL) | Azazga, Tizi Ouzou | Transformers and motors; 100% Sonelgaz from Q1 2026 | Terminal covers, cable glands, plugs and caps, and their origin | OS-051, OS-052 |
| 12 | ENICAB | Biskra | About 20,000 t/yr cable | Cable-end caps and drum/reel consumables; origin and yearly quantity | OS-051, OS-052 |
| 13 | Henkel Algérie, Réghaïa | Réghaïa, Algiers | Develops local packaging suppliers on site ("wall-to-wall"); Gliss shampoo local since Dec 2025 | Which closures are still imported; supplier-development criteria | CL-001, CL-007, CL-013 |
| 14 | Hayat DHC | Bouinane, Blida | Detergents and diapers; formal purchasing | Closure types and necks; local vs imported | CL-007, CL-013 |
| 15 | Laboratoires Venus / SAPECO | Ouled Yaich, Blida | Reportedly makes its own packaging (a sign that outside supply failed) | Their own press shop; what they still buy | CL-001, CL-003 |
| 16 | Labonedjma | Larbaâ, Blida | 600+ SKUs | Closure colours per SKU; lot sizes; stock-outs | CL-003, CL-001, CL-013 |
| 17 | Univers Détergent | Algiers | Formal technical buyer | Measuring caps, screw caps, necks | CL-007, CL-013 |
| 18 | ENAD / Shymeca | Sour El Ghozlane, Bouira | 6 detergent units and 1 cosmetics unit (public) | Bleach and soap closures; supply interruptions; payment practice | CL-007 |
| 19 | Unilever Algérie | Oran | Shampoo and soap; 80% localisation target | Closures still imported (low pain expected; global contracts) | CL-001, CL-007 |
| 20 | Anabib Plastiques | Aïn Arnat, Sétif | Drip-tape and element maker | Fittings packed with tape; stock in store before the season; colours | IF-01 to IF-08 |
| 21 | Medi Goutte | Aïn Benian, Algiers | Declares "tout type d'irrigation goutte à goutte" | Whether fittings are moulded in-house or imported | IF-01 to IF-08 |
| 22 | Groupe STPM Chiali | Sidi Bel Abbès | Largest pipe group; also a potential competitor in fittings | Pipe-end caps in the yard (OS-051); injected fittings range; imported small parts | OS-051, IF-01 to IF-08 |
| 23 | K-Plast group (K-Plast Tube; I.M.A Industry) | Sétif | PEHD pipe and cable; I.M.A injects gas-network parts | Pipe-end caps; whether I.M.A takes outside work (competitor) | OS-051, OS-052 |
| 24 | Cosider Canalisations precast plant | location to confirm by phone (not in files) | Precast walls and double-T slabs; formal AHP supplier scoring | Spacer types on cages; custom covers; stock; origin | JC-24, JC-26, JC-40, JC-30 |
| 25 | Trans-Canal Algeria | location to confirm by phone (not in files) | Automated concrete-pipe plant | Spacers on pipe cages; quantity per pipe | JC-24, JC-26 |
| 26 | Sider El Hadjar TSS | El Hadjar, Annaba | 1,000 km casing for Sonatrach 2024–26 | Thread protectors: brand, size, origin; recycling bins | OS-051, OS-052 (OS-068) |
| 27 | EACIM Algérie | Rouiba, Algiers | Metal and office furniture | Tube gauges on the line; caps and inserts in stock; colour gaps | IF-39, IF-40, IF-42 |
| 28 | Divindus AMM | Bab Ezzouar, Algiers | Series furniture for schools and administrations (tenders) | School-desk tube caps; glides; volumes per tender | IF-39, IF-40, IF-42 |
| 29 | SM Mobilier | Ouled Moussa, Boumerdès | Office, kitchen and storage furniture | Cam covers and screw covers vs board colours; shelf pins; slat holders | IF-46, IF-47, IF-48, IF-49 |
| 30 | Dhikra Office Manufacturing | Ouled Heddadj, Boumerdès | High-end office furniture | Glides, tube inserts, cap colours; imported hardware | IF-39, IF-40, IF-42 |

---

## C. Distributor and wholesaler visit list: 20, by cluster

### Rule at every shop
1. Ask the p3 questions 1–8.
2. Read the price tag or invoice.
3. Buy the samples listed in section D.
4. Ask "who is your importer?" Then go up the chain to that importer.

Where the files name no shop, the founder collects names on site. Write down for each shop: shop name, phone, products, origin, price per 100 and per 1,000.

| # | Cluster | Shop or zone | Named in files? | What to check | Products |
|---|---|---|---|---|---|
| 1 | Hammedi / Boumerdès | Leader Aluminium | Yes (Ouedkniss store 14372) | Joinery consumables price, origin, monthly quantity, colours, stock-outs | JC-02, JC-13, JC-16, JC-17, JC-07 |
| 2 | Hammedi / Boumerdès | Aluminium/PVC accessory shops next to Leader Aluminium (an Ouedkniss "accessoires aluminium" cluster) | No: names to be collected on site (target 4–5 shops) | Same as #1; dominant fly-screen and shutter profiles | JC-02, JC-13, JC-16, JC-17, JC-07 |
| 3 | Hammedi / Boumerdès | Irriplast SARL, Bordj Menaïel | Yes (Kompass) | Fittings stocked, origin, price per 1,000, pre-season stock | IF-01 to IF-08, IF-20 |
| 4 | East Algiers | El Hamiz quincaillerie wholesale zone (Dar El Beida). The files name it as a hub but it is unsourced | No: names to be collected on site (target 3 wholesalers) | Spacers, tile clips, anchors, IRL couplers, pipe clips: wholesale per 1,000, monthly quantity | JC-24, JC-26, JC-40, JC-34, JC-36, OS-002, OS-009, OS-010 |
| 5 | East Algiers | AITECH EURL (Sidi M'Hamed), irrigation distributor | Yes (Kompass) | Drip fittings origin and price | IF-01 to IF-08 |
| 6 | East Algiers / West Algiers | PAFIX emballage (Draria), cosmetic packaging trader | Yes (Facebook) | Flip-top, disc-top and screw-cap prices per 1,000; MOQ; colours | CL-001, CL-003, CL-007, CL-013 |
| 7 | East Algiers / South Algiers | E.C.A Emballages Cosmétiques (Birtouta) | Yes (Facebook https://www.facebook.com/p/ECA-Emballages-Cosm%C3%A9tiques-100064352521915/) | Same as #6 | CL-001, CL-003, CL-007, CL-013 |
| 8 | Algiers | Automotive spare-parts traders (aftermarket clips and blanking plugs). The files name no street | No: location and names to be collected (ask garages and body shops) | Which plastic clips and plugs are out of stock, for which fleet models; DZD prices | OS-084 |
| 9 | Blida / Mitidja | Irrinet SARL (Boufarik) | Yes (Kompass) | Distributor stock-outs; seasonal orders; sample purchase | IF-01 to IF-08, IF-20 |
| 10 | Blida / Mitidja | Boufarik agri-input and irrigation dealers | No: names to be collected on site (2–3 shops) | Buy 10 of each drip fitting (funnel action); origin; price | IF-01 to IF-08 |
| 11 | Blida / Mitidja | Beni Mered quincaillerie-meuble (furniture hardware) wholesalers. Beni Mered is a furniture cluster per D&B | No: names to be collected on site (2 wholesalers) | Tube caps, glides, cam and screw covers, shelf pins, slat holders: origin, price per 100, MOQ, colours | IF-39, IF-40, IF-42, IF-46, IF-47, IF-48, IF-49 |
| 12 | El Eulma (Sétif) | El Eulma wholesale quincaillerie and building-materials traders | No: names to be collected on site (the files say no El Eulma wholesaler could be named) | Spacers, tile clips, anchors, pipe clips: wholesale per 1,000, importer names | JC-24, JC-26, JC-40, JC-34, JC-36, OS-009, OS-010 |
| 13 | El Eulma (Sétif) | El Eulma electrical wholesalers | No: names to be collected on site | IRL couplers, pipe clips, anchors; local brands (e.g. HAOUAS) vs imported | OS-002, JC-36, OS-009, OS-010 |
| 14 | Sétif | Sétif / Aïn Arnat irrigation and agri dealers | No: names to be collected on site | Fittings from Anabib or Tupol vs imported; prices | IF-01 to IF-08 |
| 15 | Sétif | Sétif tile and building-materials depots | No: names to be collected on site | Tile-clip kits and wedges; spacers; origin | JC-34, JC-24, JC-26 |
| 16 | BBA | Aluminium/PVC accessory shops serving joiners who use Oxxo profiles | No: names to be collected on site | Packers and drainage caps that fit Oxxo profiles; colours | JC-02, JC-13, JC-16 |
| 17 | BBA | Appliance after-sales spare-parts shops (Condor, Géant) | No: names to be collected on site | Missing plastic spares; condensate elbows; prices | OS-039, OS-084 |
| 18 | Oran | Plast Windows Oran (Rue Bouziane Ahmed n°12 bis, cité Seddikia) | Yes (El Mouchir listing; no phone recorded) | PVC window hardware range; local vs imported; prices | JC-02, JC-13, JC-16 |
| 19 | Oran | Oran irrigation and hardware wholesalers | No: names to be collected on site | Drip fittings, spacers, anchors: prices and origin in the West | IF-01 to IF-08, JC-24, OS-010 |
| 20 | Others: Biskra (optional trip) | Biskra greenhouse and drip input dealers (end-demand centre) | No: names to be collected on site | Buy samples (funnel action); seasonal stock-outs; colours | IF-01 to IF-08, IF-20 |

---

## D. Sample-buying plan

### Rules
- **Buy every top-20 product and the key top-50 items.** Get at least one imported sample. Get one local sample too wherever a local version exists; ask "made in Algeria" or "fabrication locale?" in every shop.
- **Buy 2–4 sources per product**, from different shops or importers. That gives (a) origin and price dispersion and (b) enough pieces to read every cavity number.
- **Quantities.** For multi-cavity parts, buy at least 2× the expected cavity count from **the same bag**, so that all cavity IDs can be read. Examples: 50 pieces for a 16–24-cavity part; 100 for a 32-cavity part.
- **Keep the paperwork.** Keep each bag's label, the receipt (bon or facture) and a photo of the shelf price. **Number every bag** with sample ID = product ID + source letter + date (e.g. "IF-01-B-2026-10-19").
- **Unit prices below.** They are the retail snippet prices recorded in the files where one exists: assly, mabricole, SOGEDIM, Jumia. Everything else is an **ASSUMPTION** (roughly 2–3× the model ex-works price). The real paid price goes into the measurement sheet.

| Product | What exactly to buy (variants) | Imported version: where | Local version: where | Sources × qty | Unit price basis (DZD) | Budget (DZD) |
|---|---|---|---|---|---|---|
| JC-26 spacer chair | 40-8/24 and 50-8/24 | El Hamiz / El Eulma quincaillerie; Assly (anchor price) | Ask in same shops | 2 × 50 | 22.5 (assly 13,500/600) | 2,250 |
| JC-24 spacer wheel | 30 mm cover, rebar 8–14 | Same | Same | 2 × 100 | 13.6 (assly 13,600/1,000) | 2,720 |
| JC-40 mesh clip spacer | "étoile" for welded mesh | Same | Same | 2 × 50 | 15 (ASSUMPTION) | 1,500 |
| JC-34 tile clips (+ wedges) | 1, 1.5, 2 mm clips; reusable wedges | Mabricole/Jumia kit; Sétif tile depots | Same | 3 kits × 100, plus 1 × 100 wedges | 7.8 clips (780/100); 11 wedges (680–1,100/100) | 3,440 |
| JC-02 bridge packer | 3 thicknesses (e.g. 2, 3, 4 mm) | Hammedi (Leader Aluminium + neighbours) | Same; Plast Windows Oran | 3 × 50 | 20 (ASSUMPTION; no DZD price in files) | 3,000 |
| JC-16 fly-screen corner | 7×17 and 10×20 | Hammedi; BBA accessory shops | Same | 4 × 25 | 25 (ASSUMPTION) | 2,500 |
| JC-17 fly-screen clips | Spring and fixation clips | Hammedi | Same | 2 × 50 | 10 (ASSUMPTION; no price anywhere) | 1,000 |
| JC-36 pipe clip "collier atlas" | Ø16, Ø20, Ø25/32 | El Hamiz / El Eulma; Assly | Same | 3 × 100 | 10.2 (assly 1,021/100) | 3,060 |
| JC-13 drainage cover | White, black, one RAL colour (e.g. brown/anthracite) | Hammedi; BBA | Same | 3 × 50 | 15 (ASSUMPTION) | 2,250 |
| JC-30 formwork cone | 22 mm tube cone; D-cone type | Quincaillerie wholesalers; formwork suppliers | Same | 2 × 50 | 40 (ASSUMPTION; FOB spread wide) | 4,000 |
| JC-07 shutter guide funnel | 2 most common slat profiles | Hammedi | Same | 2 × 10 | 100 (ASSUMPTION) | 2,000 |
| OS-002 IRL coupler | 16, 20, 25 mm | El Eulma electrical; SOGEDIM | Ask for local conduit-maker brand | 3 × 50 | 25 (ASSUMPTION) | 3,750 |
| OS-010 butterfly anchor | 8 mm, without screw and with screw | SOGEDIM; El Hamiz | Same | 2 × 50 | 55 (SOGEDIM retail) | 5,500 |
| OS-009 hammer-fix sleeve | 8×80 grey | SOGEDIM; El Hamiz | Same | 2 × 100 | 15 (SOGEDIM retail) | 3,000 |
| OS-084 blanking plugs | Assortment for 2 dominant fleet models | Algiers car-parts traders; BBA after-sales shops | Same | 2 × 50 | 40 (ASSUMPTION) | 4,000 |
| OS-039 AC condensate elbow | 16 and 20 mm | BBA after-sales shops; AC installers | Same | 2 × 10 | 100 (ASSUMPTION) | 2,000 |
| OS-051 push-over pipe end cap | Ø20, 32, 40, 60 | Ask Chiali, K-Plast and hydraulic-hose shops (often given free) | Same | 4 × 25 | 20 (ASSUMPTION) | 2,000 |
| OS-052 threaded protection cap | BSP 1/4, 1/2, 3/4, 1 in | Hydraulic-hose assemblers (names on site) | Same | 4 × 25 | 20 (ASSUMPTION) | 2,000 |
| CL-001 / CL-003 flip-top | 24/410 and 28/410, white plus one colour | PAFIX, E.C.A, Ouedkniss traders | SIPEM (ask for samples or buy minimum); PAP Plast sets | 4 × 50 | 15 (ASSUMPTION; prior unsourced estimate 8–25) | 3,000 |
| CL-007 plain screw cap | 24/410 smooth/ribbed | Same | Same | 2 × 50 | 8 (ASSUMPTION) | 800 |
| CL-013 orifice reducer | 18–28 mm necks | Same; from hair-oil bottles | SIPEM | 2 × 50 | 8 (ASSUMPTION) | 800 |
| Shelf audit (closures) | Photograph 30 shampoo, dish-liquid and laundry SKUs; buy 15 with dispensing caps (local and imported brands) | Supermarkets in Algiers / Blida | Same | 15 × 1 | 400 per bottle (ASSUMPTION) | 6,000 |
| IF-39 round insert | 22 and 25 mm, 2 wall gauges | Beni Mered furniture-hardware wholesalers | Ask EACIM / Divindus what they use | 4 × 50 | 15 (ASSUMPTION) | 3,000 |
| IF-40 square/rect insert | 20×20, 25×25, 20×40 | Same | Same | 6 × 50 | 15 (ASSUMPTION) | 4,500 |
| IF-42 nail-on glide | 19 and 24 mm | Same | Same | 2 × 50 | 20 (longlist 5–20) | 2,000 |
| IF-49 bed-slat holder | 53 mm (and the most common size) | Same | Same | 2 × 25 | 25 (ASSUMPTION) | 1,250 |
| IF-46 / IF-47 / IF-48 | Cam cover, 2-part screw cover, 5 mm shelf pin (2 board colours) | Same | Same | 3 products × 2 × 100 | 5 (ASSUMPTION) | 3,000 |
| IF-01 start connector | 16/17 mm with lock nut | Irrinet, Boufarik dealers, Irriplast, Biskra | Anabib / ISS / Medi Goutte if they sell fittings | 2 × 50 | 40 (longlist 15–40) | 4,000 |
| IF-02 lock nut | Loose spare nuts if sold separately | Same | Same | 2 × 50 | 10 (ASSUMPTION) | 1,000 |
| IF-03 tape-tape coupling | 16/17 mm | Same | Same | 2 × 25 | 40 (ASSUMPTION) | 2,000 |
| IF-04 barbed coupling | 16 mm | Same | Same | 2 × 50 | 25 (ASSUMPTION) | 2,500 |
| IF-05 / IF-06 barbed tee and elbow | 16 mm | Same | Same | 2 products × 2 × 25 | 25 (ASSUMPTION) | 2,500 |
| IF-07 figure-8 | 16 mm | Same | Same | 2 × 50 | 15 (ASSUMPTION) | 1,500 |
| IF-08 end plug | 16 mm barbed and ring type | Same | Same | 2 × 50 | 15 (ASSUMPTION) | 1,500 |
| IF-20 layflat take-off | Layflat-to-tape | Same | Same | 2 × 10 | 80 (ASSUMPTION) | 1,600 |
| **Parts subtotal** | | | | | | **90,920** |
| Measurement tools (ASSUMPTION prices) | 0.01 g pocket scale with 100 g calibration weight; 150 mm digital caliper (0.01 mm); thread-pitch gauge (metric + inch); radius gauge; 10× loupe; small steel ruler; craft knife; lighter and metal tray (burn test); 3 glass jars; isopropyl alcohol; table salt; grey photo card; 300 numbered zip bags and labels | Algiers tool shops / e-shops | — | — | — | 30,000 |
| Transport, parking, contingency (about 30% of parts) | — | — | — | — | — | 27,000 |
| **Total sample plan budget** | | | | | | **≈ 148,000 DZD** |

**Optional price anchors** (only if a wholesaler refuses to sell loose pieces):
- One full Assly bag of horizontal chairs: 600 pcs, 13,500 DA.
- One bag of 1,000 spacer wheels: 13,600 DA.

These add about 27,000 DZD but give a verified pack price.

---

## E. Measurement sheet

### E.1 Template: one row per sample bag

Fill it in a spreadsheet; the columns match this table. The weight is the **mean of 10 pieces**. Dimensions are the **min and max across 10 pieces from different cavity numbers**.

| Field | What to record | How |
|---|---|---|
| Sample ID | Product ID + source letter + date (e.g. JC-24-A-2026-10-13) | From the bag label |
| Product | Name + variant (size, cover, neck) | |
| Sample source | Shop name, cluster, wilaya; importer or maker named by the shop | Ask: "c'est qui l'importateur / le fabricant ?" |
| Price paid | DZD and pack size; per piece; retail or wholesale; with or without facture | Receipt or price-tag photo |
| Origin marking | Text on the part or bag ("Made in China", Turkish/Italian brand, "Made in Algeria", none); recycling code (>PP<, >PE-HD<, >PA6<) | Loupe; photo |
| Dimensions (key) | Product-specific critical dimensions from E.4 | Caliper, 0.01 mm; 3 readings each |
| Weight (g) | Mean, min, max of 10 pcs (0.01 g scale); runner weight if a runner is attached | Tare the scale; weigh singly |
| Polymer estimate | PP / HDPE / LDPE / PA6 / POM / ABS / PVC / other, plus the tests used (E.2) | Float, burn, flex |
| Colour | Name + nearest RAL (joinery, furniture) or Pantone (cosmetics); opaque or translucent | Compare to a RAL fan or a reference sample |
| Finish | Gloss, matte or textured; visible flow lines, sink marks, flash | Visual |
| Tolerances (observed spread) | Max − min of each key dimension across 10 pcs; flag a spread > 0.1 mm on snap or thread features | Caliper |
| Threads | Type (metric, BSP, NPT, GPI/SPI closure), pitch or TPI, turns, start type | Pitch gauge |
| Neck finish (closures only) | T / E / H / S of the bottle neck and the matching cap internal dimensions (E.3) | Caliper; go/no-go on a reference bottle |
| Parting line | Location and whether flash is visible; side action (lifters, slides) visible? | Visual / loupe |
| Gate location / type | Pin-point (3-plate, small dimple), edge or tab, submarine (crescent mark on side wall), direct sprue, hot-runner (small round vestige, often on a recessed spot) | Loupe; photo |
| Cavity numbers seen | List every cavity number read (e.g. 1, 2, 3 … 16); **estimated cavities = highest number seen**, rounded up to 2, 4, 8, 16, 24, 32 or 48 | Read the numbers on all pieces in the bag |
| Likely process | Injection cold runner / hot runner / 3-plate; insert-moulded (metal nail or screw); assembled (2+ parts); not injection (extruded and cut, blow-moulded) | From gate, runner and insert marks |
| Supplier | Maker if marked, importer per shop, brand | |
| Photos | P1 top, P2 bottom, P3 side, P4 gate close-up, P5 cavity number, P6 origin mark, P7 bag label/price, P8 in use (on rebar, tube, profile, bottle) | Grey card + ruler in every frame |
| Notes / pain heard | Stock-outs, colours missing, complaints, quantities quoted by the seller | From the interview |

### E.2 Polymer estimate: float, burn and flex tests

Do these at a bench, outdoors or with ventilation, on a 2–3 mm sliver held with pliers over a metal tray.

**Never burn-test parts you suspect are PVC indoors.** PVC releases HCl.

These are general workshop identification methods, not lab results. Record the result as **ASSUMPTION / estimate**, and get the true grade later from the supplier's TDS.

**1. Float test**
- Use tap water at 1.00 g/cm³. Add a drop of dish soap to break surface tension.
- **Floats:** PP (≈0.90–0.91), LDPE (≈0.91–0.93), HDPE (≈0.94–0.96).
- **Sinks:** PA6 (≈1.13), POM (≈1.41), ABS (≈1.04–1.06), PS (≈1.05), PC (≈1.20), PVC (≈1.3–1.45).
- **To separate PP from HDPE:** mix water and isopropyl alcohol until a known PP reference piece floats and a known HDPE reference piece sinks. Calibrate with reference pieces marked >PP< and >PE-HD<. Then test the sample.
- **Caution:** talc- or chalk-filled PP and HDPE (common in cheap or recycled spacers), glass-filled PA, and heavy masterbatch loadings can sink. Record that, and expect a filled grade.

**2. Burn test**

| Polymer | Flame | Smell | Behaviour |
|---|---|---|---|
| PP | Blue base, yellow tip | Waxy, paraffin | Keeps burning, drips |
| PE | Blue base, yellow tip | Candle wax | Keeps burning, drips; softer and more waxy to the touch than PP |
| PA6 | Blue/yellow | Burnt hair / celery | Self-extinguishes; drips in strings, forms a bead |
| POM | Almost invisible blue | Sharp formaldehyde | Little smoke |
| ABS / PS | Yellow, very sooty | Sweet styrene | Keeps burning |
| PVC | Yellow with green edge | Acrid | Self-extinguishes |

**3. Flex, scratch and sound**
- **PP:** a thin section folded 20 times survives (living hinge). Flip-top hinges are always PP.
- **LDPE:** scratches easily with a fingernail and feels waxy.
- **HDPE:** stiffer than LDPE, waxy, whitens when bent.
- **PA6:** tough; gives a dull "ring" when dropped.
- **POM:** hard, slippery, with a metallic ring.
- **PS / ABS:** crack or whiten sharply when folded.

**4. Cross-check** with any recycling code moulded on the part.

### E.3 Closure neck finish reference (24/410 and 28/410)

The dimension letters follow the GPI/SPI convention:
- **T** = thread outside diameter;
- **E** = neck diameter at the thread root;
- **H** = height from the top of the finish to the shoulder or bead;
- **S** = distance from the top of the finish to the start of the thread.

The "410" finish has about 1.5 thread turns ("400" ≈ 1 turn; "415" ≈ 2 turns).

**The nominal values below are NOT from the repository files.** They are approximate reference values from the general GPI/SPI chart and are labelled ASSUMPTION. Before any mold design, verify them against the GPI standard sheet or the blower's neck drawing, and with a go/no-go check on the buyer's real bottle.

| Finish | T (mm) | E (mm) | H (mm) | S (mm) | Thread pitch |
|---|---|---|---|---|---|
| 24/410 | ≈ 23.4–23.9 | ≈ 21.4–21.8 | ≈ 15.0–15.8 | ≈ 0.8–1.6 | ≈ 8 TPI (≈ 3.2 mm) |
| 28/410 | ≈ 27.2–27.7 | ≈ 25.2–25.6 | ≈ 17.1–17.9 | ≈ 0.8–1.6 | ≈ 6 TPI (≈ 4.2 mm) |
| 28/400 (for comparison) | as 28/410 | as 28/410 | ≈ 9.5–10.3 | ≈ 0.8–1.6 | ≈ 6 TPI |

**Measure on the bottle:**
- T, E, H and S;
- the inner bore (I) at the top, which matters for plug seals and orifice reducers;
- the bead or transfer bead diameter.

**Measure on the cap:**
- internal thread crest and root diameters;
- skirt height;
- seal type: plug or "crab-claw", liner, or flat;
- orifice Ø;
- hinge type: strap or butterfly;
- hinge thickness;
- lid snap force (subjective, 1–5).

**Functional checks:**
- 50 open/close cycles of the hinge, recording whether it whitens or cracks;
- a leak test: fill the bottle with water, close it, squeeze and invert for 1 minute;
- torque to close by hand (subjective, 1–5).

### E.4 Key dimensions per product family

| Family | IDs | Key dimensions to record |
|---|---|---|
| Rebar spacers | JC-24, JC-26, JC-40 | Concrete cover (mm); rebar Ø range held; clip opening; wheel OD and rim width; chair height and footprint; wall thickness; open or closed base; filled or unfilled |
| Tile clips | JC-34 | Joint thickness at neck (1 / 1.5 / 2 / 3 mm); base size; break-off notch depth; tile thickness range; wedge length and taper |
| Joinery | JC-02, JC-13, JC-16, JC-17, JC-07 | Packer thickness series, width and length, bridge channel width; drainage slot size and clip legs; fly-screen profile inner section (7×17, 10×20) and leg length; guide-rail width |
| Pipe and electrical | JC-36, OS-002 | Pipe or conduit OD held; clip opening; screw hole Ø; stand-off from wall; coupler ID, length and stop |
| Anchors | OS-010, OS-009 | Sleeve OD and length; wing span (butterfly); collar Ø; screw size used; insert (nail-screw) present or not |
| Formwork | JC-30 | Bore for 22 mm tube; cone OD and length; tie-rod hole Ø |
| Closures | CL-001, CL-003, CL-007, CL-013 | See E.3 |
| Furniture | IF-39, IF-40, IF-42, IF-46 to IF-49 | Tube OD and wall range accepted; fin count and fin OD; cap top thickness and height; glide Ø and nail length; cam-cover Ø; pin Ø × length; slat width held |
| Drip fittings | IF-01 to IF-08, IF-20 | Barb OD and barb count; tape ID it fits (16/17 mm); lock-nut thread pitch and OD; rubber or no rubber insert; figure-8 slot width; wall thickness |
| Industrial caps | OS-051, OS-052, OS-084, OS-039 | Pipe or hole Ø held; panel thickness; thread type and size; head Ø; elbow ID/OD |

---

## F. Validation thresholds: GO / WAIT / KILL

### F.1 Evidence rules that apply to every product

#### Counting rules
- **Independent buyer.** A different legal owner. Two branches of one group = 1 buyer. A distributor and its own importer = 1 buyer. At least one of the three buyers must be an end user or a distributor that buys from a **different** importer than the others.
- **Recurring need.** The buyer reorders at least quarterly, **and** reports a past purchase (last order date and quantity). Opinions do not count (p3 design rule).
- **Volume counting.**
  - 100% of volume backed by an invoice, delivery note (BL), PO or signed LOI.
  - 50% of a stated volume with a named last order.
  - 0% of "maybe" or "if the price is good".
- **Target price.** The price the buyer states they will pay us: ex-VAT, delivered, in DZD per piece. It must be cross-checked against at least one observed price (shelf tag, invoice or e-shop) for the imported part.

#### GO: all seven must hold
1. **≥3 independent buyers confirm a recurring need**, and at least 2 of them are "Hot" leads by the p3 scoring.
2. **Combined counted annual volume ≥ the model's break-even volume** for that product: `breakeven_volume_pcs_per_year` in `top20_economics.csv`; F.2 for TOP50 items.
3. **Target price ≥ 1.25 × the model's unit cost at resin 300 DZD/kg** (F.2). Recompute the unit cost at the confirmed volume and at the quoted resin price once resin quotes arrive.
4. **Acceptable payment terms:**
   - cash or cheque on delivery;
   - transfer at 30 days or less;
   - or a guaranteed traite (avalisée by a bank) of up to 60 days.

   Open-account credit beyond 30 days does not count toward GO. Public payers with documented arrears (e.g. ENIEM) count only with advance payment.
5. **Tooling recoverable within 12 months, or customer-funded.**
   - Recoverable means the counted volume ≥ the 12-month mold-recovery volume in F.2. That figure equals 2 × the 2-year break-even used in the model.
   - Customer-funded means the customer pays ≥50% of the mold at order, with mold ownership written into the contract.
6. **No entrenched local supplier at low MOQ.**
   - Fails if ≥3 local suppliers already offer the same part at ≤ our target price, with MOQ ≤ the buyer's usual lot and no stock-outs reported.
   - Passes if there are no such suppliers, or if the local supplier has documented stock-outs, colour gaps or lead times over 4 weeks.
7. **Technical fit is confirmed by the measured sample:**
   - shot weight (part × cavities + runner) within the press window: 45–200 g PP on 120 t, or 35–160 g on 100 t;
   - mold width ≤ about 400 mm;
   - the resin can be bought locally. PP and PE always pass. PA6 needs a confirmed stockist, because the files found none in small lots.

#### WAIT: re-test at ALGEST or within 8 weeks
WAIT applies if pain or price is real but one GO condition is short. Typical cases:
- only 1–2 buyers so far;
- counted volume 50–99% of break-even;
- target price 1.0–1.25 × unit cost;
- terms of 31–60 days without a guarantee;
- the resin stockist is unconfirmed (PA6);
- a local supplier exists but with reported stock-outs;
- the dominant size or profile is not yet known (joinery, furniture gauges, fleet models).

Next step for each WAIT: name the missing evidence and the buyer who can give it.

#### KILL: any one is enough
- **No pain.** At least 5 interviews of the right buyer type are done, and none reports a stock-out, MOQ, colour, size, lead-time or price problem, **and** wholesale prices sit at or near the landed import floor (p2 joinery downgrade rule).
- **Volume.** Counted volume < 50% of break-even after all calls in the cluster.
- **Price.** Target price < the model unit cost at resin 300 (margin ≤ 0), or < the unit cost at resin 400.
- **Landed import.** The landed import price at the official rate is < 1.5 × our unit cost and distributors report no availability problem (p2 irrigation rule).
- **Incumbents.** ≥3 local suppliers already supply at low MOQ at or below our price (p2 closures rule: for flip-tops, 5k MOQ at ≤ about 6 DZD).
- **Payment.** Only 60–90+ day open-account terms are on offer, or the buyer has a payment-incident history.
- **Technical.** The measured sample needs more than 120 t (shot or mold size), a second process, certification, or an unscrewing mold that the economics did not include.

### F.2 Product thresholds

**Source of the numbers.**
- The 20 TOP20 rows come from `top20_economics.csv`: unit_cost_base and breakeven_volume_pcs_per_year.
- The TOP50 rows were computed for this note with the same function (`model/economics.py` unit_cost at resin 300, 70% use, 60-day credit). They are not in a data file.
- In both, the unit cost includes mold amortisation over 2 years at the model volume, plus packaging, delivery, selling and credit at a % of price.

**Column definitions.**
- "12-mo mold recovery" = mold landed cost (US$ × 1.25 × 133) ÷ (price − unit cost excluding the mold), at the model price.
- "Passes at model price?" = whether the model's own price (mostly ASSUMPTION) already clears the 1.25× rule.

| ID | Model price (DZD) | Unit cost @300 (DZD) | GO needs target price ≥ | Passes at model price? | Break-even vol/yr | 12-mo mold recovery vol | Mold US$ | Product-specific test (in addition to F.1) |
|---|---|---|---|---|---|---|---|---|
| JC-26 | 12.02 | 9.76 | **12.20** | **No** | 148,654 | 297,309 | 8,000 | Wholesale per 1,000 must be ≥ 12,200 DZD. Assly retail of 21–22.5 DZD/pc suggests room. Ask 3 wholesalers (El Eulma, East Algiers) + 1 precast plant |
| JC-24 | 7.48 | 5.85 | **7.31** | Yes | 208,226 | 416,453 | 7,000 | Needs 120 t. Wholesale ≥ 7.31; Assly retail is 13.6. KILL if wholesale ≤ 5.85 |
| JC-40 | 6.80 | 5.21 | **6.52** | Yes | 165,059 | 330,117 | 7,000 | Third spacer SKU: GO only after JC-24 or JC-26 is GO. Needs 120 t |
| JC-34 | 4.29 | 3.47 | **4.34** | **No** | 323,466 | 646,932 | 9,000 | Wholesale ≥ 4.34 per clip (retail is 7.8). Break-off neck must snap cleanly in 10/10 trials on the measured samples |
| JC-02 | 8.75 | 7.57 | **9.46** | **No** | 147,651 | 295,303 | 8,000 | No DZD price exists: GO requires a field price ≥ 9.46. Universal across ≥2 profile systems (Oxxo + Turkish/aluminium) |
| JC-16 | 11.00 | 8.49 | **10.61** | Yes | 69,837 | 139,673 | 7,000 | GO only if 1–2 profile sizes cover ≥70% of Hammedi sales. Bundle with JC-17 |
| JC-36 | 5.61 | 3.47 | **4.34** | Yes | 191,627 | 383,254 | 8,000 | First confirm what "collier atlas" is (snap clip vs screw clip). KILL if local electrical molders already supply at ≤ 4.34 |
| JC-13 | 5.50 | 3.62 | **4.52** | Yes | 162,264 | 324,529 | 8,000 | GO needs ≥3 joiners or distributors reporting colour or stock gaps (the colour need is still a hypothesis) |
| JC-30 | 15.43 | 7.99 | **9.98** | Yes | 61,760 | 123,519 | 8,000 | GO only if ≥2 of 3 formwork contractors use the 22 mm PVC tube + cone system (not the Chinese D-cone) |
| OS-002 | 13.75 | 5.89 | **7.36** | Yes | 46,635 | 93,271 | 5,750 | KILL if conduit extruders bundle couplers at or near cost |
| OS-010 | 30.25 | 13.34 | **16.67** | Yes | 32,954 | 65,907 | 10,000 | PA6: needs a stockist quote (none found in the files). Pull-out test vs the imported sample. The single 55 DZD retail listing must be confirmed by ≥2 wholesale prices |
| CL-003 | 4.82 | 2.71 | **3.39** | Yes | 0 (uses stock molds) | see CL-001 | 0 | Depends on owning the CL-001/CL-002 molds. GO only if the shampoo maker confirms a 24/410 or 28/410 dispensing need of ≥50k/yr **and** SIPEM has no hinged flip-top at 5–10k MOQ. KILL if ≥3 local suppliers offer one at 5k MOQ at ≤ about 6 DZD |
| IF-39 | 5.00 | 4.35 | **5.44** | **No** | 231,895 | 463,790 | 8,000 | One or two tube gauges must cover ≥60% of buyers' volume |
| IF-40 | 6.00 | 5.07 | **6.34** | **No** | 218,776 | 437,551 | 9,000 | As IF-39. Rectangular 20×40 alone must reach break-even, or run as an insert in a family mold |
| IF-07 | 4.00 | 3.58 | **4.47** | **No** | 171,138 | 342,276 | 6,000 | Sell only as part of the drip family (IF-01/04/08). KILL as a stand-alone item |
| IF-08 | 5.00 | 3.26 | **4.08** | Yes | 158,258 | 316,515 | 7,000 | Distributors must report a pre-season stock-out, or Chinese landed ≥ 1.5 × 3.26 DZD |
| OS-009 | 8.25 | 7.17 | **8.97** | **No** | 161,844 | 323,689 | 11,000 | PA6 stockist + nail-screw cost known. KILL if the sleeve-only price is below 8.97 |
| OS-084 | 13.75 | 11.49 | **14.36** | **No** | 78,613 | 157,226 | 10,000 | ≥3 aftermarket wholesalers name the same plug sizes for the same fleet models |
| IF-01 | 15.00 | 6.20 | **7.75** | Yes | 71,855 | 143,710 | 10,000 | Fits the tape OD of ≥2 local tape makers (Anabib, Medi Goutte, DripGlobe). Pre-season order timing confirmed |
| IF-04 | 10.00 | 5.54 | **6.93** | Yes | 85,475 | 170,951 | 8,000 | As IF-01 |
| JC-17 (TOP50) | UNKNOWN | — | Price needed first | — | — | — | 7,000 | No price anywhere. Get ≥3 DZD prices; evaluate only bundled with JC-16 |
| IF-03 | 15.00 | 11.28 | 14.10 | Yes | 66,780 | 133,560 | 9,000 | Drip family |
| IF-02 | 5.00 | 4.68 | 5.85 | No | 273,821 | 547,642 | 12,000 | Only with IF-01/IF-03 (lock nut) |
| IF-05 | 12.00 | 8.60 | 10.75 | Yes | 93,003 | 186,006 | 10,000 | Drip family |
| IF-06 | 10.00 | 7.57 | 9.47 | Yes | 100,902 | 201,804 | 9,000 | Drip family |
| IF-20 | 20.00 | 20.40 | 25.51 | No | 51,390 | 102,779 | 9,000 | Layflat users must be confirmed (Biskra / El Oued) |
| IF-42 | 5.00 | 3.80 | 4.75 | Yes | 194,538 | 389,077 | 8,000 | Furniture family |
| IF-49 | 12.00 | 11.95 | 14.93 | No | 99,198 | 198,396 | 8,000 | Slat size must dominate |
| IF-46 | 1.00 | 1.92 | 2.40 | No | 1,292,233 | 2,584,467 | 9,000 | Colour-match service only; needs a ≥2.4 DZD price, which is unlikely |
| IF-47 | 1.00 | 2.18 | 2.73 | No | 1,416,990 | 2,833,980 | 11,000 | As IF-46 |
| IF-48 | 1.50 | 2.04 | 2.55 | No | 784,406 | 1,568,812 | 9,000 | As IF-46 |
| CL-001 | 3.86 | 4.69 | 5.86 | No | 598,151 | 1,196,301 | 12,000 | Own-funded stock mold needs about 1.2M pcs in 12 months at 3.86 DZD. In practice: customer-funded mold, or price ≥ 5.86 |
| CL-007 | 2.89 | 3.79 | 4.74 | No | 505,535 | 1,011,071 | 8,000 | Range filler only (p2); never the reason to buy a mold |
| CL-013 | 4.95 | 3.49 | 4.36 | Yes | 180,861 | 361,722 | 8,000 | Shot below the minimum on 80 t (funnel press note): run with more cavities on 100–120 t, or skip |
| OS-039 | 27.50 | 9.76 | 12.20 | Yes | 33,219 | 66,438 | 8,500 | ≥1 OEM integration manager (Samha / Géant / Condor-Hisense) gives a volume + ≥2 installers or after-sales shops |
| OS-051 | 2.75 | 6.34 | 7.92 | No | 1,458,741 | 2,917,481 | 10,000 | Only if real prices are ≥ 7.92 (the model price is an ASSUMPTION) |
| OS-052 | 2.75 | 7.12 | 8.90 | No | 1,256,354 | 2,512,708 | 12,500 | As OS-051 |
| JC-07 | 27.50 | 38.80 | 48.50 | No | 30,300 | 60,601 | 8,000 | Volume of only 20k/yr in the model: GO only if 2–3 dominant slat profiles are confirmed and ≥3 assemblers buy |

**What the table shows:**
- **8 of the 20 TOP20 products fail their own GO price rule at the model price**: JC-26, JC-34, JC-02, IF-39, IF-40, IF-07, OS-009 and OS-084. For these, the field visit must find real wholesale prices above the model assumption, or a cheaper mold (fewer cavities, local maker). Otherwise they cannot pass.
- Every break-even volume is the same order as, or larger than, the model's assumed annual volume (100k–500k pcs). **One or two buyers will never be enough;** each GO needs the volume of a channel (≥3 distributors, or 1 OEM plus 2 distributors).
- **All 20 TOP20 products together** use only **2,254 machine-hours/yr** at model volumes. A two-shift press offers 4,800 h/yr in the model. The press purchase rule (F.4) therefore depends on stacking several GO products.

### F.3 Mold approval rules (gate before any mold money is paid)

| Gate | Rule |
|---|---|
| M0. Product GO | The product has passed F.1/F.2, **or** a customer pays ≥50% of a customer-owned mold |
| M1. Drawing | The drawing is built from the measurement sheet (all cavity numbers measured, min/max). The buyer signs or stamps the critical dimensions and the material. For closures: the neck is verified on the buyer's own bottle |
| M2. Quotes | ≥3 written quotes: ≥2 local (Zerouni, FMPI, Precision Industry, CFM) and ≥1 China. Each states steel grade, cavities, runner type, cycle time, T1 date, warranty shots, repair terms, and that the mold fits the press (width ≤ about 400 mm on 120 t / 380 mm tie-bar on 100 t; shot inside the 45–200 g window) |
| M3. Order conditions | Payment staged 50/40/10 (40 at T1, 10 after sample approval). Contract states: (a) mold ownership; (b) no reuse of the design; (c) NDA (copy risk is high per p3). Plus one of: a signed PO/LOI for ≥3 months of volume, or a customer deposit. China molds only once the bank has confirmed domiciliation (120% provision ≥30 days before shipment) and the 3–4-month lead time is in the plan |
| M4. T1 approval | 5 shots × all cavities measured. All critical dimensions within drawing tolerance; snap and thread features within ±0.05 mm unless the buyer states otherwise. Weight spread ≤ ±2% across cavities. No short shots. Flash ≤ 0.1 mm. Gate vestige does not affect function. Cycle time ≤ quoted + 10%. Functional test on the buyer's real counterpart (rebar, tube, profile, tape, bottle). Flip-tops: hinge life written into the contract (p2), plus ≥300 open/close cycles without cracking and a leak test |
| M5. Customer sample approval | The buyer signs the approved sample (keep 10 pcs per cavity as the master). Then a paid trial order |
| M6. Release | 3 consecutive production lots within tolerance. Only then is the mold invoice balance (10%) paid |

### F.4 Press purchase trigger

**Step 1. Molds first, press second.** A product GO triggers a **mold**, not a press. The first runs go to a subcontractor that runs customer molds: SNK Plastic (Rouiba, 50–650 t) or MIRAF (BBA), under a confidentiality agreement.

**Step 2. Buy the press only when all of the following are true:**
1. **Two GO products from two families.** At least 2 products have reached GO, preferably in different families (e.g. drip fittings + spacers), each with a signed PO/LOI or a paid deposit.
2. **Contribution covers fixed costs and molds.** Confirmed annual contribution before fixed costs, Σ(counted volume × (price − variable cost)), must be ≥ annual fixed cost (12 × 439,000 DZD = **≈5.3 M DZD** in the model's 2-shift `FIXED_MONTHLY`) **plus** the landed cost of the launch molds. **Or:** subcontract runs have used ≥150 machine-hours/month for 3 consecutive months.
3. **Tonnage choice is driven by the GO list.**
   - Buy **120 t** if any GO product needs it: JC-24, JC-40, JC-02 or the CL-001/CL-003 flip-top. 120 t covers 20/20 of the TOP20 and 38/38 of the TOP50.
   - Otherwise **100 t** is enough: it covers 16/20 and 34/38, and saves about US$3,280 landed (`machine_comparison.csv`: 30,600 vs 33,880 US$ without AAPI).
   - Either way, ask for the small-screw option for 1–5 g parts.
4. **Inputs are quoted.** ≥2 written resin quotes (PP homopolymer and HDPE) at ≤ 350 DZD/kg ex-VAT, with the economics re-run at the quoted price. A masterbatch quote. A PA6 stockist if an anchor product is in the GO set.
5. **Site and service are ready.**
   - The site has ≥65 kVA available (the 120 t row in `machine_comparison.csv`).
   - The dealer (AFC/Yizumi, or Plasticolor/Chen Hsong) commits to commissioning and a technician response time.
   - A setter is identified.
6. **Finance is ready.**
   - The domiciliation bank has agreed.
   - The 120% provision is funded at least 30 days before shipment.
   - The AAPI duty exemption status is known.
   - At least 6 months of fixed costs are funded in cash.

**Step 3. If fewer than 2 products are at GO after ALGEST (26 Nov):**
- do not buy the press;
- keep the molds that have passed GO at a subcontractor;
- re-test the WAIT products in the 2027 fair season.

---

## G. Four-week field itinerary

### Calendar assumptions
- **Working week:** Algeria works Sunday to Thursday. Friday and Saturday are the weekend. Saturday mornings are marked optional for markets and private shops (ASSUMPTION: many private wholesalers open on Saturday).
- **1 November** (Revolution Day) is a public holiday.
- **Travel times** are not given because the files hold none. Plan BBA and Sétif as a 4-night trip, and Oran/West as 2–3 nights.

### Fairs with dates in the files

| Fair | Date | Place | Status |
|---|---|---|---|
| **ALGEST (international industrial subcontracting fair)** | **23–25 Nov 2026 (Mon–Wed)** | **SAFEX, Pins Maritimes, Algiers; co-organised by BASTP; www.algest.dz** | **In the plan (Week 4)** |
| Plast Alger & Printpack Alger | 30 Mar–1 Apr 2026 | SAFEX | Past. 2027 edition likely spring; date not confirmed |
| Batimatec | 3–7 May 2026 | SAFEX | Past. Next likely around May 2027 |
| SIPSA-Filaha | 18–21 May 2026 | Pins Maritimes | Past. Next likely May 2027 |
| Cosmetica North Africa (4th ed.) | 21–24 Jan 2026 | SAFEX | Past. Get the 2026 exhibitor list (call #34) |
| FIA (Foire Internationale d'Alger) | 22–27 Jun 2026 | SAFEX | Past |
| SANIST (reverse subcontracting, CACI/SAFEX) | Around April (2025 edition ended 24 Apr) | Algiers | 2027 date to be asked of BASTP/CACI |
| Hassi Messaoud technical days (Sonatrach local manufacturing) | May 2024 edition (81 exhibitors) | Hassi Messaoud | Ask Sonatrach for the next date (call #30) |

### Priority industrial zones (from the files)

| Cluster | Zones |
|---|---|
| East Algiers | ZI Oued Smar; Rouiba / Réghaïa; Dar El Beida / El Hamiz; Bab Ezzouar; Kouba; Tassala El Merdja; Baba Hassen |
| Boumerdès | Hammedi; Ouled Moussa; Khemis El Khechna (ZA n°02); Bordj Menaïel; Ouled Heddadj |
| Blida / Tipaza | Boufarik; Beni Mered; ZA Beni Tamou; Ouled Yaïch; Larbaâ; Bouinane; Guerouaou; Bou Ismaïl |
| Sétif | ZI Sétif; Aïn Arnat; El Eulma ZI (B24); Guedjel; Mezloug |
| Bordj Bou Arréridj | BBA ZI and new ZI; Aïn Taghrout; El Achir |
| West | ZI Es Senia and Bir El Djir (Oran); Zaaroura (Tiaret); ZI Voie A (Sidi Bel Abbès) |
| East coast | Hamadi Krouma (Skikda); El Bouni and El Hadjar (Annaba) |

### Week 0 (Sun 4 – Thu 8 Oct): phone sprint and preparation (desk, not a field week)
- **Phone campaign.**
  - Calls 1–36 (wave 1) and 37–50 (wave 2).
  - Target: 25 meetings booked for Weeks 1–3.
  - Re-dial and correct every recorded contact.
- **Paperwork and kit.**
  - Prepare the supplier administrative file.
  - Order the measurement tools (section D).
  - Print the p3 interview in FR and darja, and the measurement sheet.
- **Fair and buyer lists.**
  - Register for ALGEST with BASTP (call #35).
  - Request the Cosmetica exhibitor list (call #34).
- **Molds and machines.**
  - Send 3 sample-based RFQs to the mold makers (calls 42–45) as soon as the first samples are bought.
  - Send press RFQs (calls 46–48).

### Week 1 (Sun 11 – Thu 15 Oct): East Algiers and Boumerdès (home cluster)

| Day | Where (in order) | Who / what |
|---|---|---|
| Sun 11 | ZI Oued Smar → Dar El Beida / El Hamiz | SIPEM (closures, posing as buyer, #2); 2M Expert (Cosmos press + resin prices, #48); El Hamiz quincaillerie wholesalers (C4: spacers, tile clips, anchors, IRL, pipe-clip samples) |
| Mon 12 | Rouiba / Réghaïa → Bab Ezzouar | EACIM (B27, #27); SNK Plastic (#36: rates, competition check); Henkel Réghaïa (B13; meeting only if booked); Divindus AMM (B28, #28) |
| Tue 13 | Hammedi (full day) | Leader Aluminium (#19, C1) + 4–5 neighbouring accessory shops (C2). Joinery samples: JC-02, JC-13, JC-16, JC-17, JC-07. Note profile sizes and colours |
| Wed 14 | Ouled Moussa → Khemis El Khechna → Bordj Menaïel → Ouled Heddadj | SM Mobilier (B29); Precision Industry (#44); FMPI site (#43); Irriplast (#17, C3); Dhikra Office (B30) |
| Thu 15 | Kouba → Tassala El Merdja → Baba Hassen | AFC Industry / Yizumi (#46); Zerouni Molds (#42); CDTA (reverse engineering and 3D printing for drawings from samples). Evening: enter Week 1 data |
| Sat 17 (optional) | Algiers supermarkets + car-parts traders | Closure shelf audit (30 SKUs, buy 15); aftermarket plug samples (C8) |

### Week 2 (Sun 18 – Thu 22 Oct, + Sat 24 optional): West Algiers, Mitidja/Blida, then Oran and West

| Day | Where (in order) | Who / what |
|---|---|---|
| Sun 18 | Draria → Aïn Benian → Zéralda → Birtouta | PAFIX (#10, C6); DripGlobe (#14); Medi Goutte (#13, B21); Distripol (#39: resin quote); E.C.A Emballages (C7) |
| Mon 19 | Boufarik → Beni Mered → Beni Tamou → Guerouaou | Irrinet (#16, C9) + Boufarik dealers (C10: buy 10 of each drip fitting); Beni Mered furniture-hardware wholesalers (C11); Taif Master Batch (#41); HM Plast (reserve: necks and caps) |
| Tue 20 | Larbaâ → Bouinane → Ouled Yaïch | Labonedjma (#6, B16); Hayat DHC (B14); Laboratoires Venus (B15; ask to see the packaging shop) |
| Wed 21 | Bou Ismaïl → Algiers | Himaplast (#40: masterbatch colour-matching test with 3 samples); afternoon: Univers Détergent (#9, B17) |
| Thu 22 | Oran: ZI Es Senia → Bir El Djir → Seddikia | AB Polymers (#38: resin quote); Etoile Plastique (competitor check; phones as recorded: 041 61 76 86; 0770 91 31 31; 0561 75 75 75; 0661 20 04 65); BRUM (masterbatch and recycled PP/HDPE); Plast Windows Oran (C18); Oran wholesalers (C19); Unilever Oran (B19; only if booked) |
| Sat 24 (optional) | Sidi Bel Abbès (and Tiaret if booked) | Groupe STPM Chiali (#18, B22: pipe-end caps, fittings range). Izdihar PVC, Zaaroura (#21, B2) only with an appointment, otherwise by phone |

### Week 3 (Sun 25 – Thu 29 Oct): BBA, Sétif, El Eulma, then Annaba/Skikda

| Day | Where (in order) | Who / what |
|---|---|---|
| Sun 25 | Aïn Taghrout → BBA ZI → El Achir | Oxxo (#20, B1); BBA joinery accessory shops (C16); Condor (B6), Géant (B5), Condor–Hisense (B4) integration offices if booked; MIRAF (reserve: subcontract molding, competitor) |
| Mon 26 | BBA → Guedjel (Sétif) → Sétif | Appliance after-sales shops (C17); Samha (#33, B7); Brandt (B8); Iris (B9) |
| Tue 27 | Aïn Arnat → ZI Sétif | Anabib Plastiques (#12, B20); Tupol (reserve); Aïn Arnat/Sétif dealers (C14); K-Plast group / I.M.A (B23); ALMOULES / SIPLAST (mold maker, 6-week mold lead time per the files); Sétif tile depots (C15) |
| Wed 28 | El Eulma (full day) | El Eulma wholesale quincaillerie (C12) and electrical wholesalers (C13); CFM Engineering (#45); Cumnewtec (reserve); Soloplast (reserve: necks and caps) |
| Thu 29 | Skikda (Hamadi Krouma) → Annaba (El Bouni, El Hadjar) | Polychimical (#37: resin quote and grades); Decoplast (masterbatch, El Bouni); Sider El Hadjar TSS (#32, B26) only with a confirmed appointment |

### Interlude (Sun 1 – Thu 19 Nov): desk weeks between field weeks
- **Measure every sample bag** (section E), and finish the polymer, cavity and gate fields.
- **Update the data.**
  - Update `opportunities_master.csv` with observed prices, origin, MOQ and pain.
  - Recompute F.2 with the field prices and volumes.
- **Molds.** Send RFQs built from the measured drawings: ≥2 local + ≥1 China per candidate GO product.
- **Inputs and money.**
  - Collect the resin and masterbatch quotes.
  - Get the customs broker readout (#49) and the bank answers (#50).
- **Second-round calls** to WAIT buyers, to fill the missing evidence.
- **Optional South trip (Sun 8 – Tue 10 Nov)**, only if drip fittings are leading: Biskra greenhouse/drip input dealers (C20), ENICAB (B12; reserve call), and El Oued dealers (names to be collected on site).
- **Optional Tizi Ouzou day:** ENIEM (B10; advance payment only) and ENEL Azazga (B11).

### Week 4 (Sun 22 – Thu 26 Nov): ALGEST and decision gate

| Day | Where | Who / what |
|---|---|---|
| Sun 22 | East Algiers / Hammedi | Return to the 3–5 hottest leads with measured samples, drawings and indicative prices. Ask for an LOI, PO or deposit |
| Mon 23 – Wed 25 | **ALGEST, SAFEX (Pins Maritimes)** | BASTP B2B meetings with large buyers that post subcontracting needs. Find the Sonatrach/Sonelgaz local-content stands (#30, #31). Meet mold makers and subcontract molders. Show samples from the measured families. Collect cards for every "names to be collected" cluster |
| Thu 26 | Desk | **Decision gate.** Apply F.1/F.2 product by product (GO / WAIT / KILL), F.3 for each mold, and F.4 for the press. Write the outcome to `funnel_scores.csv` / `opportunities_master.csv` and to a Phase 7 results note |

### Targets for the 4 weeks
- **Interviews:** ≥40, across ≥6 sectors (p3 asks for ≥20 across 6+ sectors before the first mold).
- **Samples:** ≥120 sample bags measured.
- **Prices:** ≥3 observed DZD prices for every TOP20 product.
- **Quotes:** ≥3 resin quotes, ≥6 mold quotes, ≥2 press quotes.
- **Customs:** 1 tariff readout.
- **Outcome:** GO / WAIT / KILL decided for all 20 TOP20 products by 26 Nov 2026.
