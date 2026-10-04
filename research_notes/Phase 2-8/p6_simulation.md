# Phase 6: Market simulation of a one-press entry in Algeria (analyst role-play)

Run date: 2026-10-04. Engine: **structured role-play by one analyst. This is not MiroFish.** Inputs: `mirofish_seed/` (seeds 01–07, `personas.md`, `scenarios.md`), `data/top20_economics.csv`, `data/machine_comparison.csv`, `data/economics_killed.csv`, `model/economics.py`, `p3_buyer_behavior.md`. Calculator: `model/sim_calcs.py`, which reproduces every number below when run with `python3 model/sim_calcs.py`.

> **Everything in sections 2–4 is a SIMULATED OUTCOME.** None of it is evidence. A simulated outcome can justify a field question; it cannot justify a conclusion in a later report. Any behaviour taken from a persona attribute tagged `[ASSUMPTION]` is marked **(A)**. Behaviour backed by a seed fact is marked **(E: seed §)**.

---

## 1. Method and limits

**Why this is not MiroFish.** MiroFish needs the founder's own LLM key, a Zep key and network access. This environment had none of these. The founder can still run the seed package later (see `mirofish_seed/README.md`). This document is the transparent fallback: one analyst plays all 21 persona cards against each of the 15 scenarios.

**Procedure. Each scenario was run the same way:**
1. **Rounds.** The scenario was played at month 0, 3, 6, 12 and 18/24. Month 0 is Nov 2026.
2. **Persona actions.** In each round I wrote down what each driving persona does and why. The "why" comes from that persona's card: its incentives, fears, payment habits, switching triggers and propensity to copy.
3. **Numbers.** Where money matters, the persona decisions (accounts won, volumes, prices, terms, stoppage days) were converted into figures with `sim_calcs.py`. That script imports the functions and parameters of `economics.py` unchanged:
   - FX 133 DZD/USD; 400 clock-hours a month on 2 shifts, with OEE 0.85 applied inside parts per hour;
   - fixed costs 439k DZD/month plus 120k founder and overhead, so **559k DZD/month in cash**;
   - power 90 DZD per running hour;
   - resin base case 300 DZD/kg, molds landed at 1.25 × FOB, credit cost 8% a year.
4. **Variants.** At least two variants were run wherever the persona assumptions are weakest. The summary table says whether the outcome holds under both.
5. **Evidence check.** Each simulated behaviour was compared with the seeds. Where it conflicted, I adjusted the behaviour, re-ran that step and recorded the change ("**Adjusted:**").

**Additional simulation inputs (all ASSUMPTION).**
- **Changeover time:** 3.0 h for a full mold change and 0.75 h for an insert swap. The vendor claims under 5 minutes for inserts (S07); I added time for purging and the first-article check.
- **Account size at steady state:** 15–25k pcs/month per account. The first month is a trial order at 30% of that.
- **Drip-fitting demand:** seasonal profile, peaking Nov–Jan.
- **Flip-top mold:** USD 8k, with a 1 h colour purge plus 3 kg of purged resin at each colour change.
- **Insert frames:** USD 9k each; each insert costs 40% of a full mold.
- **Subcontracting:** 3,000 DZD/h.

**Product correction.** The baseline packer price of 3.5 DZD is a flat-packer price. The model already kills that part: JC-01 is in `economics_killed.csv` even at 5.79 DZD. The packer used in this simulation is therefore the bridge packer JC-02 at 8.75 DZD.

**Limits.**
- One analyst plays every actor. That builds in consistency bias and leaves out any emergent behaviour between agents.
- All buyer behaviour on switching, trust, tooling and credit days is **(A)**. Seed 05 and P3 report almost no Algerian behavioural evidence on these points.
- All prices and volumes in the model are ASSUMPTION or retail-derived. The only exceptions are the spacer and tile-clip prices, which are STRONG SIGNAL.
- The cash figures exclude VAT timing, AAPI savings and the founder's salary beyond the 120k overhead line.

---

## 2. Summary table (SIMULATED OUTCOMES)

| # | Scenario | Key SIMULATED OUTCOME | Holds under both variants? | Implication for strategy |
|---|---|---|---|---|
| 1 | Quiet entry | **With an introduction and a wholesaler channel:** 48 / 107 / 150 h a month reached at months 6 / 11 / 16; utilisation 28% at month 12; peak cash need **11.6 M DZD** including press and 3 molds. **Without an introduction:** 107 h is not reached by month 18. | Yes on direction; timing depends heavily on the introduction | Get an introduction before the press lands. Keep subcontract-first until about 107–150 h is ordered |
| 2 | Flip-top caps | Margin is 13–19% at 4.82 DZD. A 5k-per-colour minimum adds 0.40 DZD a cap. Only **1–3 brands adopt by month 12** when a SIPEM-like incumbent exists, versus 3–6 when it does not. Filling 100 h needs about 230k caps a month | Fragile | Treat caps as a short-run colour service sold through a blower, not as a volume line |
| 3 | Copy at month 6 | A new copycat entrant loses money: −58% to −105% full margin at 15% utilisation. **The real copier is an incumbent with idle presses**, which still earns 40–53% over its marginal cost after a 30% cut | Yes | Defend through service, contracts and control of the molds. Do not try to win on price |
| 4 | 3 → 10 → 20 molds | 3 spacer-led molds cannot cover fixed costs even at the planned volumes. 10 molds use 36–49% of the press; 20 molds use 51–77%. Make-to-order with full molds wastes **120 h a month (30% of capacity)** on changeovers. A second press needs **≥1.3× planned volume** with 20 molds | Yes | Use insert frames from about mold 6 onwards. Hold 2–4 weeks of stock. Do not plan a second press within 18 months |
| 5 | Imports tighten | Protection raises the price umbrella by about 44% (DAPS). The binding constraint becomes **mold lead time (3–4 months), not press hours**. Traders approach the founder as distributors | Yes | Keep 2–3 spare molds' worth of designs ready and line up a local mold maker |
| 6 | Resin +20/50/100% | At +50% no SKU loses money, but 10 of 20 fall below 15% margin. At +100%, **6 go negative** (spacers, tile clips, bridge packer, furniture inserts). An 8-week buffer costs 0.57 M DZD and pays back 6× in a single +50% event | Yes | Use resin-indexed price clauses. Carry a 4–8 week buffer. Weight the mix toward drip fittings, anchors and conduit parts |
| 7 | Imports ease | At official FX the spacer wheel lands at **2.4–3.6 DZD**, against a full cost of 5.85. Spacer volume falls 30–60%. Drip fittings, caps and custom parts hold if service is good | Fragile for spacers; holds for custom parts | Do not build the business on catalogue items whose only edge is price |
| 8 | 60/90-day credit | At 1.5 M DZD monthly revenue, receivables are **1.8 M** (60% of sales at 60 days) to **4.05 M** (90% at 90 days). A 15% bounce rate eats 11–17% of gross contribution | Yes | Use traites and cap each customer at one month of purchases. Refuse terms longer than 60 days to public buyers |
| 9 | Press down 2/7/30 days | Lost contribution is 22–36k DZD a day. **A 30-day stop loses accounts worth about 0.1 M DZD a month each, for about 6 months.** A dealer-backed press stops for 7 days or less | Yes | Buy through a dealer with local technicians, keep a spares kit and 2 weeks of stock, and pre-qualify an SNK-like subcontractor as backup |
| 10 | Location | **East Algiers–Boumerdès is fastest to first customers and support but has the most copiers.** BBA/Sétif is second. Oran is last | Yes | Choose East Algiers–Boumerdès, with copy defences in place from day 1 |
| 11 | Customer funds mold | Groups accept funding of 50% at order and 50% at sample approval. Owner-led SMEs mostly refuse. **Saves 1.0–1.8 M DZD per part.** The 120% bank provision opens a 1–2 month cash gap | Yes on the split between buyer types | Use a two-tier tooling policy |
| 12 | Founder funds molds | 7 of 19 molds pay back within 12 months; all pay back within about 21 months at planned volumes. A 10–20% price premium recovers almost no mold within 12 months (the premium needed is 31–125%). **10 molds = 12.5 M DZD** | Yes | Fund only universal stock molds, assume a 2-year life, and stop at 3–6 molds in year 1 |
| 13 | Exclusive anchor | With the anchor at 50% of revenue on 90-day terms, receivables reach 2.25 M DZD, and a 90-day slip doubles that. When exclusivity ends, a group with a captive shop **moves the part in-house** | Fragile when the anchor share is ≥50% | Keep the anchor at ≤30% of revenue. Limit exclusivity to 12–24 months and tie it to a minimum quantity backed by traites |
| 14 | Catalogue-lite | **Tooling (12.5–37 M DZD), not stock (0.3–1.9 M), limits catalogue size.** Wholesalers stay because of margin, not availability (no scarcity signal for spacers) | Yes | Start with 10 SKUs on inserts. Grow the catalogue from sell-through data |
| 15 | Price war | An incumbent's cash floor is 45% below spacer prices, so it can sustain the war and **does not need to raise prices again**. Over 12 months the founder's cash cost is −1.8 M (match a 20% cut) to −3.6 M (match a 40% cut). Exiting without other work to redeploy the press costs −5.8 M | Yes | Match 20% cuts. Answer 30–40% cuts with a partial match plus service. Keep high-contribution families as ballast |

---

## 3. Scenario write-ups (SIMULATED OUTCOMES)

### S1. Quiet one-machine entry
**Variants:**
- **A.** Spacers, sold direct, no introduction, priced about 20% under street prices.
- **B.** Spacers and packers through 2 wholesalers, with an introduction ("maarifa") from the resin distributor.
- **C.** Drip fittings through a tube maker.
- **D.** Flip-top caps sold direct to brands.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m0** | The hardware wholesaler and the joinery distributor ask for samples. Neither orders before seeing stock. | (A) |
| **m3** | In B, the wholesaler places a trial order, paid by cheque on delivery. Reason given: the shelf margin between the founder's 7.48–12.02 DZD and the retail price of 13.6 DZD for the 30-mm wheel. In A, there is still no order: owners do not receive unknown visitors. | Payment by cheque on delivery (E: S05 §2); retail price (E: S04 §3); refusal of visitors (A) |
| **m6** | B reaches 59 h a month. The machine distributor tells another buyer that "a new 120 t is running spacers". | (A) |
| **m12** | B reaches 114 h (28% utilisation) and 1.10 M DZD of revenue. The first reorder came in month 3, and the wholesaler now asks for 30 days. | 30-day request (A) |
| **m18** | B reaches 167 h. | — |

**Computed results:**

| Variant | Hours a month at m6 / m12 / m18 | Months to 48 / 107 / 150 h | Operating-cash trough (excl. capex) | Peak cash need (incl. 8.25 M press + 3 molds) |
|---|---|---|---|---|
| A | 26 / 68 / 104 | 10 / not reached / not reached | −5.4 M | 14.1 M DZD |
| B | 59 / 114 / 167 | 6 / 11 / 16 | −2.8 M | 11.6 M DZD (≈USD 87k) |
| C | 5 / 21 / 16 | none reached | −3.7 M | 12.2 M |
| D | 11 / 33 / 54 | 18 / not reached / not reached | −7.5 M | 16.0 M |

Variant C uses very few hours, yet its contribution covers fixed costs by month 12. That happens only because the drip prices of 10–15 DZD are ASSUMPTION; drip fittings earn 30–40k DZD per hour, against about 5k for spacers. Break-even if spacers were the only product is **111–118 h a month**, and covering fixed costs needs about 85k spacer chairs a month.

**Robustness.**
- The ranking B > A holds under both stances on introductions.
- Timing depends on the introduction (A).
- The project's peak-cash estimate of 6.2 M DZD assumed subcontracting first. Committing to the press at m0 roughly doubles the peak need.

**Evidence check.**
- Payment by cheque or cash on delivery is *consistent* (S05 §2).
- No named wholesaler and no stated buyer pain were found (S04): the speed of adoption has *no evidence*.
- **Adjusted:** my first pass had the wholesaler adopt for availability. Seed 04 §3 says spacers are in stock on several e-shops, with no sign of scarcity. I re-ran the step with adoption driven by margin, which pushed the first reorder from m2 to m3. The figures above already include this change.
- **Field question:** "What margin does a wholesaler need to put a new local spacer brand next to the imported one?"

### S2. Shampoo and dispensing-cap niche
**Variants:** minimum per colour of 5k, 10k or 20k caps; SIPEM-like incumbent present or absent; 2% hinge failures in month 3 or no defects.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m0** | The shampoo owner asks first for the neck size. The founder needs the bottle blower to confirm it. | Neck specs undocumented (E: S04 [UNKNOWN]) |
| **m3** | Two brands test caps on their filling lines. The blower co-sells caps if they fit and are cheaper than the trader's set. | (A) |
| **m6** | **Hinge-failure variant:** one brand drops the cap and returns to the trader set, keeping it as its backup. | (A) |
| **m12** | With no incumbent and no defects: 3–6 brands. With a SIPEM-like incumbent: 1–3 brands, because the blower already has a source. | (A) |

No brand offers to fund a custom mold: the shampoo owner's card has low cash and does not want to tie it up in a mold (A).

**Computed results:**
- At 4.82 DZD the margin is 13.1% / 17.2% / 19.3% with a 5k / 10k / 20k minimum per colour. At 4.0 DZD the line roughly breaks even.
- Landed import price at FOB USD 0.012–0.045:

| FX basis | Landed price per cap |
|---|---|
| Official | 2.8–10.7 DZD |
| Parallel | 5.1–19.3 DZD |

- Filling 100 h a month needs about **230k caps a month**, roughly 10 or more small brands.

**Robustness.** The line pays only at prices of 5 DZD or more, sold to buyers who price against parallel-FX imports. The outcome does not hold in the incumbent-present variant.

**Evidence check.**
- The founder anecdote is a WEAK SIGNAL, and no flip-top maker was indexed.
- **Adjusted:** my first pass treated the niche as empty. SIPEM's dispenser-cap claim is a STRONG SIGNAL (S02 §2), so the incumbent-present run is the base case. Adoption fell from 3–6 brands to 1–3.
- **Field question:** "Ask 3 blowers which neck sizes they ship most and where their caps come from."

### S3. A competitor copies after 6 months
**Variants:** the copied part is a catalogue SKU or one customer's drawing; the copier cuts price by 10%, 20% or 30%; the copier is a new entrant or an incumbent.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m6** | The copycat buys a JC-24 sample from a wholesaler shelf. A local mold maker offers a copy mold in 6 weeks. | Mold makers produce parts "from models" (E: S02 §6) |
| **m9** | The wholesaler takes the copy at −20% as a second source. | Keeps several sources (A) |
| **m12** | The founder keeps about 60% of the SKU if it holds price and adds 48-hour delivery, against about 85% if it matches. | (A) |
| **m18** | The new-entrant copier has not filled its press and stops cutting. | — |

**Computed results.**
- A new copycat with 1–2 SKUs at about 15% utilisation runs a full margin of −58% (10% cut) to −105% (30% cut) on JC-24/JC-26. It would need about 125k JC-26 a month just to break even.
- An **incumbent** pricing at marginal cost keeps a 40–53% margin even after a 30% cut.
- If the founder matches, its own full margin at 70% utilisation falls to 1.5% (JC-26) or 5.3% (JC-24) at −20%, and turns negative at −30%.

**Robustness.**
- The sustainability result holds in both variants.
- A part made to one customer's drawing is copied less, because the buyer guards its drawing (A). It is still exposed if the buyer hands the mold to someone else (S11).

**Evidence check.**
- Copying capability is *consistent* (S02 §6), and the IP index is VERIFIED.
- No copying case is documented: *no evidence*.
- **Adjusted:** the scenario's own setup (a new entrant with the same press) proved economically weak. I re-ran with the SNK-like incumbent as copier, which is the persona with the "#1 copying threat" (A). Copying pressure then becomes permanent instead of fading by m18.
- **Field question:** "Ask mold makers how often clients bring a competitor's part to copy."

### S4. 3 → 10 → 20 molds on one press
**Variants:** full molds vs insert frames; make-to-order vs stocked; molds from China vs local.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m0–m3** | The bank officer requires the 120% provision 30 days before each shipment. | (E: S01 §4) |
| **m6** | Buyers ask for a second colour or size. | (A) |
| **m9** | 10 molds. Batching imports to fewer events locks **9.1 M DZD** in provisions. | — |
| **m18** | 20 molds. | — |

**Computed results.** Volumes are the planned volumes in `top20_economics.csv`.

| Molds | Running hours a month | Changeover hours: full molds (make-to-order / stocked) | Changeover hours: inserts (make-to-order / stocked) | Press occupied | Gross contribution vs 559k fixed | Mold cash: full vs insert |
|---|---|---|---|---|---|---|
| 3 | 82 | 18 / 9 | 4 / 2 | 21–25% | **0.45 M (below fixed)** | 3.7 M vs 4.5 M |
| 10 | 137 | 60 / 30 | 15 / 8 | 36–49% | 1.38 M | 12.6 M vs 8.0 M |
| 20 | 188 | 120 / 60 | 30 / 15 | 51–77% | 2.61 M | 26.7 M vs 16.7 M |

- All 20 top SKUs together use only **47% of the press**.
- Press 1 passes 75% utilisation (the rule for a second press) only at **1.28× the planned volume with 20 molds, or 1.97× with 10**.
- Insert frames cost more at 3 molds and save 37% from 10 molds up.

**Robustness.** The direction holds in all four variants. Local molds (6 weeks) remove the provision cost but not the cost of the mold itself.

**Evidence check.**
- Provision timing is *consistent* (VERIFIED).
- Insert changeover time is a vendor claim. **Adjusted:** I used 0.75 h instead of the claimed 5 minutes.
- Under the rule "utilisation dominates unit cost" (S06 A), the 3-mold start is the weak point.
- **Field question:** "Ask 2 local mold makers for a price on inserts for a standard frame."

### S5. Import restrictions on finished parts tighten
**Variants:** mild (DAPS extended to 3925/3926.90) or severe (DAPS plus PPI refusals plus a crackdown on cabas); one press only, or with overflow to a subcontractor.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m3** | The import trader cannot renew its PPI line. The wholesaler loses its imported packers. | PPI and domiciliation rules (E: S01 §4–5) |
| **m4** | Enquiries double. | (A) |
| **m6** | Two traders offer to distribute the founder's parts. | (A) |
| **m6** | A copycat enters with a mold made from a sample. | (A) |
| **m12** | The founder raises prices 10–15% and buyers accept, because the alternative is no supply. | (A) |

**Computed results.**
- DAPS at 60% raises the officially landed price by about 44%: JC-24 goes from 2.4–3.6 to 3.4–5.1 DZD, and caps from 2.8–10.7 to 4.1–15.4.
- Even path B's demand doubled (228 h) fits within the 400 h available.
- The constraint is the **3–4 months from purchase order to mold on the floor**. In the severe variant, the founder's own mold and resin imports also need a PPI line.

**Robustness.**
- Mild variant: the founder gains.
- Severe variant: the gains are capped by mold lead time, and some of them go to the copycat.

**Evidence check.**
- The Algex 2022 shortages and the 2021 resin stoppage are *consistent* with input imports also being blocked.
- **Adjusted:** the first pass let the founder scale freely. I re-ran it with the founder's own imports under the same PPI and domiciliation friction.
- **Field question:** "Ask a customs broker for the DAPS status of HS 3925/3926.90/3917."

### S6. Resin up 20%, 50% or 100%
**Variants:** price rise only, or rationing with 2-week gaps; buffer of 0, 4 or 8 weeks; fixed price or resin-indexed clause.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m4** | The resin distributor asks for cash and limits lots for new molders. | (A) |
| **m5** | Construction wholesalers refuse rises above about 10% and threaten to go back to imports. | (A) |
| **m5** | The irrigation tube maker accepts a rise if supply before the season is assured. | (A) |
| **m6** | The incumbent passes the rise through. | (A) |
| **m6** | Importers face the same world prices, so the price umbrella moves up partly. | World PP +38% (E: S03 §3) |

**Computed results.** Full margin at 70% utilisation, top-20 SKUs:

| Resin price (DZD/kg) | SKUs with negative margin | SKUs below 15% margin |
|---|---|---|
| 300 | 0 | 4 |
| 360 | 0 | 7 |
| 450 | 0 | 10 |
| 600 | 6 | 11 |

- At 600 DZD/kg the negative SKUs are JC-26 (−12%), JC-24, JC-34, JC-02, IF-39 and IF-40.
- To hold margin at +100%, spacers need about 30% higher prices. Drip fittings, anchors and conduit couplers need under 10%.
- The 8-week buffer is 1.9 t of resin, worth 0.57 M DZD. It costs 43k DZD a year to carry and gains 0.28 M DZD in a single +50% event.

**Robustness.**
- In the rationing variant, the 0-week buffer stops the press for 2 weeks. The 4–8 week buffers avoid any stop.
- The resin-indexed clause keeps margin, but construction buyers resist it (A).

**Evidence check.**
- The 2021 crisis (×3, plants stopped for months) is *consistent* with the rationing run being the relevant one. A tripling would kill every spacer line.
- **Adjusted:** the first pass assumed price-only availability. The 2021 precedent is VERIFIED, so rationing is now the stress case.
- **Field question:** "Ask the distributor which origin a lot comes from, and whether it can hold 1–2 t for the founder."

### S7. Chinese imports become easier
**Variants:** duty cut from 30% to 15% only; or all easing measures plus wider official FX for traders.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m6** | The import trader restocks Chinese spacers and packers at official FX. | (A) |
| **m9** | The wholesaler, which is driven by price, moves 30–60% of its spacer volume back to imports. | (A) |
| **m9** | The irrigation tube maker stays, because of fit, fitting availability before the season, and a local invoice. | (A) |
| **m12** | Procurement managers stay, because they need to show local integration. | (E: S01 §1, P3 §1) |

**Computed results.**

| Part | Founder's full cost | Landed at official FX today (DD 30%) | Landed at official FX with DD 15% |
|---|---|---|---|
| Spacer wheel JC-24 | 5.85 | 2.4–3.6 | 2.1–3.2 |
| Drip coupling IF-04 | 5.54 | 2.4–7.1 | 2.1–6.3 |
| Flip-top cap | 2.71 | 2.8–10.7 | — |

- Spacer-wheel pricing survives today only through import friction and the importer's margin.
- The drip coupling and the flip-top cap still have room against the mid and high FOB range.

**Robustness.** Spacers fail in both variants. Custom and fit-critical parts hold.

**Evidence check.**
- No relaxation was found (STRONG SIGNAL), so this is a low-probability scenario.
- The seed assumption that "the local molder competes with the importer's margin" is *consistent* with the result.
- The freight factor of 1.2 may understate shipping costs for bulky spacers: *no evidence*.
- **Field question:** "Ask a wholesaler for its landed cost per 1,000 imported spacers."

### S8. Customers demand 60- or 90-day credit
**Variants:** 30%, 60% or 90% of revenue affected; bounce rate 0%, 5% or 15%; founder accepts the terms, refuses them, or accepts only with a traite and a cap.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m3** | Wholesalers ask for 60 days on post-dated cheques. | (A) |
| **m3** | Wholesalers' cash is tight after the cash-deposit ban. | (E: S05 §2) |
| **m6** | The public furniture maker offers 90 days or more on tender payment. | (A) |
| **m6** | **Refuse variant:** 1 of 2 wholesalers leaves for an importer that offers credit. | (A) |
| **m12** | **Cap variant (a traite and at most one month of a customer's purchases outstanding):** both wholesalers stay, at 45 days. | (A) |

**Computed results.**
- Receivables at 1.5 M DZD monthly revenue:

| Share of sales on credit | 60 days | 90 days |
|---|---|---|
| 60% | 1.8 M DZD | 2.7 M DZD |
| 90% | 2.7 M DZD | 4.05 M DZD (≈7 months of fixed costs) |

- Overdraft interest is only 135–304k DZD a year. **The constraint is access to a credit line, not its price.**
- With 50% of bounced amounts recovered, a 15% bounce rate costs 0.8–1.2 M DZD a year (11–17% of gross contribution). A 5% bounce rate costs 4–6%.

**Robustness.** The cap policy is the best response in both the 5% and the 15% bounce cases.

**Evidence check.**
- The criminal cheque regime and public payment delays are *consistent*.
- **Adjusted:** the first pass had public buyers paying at 90 days. ENIEM's record and the 130 bn DZD of public arrears are STRONG/VERIFIED, so I re-ran the public furniture variant at 180 days or more. The result: serve public buyers only on advance payment.
- **Field question:** "Ask what instrument and how many days you paid your last plastics supplier."

### S9. The press fails for 2, 7 or 30 days in month 8
**Variants:**
- **Cause:** heater (spare part on hand), controller board, or pump.
- **Purchase route:** through a dealer, or imported directly.
- **Finished stock:** 0, 2 or 4 weeks.

**Rounds:**

| Day | What happens | Basis |
|---|---|---|
| **d0** | The wholesaler calls. | — |
| **d3** | With no stock, the irrigation tube maker activates its import source, mid-season. | (A) |
| **d7** | A dealer technician fixes the press if it was bought through the dealer. | AFC commissioning capability (E: S02 §4) |
| **d7** | With a direct import, a freelance technician is still being found. | No repair business exists (E: S02 [UNKNOWN]) |
| **d30** | Two accounts have moved to the backup source. One returns after 2 months; the other is lost. | (A) |

**Computed results.**
- At 120 h a month, a stop loses 43k / 151k / 648k DZD of contribution over 2 / 7 / 30 days. Fixed costs of 22k DZD a day keep running.
- Subcontracting the gap at 3,000 DZD/h costs 0.12 M DZD for 7 days and 0.50 M for 30 days.
- 2 weeks of finished stock costs about 0.2 M DZD.
- **A lost 25k-a-month spacer account is worth about 106k DZD a month in contribution.**

**Robustness.**
- Money lost to downtime is small in every variant. The lost customers are the real cost.
- With a dealer purchase plus 2 weeks of stock, the 7-day case loses no accounts.

**Evidence check.**
- **Adjusted:** the "controller board in 1–3 weeks" assumption conflicts with seed 01 §4. Commercial express shipments are reserved for registered importers, a broker is needed, and domiciliation still applies. I re-ran the stop at 3–6 weeks unless the dealer holds the board in stock.
- **Field question:** "Ask AFC-like dealers which spare parts they keep in Algeria."

### S10. Location: Algiers vs Sétif–El Eulma vs BBA vs Oran
Distances below are general geography, not seed data (A). Rent is UNKNOWN in every location.

| Location | Time to first 5 customers | Support for molds and the machine | Exposure to copying | Resin | Families that fit |
|---|---|---|---|---|---|
| East Algiers–Boumerdès | **Fastest (≈m6).** Hammedi joinery cluster; Blida/Algiers cosmetics; furniture makers in Rouiba | Best: dealers in Kouba and Oued Smar, local mold makers | **Highest** (SNK, SIPEM, informal shops) | Distripol, Zéralda | Packers, caps, furniture, spacers |
| Sétif–El Eulma | ≈m8. Tube makers in Aïn Arnat; blowers | Good: ALMOULES, CFM | Medium; the big players there are captive | Skikda, about 200 km away (A) | Drip fittings, caps through blowers |
| BBA | ≈m9. Oxxo; appliance makers | Medium | Medium (MIRAF) | Skikda | Joinery supplied to plants, appliance spares |
| Oran | ≈m12. Commodity molders only on record | Weak | Low on record (directories under-count) | AB Polymers, Es Senia | Unclear |

**Robustness.** East Algiers–Boumerdès ranks first under both a "copying matters" weighting and a "speed matters" weighting. Sétif ranks first only for a drip-led entry.

**Evidence check.** The cluster map and the Oran evidence are *consistent* (S02 §1). There is *no evidence* on rent or delivery costs.

### S11. The customer funds the mold
**Variants:** 50% at order + 50% at sample approval, or 30% upfront with the rest amortised over pieces; owner-led SME or group buyer; free removal of the mold or a buy-out fee.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m1** | The group procurement manager accepts 50/50, because its QA process expects owned tooling. | (A) |
| **m1** | The shampoo owner refuses: "you are the molder". | (A) |
| **m1** | The detergent manufacturer accepts 30% upfront plus amortisation. | (A) |
| **m4** | The Chinese mold maker asks for its 30–50% deposit. The bank needs the 120% provision 30 days before shipment, so the founder pre-funds for about 1–2 months. | Mold-maker deposit (E: S06 §3); provision rule (E: S01 §4) |
| **m12** | In the free-removal variant, one SME moves its mold to a cheaper molder. | (A) |

**Computed results.** Each customer-funded part avoids 1.0–1.8 M DZD of capex. Launches roughly double for group buyers. SME launches stay flat.

**Robustness.**
- The split by buyer type holds in both variants.
- The buy-out fee with notice period prevents molds from leaving.

**Evidence check.**
- Algerian tooling norms are UNKNOWN. The China split of 50/40/10 is VERIFIED.
- **Adjusted:** the first pass ignored how the bank treats a mold deposit made before shipment (UNKNOWN). I re-ran the cash timing with the provision fully pre-funded.
- **Field question:** P3 Q14–15.

### S12. The founder funds the mold
**Variants:** 3, 6 or 10 molds in year 1; price premium 0% or 20%; financed by overdraft or leasing.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m3** | Buyers reject a 20% premium on spacers. | Price sensitivity (A) |
| **m9** | 3 of 10 molds have barely run, because demand is long-tail. | (A) |
| **m12** | A copycat targets the founder's best-selling mold design. | (A) |

**Computed results.**
- 7 of 19 molds pay back within 12 months after absorbing fixed costs; all 19 pay back within about 21 months. The fastest are OS-002 and IF-01 (about 6 months).
- Recovering a mold within 12 months would need a 31–125% price premium.
- Mold capex is 3.7 M / 7.5 M / 12.5 M DZD for 3 / 6 / 10 molds. On 10 molds, overdraft interest is 0.94 M DZD a year and leasing is 1.26 M.

**Robustness.** The 10-mold variant creates the cash trough in both financing variants.

**Evidence check.**
- Mold prices and interest rates are VERIFIED.
- "Mold amortisation dominates at low volume" is *consistent*.
- No adjustment was needed.

### S13. An exclusive customer mold
**Variants:** anchor at 30%, 50% or 70% of revenue; paying at 60 or 90 days; exclusivity of 12 months or unlimited.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m0** | A group buyer under pressure to raise local integration funds the mold. | Integration targets (E: S04 §6) |
| **m9** | Payment slips by 30–60 days. | (A) |
| **m12–24** | At the end of exclusivity, the group re-tenders or moves the part to its captive shop. | Captive molding (E: S02 §2, Condor/Brandt) |

**Computed results.**

| Anchor share of revenue | Receivable at 60 days | Receivable at 90 days | Contribution lost if the anchor halves volume |
|---|---|---|---|
| 30% | 0.9 M DZD | 1.35 M DZD | 90k DZD a month |
| 50% | 1.5 M DZD | 2.25 M DZD | 150k DZD a month |
| 70% | 2.1 M DZD | 3.15 M DZD | 210k DZD a month |

A 90-day slip adds 1.35–3.15 M DZD to receivables.

**Robustness.**
- At a 30% anchor share the founder survives both a delay and a volume cut.
- At 70% it does not, without new credit.

**Evidence check.**
- The Shaily–IKEA pattern (about 50% anchor) is *consistent*. Public payment delays are *consistent*.
- **Adjusted:** the first pass assumed renewal when exclusivity ended. The VERIFIED make-vs-buy cases led me to re-run it with the part moved in-house.

### S14. A standard catalogue product
**Variants:** 10 or 30 SKUs; 2 or 8 weeks of stock; 2 or 6 wholesalers.

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m2** | Wholesalers take free samples and a PDF catalogue. | (A) |
| **m6** | 4 of 10 SKUs carry 70% of sales. | (A) |
| **m6** | With 6 wholesalers, they undercut one another and two stop stocking. | (A) |
| **m9** | A copycat copies the best seller. | (A) |
| **m12** | A 10-SKU catalogue grows to 12. A 30-SKU catalogue shrinks to about 15. | (A) |

**Computed results.**
- Stock at 2–8 weeks of cover: 0.29–1.16 M DZD for 10 SKUs; 0.48–1.94 M DZD for 30 SKUs.
- Tooling: 12.5 M DZD (full molds) or 8.0 M (inserts) for 10 SKUs; 37.4 M or 23.9 M for 30 SKUs.

**Robustness.** Tooling is the binding constraint in every variant.

**Evidence check.** The Caplugs/Essentra analogy is *consistent* only for a library already paid off.
- **Adjusted:** the first pass made wholesalers loyal for availability. Seed 04 says spacers and tile clips are in stock everywhere, so I re-ran loyalty as margin-driven. That cut the base case from 6 wholesalers to 2–3.

### S15. A competitor price war at month 8
**Variants:**
- **Attacker:** an incumbent or a copycat.
- **Price cut:** 20%, 30% or 40%.
- **Duration:** 3, 6 or 12 months.
- **Founder response:** one of four (see the table below).

**Rounds:**

| Month | What happens | Basis |
|---|---|---|
| **m8** | The SNK-like incumbent cuts spacer prices to fill idle presses. | Cuts to keep repeat parts (A) |
| **m9** | The wholesaler switches half its volume. | (A) |
| **m9** | The procurement manager does not switch, because changing suppliers costs it a QA requalification. | (A) |
| **m14** | The copycat attacker quits. The incumbent stays down. | — |

**Computed results.**
- The incumbent's cash floor (no depreciation or interest) is 6.63 DZD for JC-26 and 4.06 DZD for JC-24, **about 45% below list price**. A cut of 40% or less is therefore sustainable for it.
- Drip fittings keep 57–78% of their contribution per hour even after cuts.
- Extra cash cost to the founder over 12 months, by response:

| Founder response | 20% cut | 30% cut | 40% cut |
|---|---|---|---|
| Match | −1.81 M DZD | −2.72 M | −3.63 M |
| Partial match + service | −2.13 M | −2.47 M | −2.81 M |
| Hold price with contracts | −2.32 M | −3.48 M | −3.48 M |
| Exit the family, with no other work for the press | −5.79 M | −5.79 M | −5.79 M |

Over 3 months the costs are 0.4–1.2 M DZD.

**Robustness.**
- A copycat attacker always fades within 6 months. An incumbent attacker does not.

**Evidence check.**
- Household plastics are already a long-running price war (WEAK SIGNAL), *consistent* with the incumbent staying down.
- **Adjusted:** the first pass had the incumbent raise prices again after 6 months. That was changed to "stays down".

---

## 4. Strategy stress-test conclusions (from SIMULATED OUTCOMES, to be field-tested)

### Robust choices (hold in most scenarios and variants)
1. **Own machine as the end state, not the day-0 commitment.**
   - Owning the press is what makes it possible to:
     - keep molds in-house (S3, S11);
     - control downtime (S9);
     - absorb a protection windfall (S5).
   - Committing at m0, before orders exist, roughly doubles peak cash to 11.6–16 M DZD (S1).
   - Keep the project rule: buy when at least 107–150 h a month of recurring orders exist, or the cash peak is covered.
2. **Insert-based mold families from about mold 6 onwards.**
   - They save 37% of tooling cash at 10–20 molds.
   - They cut changeovers from 120 h to 15–30 h a month (S4, S14).
   - At 3 molds they cost more, so start with full molds.
3. **Two-tier tooling.**
   - Group buyers fund their custom molds, 50/50, with a buy-out clause.
   - The founder funds only universal stock molds over a 2-year life.
   - A price premium cannot recover a mold within 12 months (S11, S12).
4. **Stock holding.**
   - 2–4 weeks of finished goods: 0.2–0.4 M DZD.
   - 4–8 weeks of resin: 0.28–0.57 M DZD.
   - These are the cheapest insurance in S6 and S9.
5. **East Algiers–Boumerdès location**, with copy defences from day 1 (S10).
6. **A mix that includes high contribution per hour.** Drip fittings, conduit couplers, formwork cones and anchors earn about 24–88k DZD/h, against about 5k for spacers. They carry the business through resin shocks (S6), price wars (S15) and easier imports (S7). *Caveat:* their prices are ASSUMPTION, so they are the first thing to verify.
7. **Credit discipline:** traites, at most one month of a customer's purchases outstanding, advance payment from public buyers (S8, S13).

### Fragile choices
- **Leading with rebar spacers.** They are the first to fail under:
  - resin +100% (S6);
  - easier imports, where they land at 2.4–3.6 DZD against a cost of 5.85 (S7);
  - an incumbent price war (S15).

  Three spacer-led molds cannot cover fixed costs (S4). Use spacers as volume filler, not as the core.
- **Flip-top caps as a volume line** (S2). They work only as a colour or short-run service sold through a blower, at 5 DZD or more.
- **An anchor at 50% or more of revenue, or unlimited exclusivity** (S13).
- **Ten or more founder-funded molds in year 1** (S12).
- **A broad catalogue of 30 SKUs at launch** (S14).
- **Expecting a second press within 18 months** (S4).

### Early-warning indicators to monitor monthly

| Indicator | Threshold | Action |
|---|---|---|
| Hours ordered a month (recurring) | Below 60 h at m6, or below 107 h at m12 | Stay on subcontract, or move to 1 shift; delay mold imports |
| Gross contribution against 559k fixed costs | Below 1.0× for 3 consecutive months after m9 | Change the mix toward high-contribution families |
| Resin quote and distributor lot limits | Above 400 DZD/kg, or lots rationed | Trigger indexed clauses; raise the buffer to 8 weeks |
| Wholesaler shelf price of imported spacers or packers | Falls 15% or more | Expect S7 or S15; stop adding spacer molds |
| New PPI/DAPS notes; Note 01/DGC/2026 relaxed | Any change | Re-run S5 or S7 |
| DSO and cheque incidents | DSO above 45 days; any bounce | Apply the exposure cap; move that customer to cash |
| Largest customer's share of revenue | Above 30% | Add accounts before adding molds for that customer |
| A copy seen on a shelf or offered by a mold maker | First sighting | Date-code the parts; offer the customer a contract with traites |
| Press stops and dealer parts lead time | More than 1 stop over 2 days | Raise finished-goods stock to 4 weeks; prepare the subcontractor backup |
| Each of the 19 molds: pieces sold against plan | Below 50% at m6 | Stop founder-funded tooling of the same type |

**What the founder must verify before relying on any of this:**
- drip-fitting and conduit prices;
- wholesaler margin needs;
- who pays for molds;
- credit days and instruments;
- neck sizes.

All are covered by P3 §7 questions 4, 5, 13 and 14 and by the field questions above.
