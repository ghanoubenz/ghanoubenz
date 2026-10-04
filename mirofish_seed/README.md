# MiroFish seed package — Algeria one-press plastic-component entry (Phase 6)

Prepared 2026-10-04 from the repository's research notes only (no new web research). The founder can run this in MiroFish (github.com/666ghj/MiroFish) on their own machine. The founder's own LLM and Zep keys are needed, and the simulation could not be run in the environment where this package was built.

## What is in this folder

| File | Use | Upload to MiroFish? |
|---|---|---|
| `01_policy_and_regulation.md` | Customs, banking, import programme, AAPI, GPI cut-off, taxes | **Yes** (seed) |
| `02_supply_side_competitors.md` | Molders, mold makers, machine dealers, clusters, copying | **Yes** (seed) |
| `03_resin_and_inputs.md` | Resin, masterbatch, regrind supply and prices | **Yes** (seed) |
| `04_buyers_and_demand.md` | Buyers by sector, visible prices, demand signals | **Yes** (seed) |
| `05_buyer_behavior_and_payment.md` | Buying centres, payment, switching, tooling, trust | **Yes** (seed) |
| `06_economics_and_machines.md` | Cost inputs, machines, molds, cost model | **Yes** (seed) |
| `07_global_analogies.md` | Company origins, country comparison | **Yes** (seed) |
| `personas.md` | 21 persona cards with evidence tags | Optional (see step 3) |
| `scenarios.md` | 15 scenarios: setup, variables, outcomes | **No.** It describes hypothetical events. If uploaded, the knowledge graph would store them as facts |
| `README.md` | This file | **No** |

Every statement in the seeds carries one tag: `[VERIFIED date · source]`, `[STRONG SIGNAL]`, `[WEAK SIGNAL]`, `[UNKNOWN]` or `[ASSUMPTION]`. Assumptions sit in an "Assumptions (not facts)" section at the end of each seed. "VERIFIED" means the figure was seen in a search-engine snippet of the named source. The research proxy blocked Algerian sites, so no official text was read in full.

---

## How to run MiroFish with this package

> **Accuracy note.** Only the four environment-variable names below were supplied as confirmed for this package; they come from MiroFish's `.env.example`. The install commands, ports and workflow steps come from memory of the MiroFish README and were **not re-checked**, because this environment had no network access. Check them against the current README in the repository before running.

### 1. Install and configure

```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
cp .env.example .env
```

Edit `.env` and set:

```bash
LLM_API_KEY=<your LLM provider key>
LLM_BASE_URL=<OpenAI-compatible endpoint of your provider>
LLM_MODEL_NAME=<model name at that provider>
ZEP_API_KEY=<your Zep Cloud key>
```

- MiroFish calls the LLM through an OpenAI-compatible API. Any provider that exposes that format will work.
- Leave any other variables in `.env.example` at their defaults unless the MiroFish README says otherwise.
- **Never commit `.env`** or paste the keys into this repository.

Install and start the app. These commands are as recalled; confirm them in the MiroFish README:

```bash
npm run setup:all     # installs frontend (Node) and backend (Python) dependencies
npm run dev           # starts frontend and backend
# frontend usually at http://localhost:3000, backend API at http://localhost:5001
# alternative: docker compose up -d
```

### 2. Build the knowledge graph (step "Graph Building")

1. Upload the seven seed files `01_…md` to `07_…md` together in a single project.
2. Paste the prediction requirement for the scenario you are running. The texts are below.
3. Let MiroFish extract entities and relations into Zep. Check the extracted entities before you continue. Real firm names (SNK Plastic, AFC Industry, Henkel, and others) will appear as entities. That is expected, because they are evidence anchors.

### 3. Environment and persona generation

- MiroFish generates its own agent personas from the graph.
- To steer it toward the 21 roles in `personas.md`, upload `personas.md` together with the seeds in step 2. In that case, add this sentence to the prediction requirement: "Persona behaviours tagged [ASSUMPTION] are hypotheses, not observed facts."
- Confirm that the generated agent list covers at least the personas named under "Personas driving" for that scenario in `scenarios.md`. If one is missing, regenerate before starting.

### 4. Run the simulation: start small, because cost is high

- **Keep every run under 40 rounds.** MiroFish's own guidance warns that consumption is high. Start with a 10–15 round pilot of Scenario 1 to measure token and Zep cost, then size the other runs.
- Suggested mapping: 1 round ≈ 2 weeks of market time, so 36 rounds ≈ 18 months. If cost is a constraint, use 1 round ≈ 1 month (18 rounds).
- Run **one scenario variant per project**. Write down the variant letters, model name, round count and date for every run.
- Suggested order:
  1. Scenarios 1 and 2, which set the baseline.
  2. Scenarios 3, 6, 8 and 9, the stress tests.
  3. The rest.

### 5. Report and interaction

- Generate the MiroFish report.
- In the deep-interaction step, ask the key agents (shampoo owner, wholesaler, incumbent molder, copycat, bank officer) **why** they acted as they did. Record the answers in item 3 of the reporting template in `scenarios.md`.

### 6. What MiroFish can and cannot answer

- MiroFish simulates how actors interact and react: who adopts, who copies, who switches, how sentiment spreads.
- It is **not** an accounting model. Compute utilisation, margin, cash and DSO outside MiroFish. Take the simulated decisions (volumes, prices, credit terms, timing) and run them through the cost model in `06_economics_and_machines.md` or `model/economics.py`.

---

## Mandatory rule for every output

1. Label every result **SIMULATED OUTCOME**: report headings, tables, quotes from agents, and any chart.
2. Compare each simulated outcome with the seed evidence and mark it *consistent*, *contradicted* or *no evidence*. Name the seed section, for example "S05 §2".
3. Do not cite a simulated outcome as a fact in any later report, deck or decision memo. It may justify a **field question**, not a conclusion.
4. Where an outcome rests mainly on `[ASSUMPTION]` persona behaviour, or on a `[UNKNOWN]` gap, say so in the same sentence.
5. Use the reporting template at the end of `scenarios.md`.

---

## Prediction-requirement texts (paste one per run)

Each text is self-contained. Replace `<variant>` with the variable levels you chose from `scenarios.md`.

### Scenario 1: Quiet one-machine entry
```
Using only the uploaded seed documents, simulate the Algerian market from November 2026 for 18 months after a first-time founder quietly installs one new 120-tonne injection press in the East Algiers–Boumerdès area and sells small B2B plastic parts (rebar spacers, glazing packers, drip-tape fittings, PP flip-top caps) only through direct visits and introductions, with no advertising. Variant: <first product family; direct vs via wholesalers; price vs import landed price; with or without an introduction by a resin distributor or mold maker>. Agents should include buyers from construction, joinery, irrigation and cosmetics, hardware wholesalers, an incumbent custom molder, a machine dealer and potential copycat entrants. Predict: which buyer types adopt first and why; how many active customers and roughly how many machine-hours of monthly orders the founder reaches at months 6, 12 and 18; when competitors or dealers notice the niche; and the first reorders. Treat statements tagged [ASSUMPTION] as hypotheses, not facts. Label every result SIMULATED OUTCOME and state for each whether the seed evidence supports it, contradicts it, or is silent.
```

### Scenario 2: Shampoo / dispensing-cap niche
```
Using only the uploaded seed documents, simulate 18 months from November 2026 in which a new Algerian molder with one 120-tonne press launches stock PP flip-top caps (28/410, later 24/410) from an 8–12 cavity mold, offering colour-matched lots from small minimums, selling to small and mid-size shampoo and detergent fillers directly and through bottle blowers. Variant: <MOQ 5k/10k/20k per colour; direct vs bundled with a blower; price vs trader price; an incumbent local molder already offers flip-tops or not; hinge-failure incident in month 3 or not; standard vs non-standard necks>. Agents should include shampoo factory owners, detergent manufacturers, bottle blowers, import traders of caps and pumps, an incumbent cap molder, a Chinese mold maker and end consumers. Predict: how many brands adopt, monthly volumes, achieved price relative to imported caps, the role of blowers, reactions to any quality problem, and whether any brand offers to fund a custom mold. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 3: Competitor copies after 6 months
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder that has built a customer base for small B2B parts, and a copycat entrant who, at month 6, buys the same press and has a mold made from a sample of the founder's best-selling part. Variant: <copied part is a catalogue item vs a part made to one customer's drawing; copycat price cut 10/20/30%; founder defence: none / match price / hold price with stock and 48-hour delivery / supply contracts with bills of exchange / molds kept in-house with date-coded parts; copy mold made locally in 6 weeks vs imported in 3–4 months>. Agents should include the copycat, local mold makers, hardware wholesalers, joinery distributors, group procurement managers and the founder's existing customers. Predict the founder's share of the copied part at months 9, 12 and 18, price erosion, which customers defect and why, and whether copying spreads to other parts. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 4: 3 → 10 → 20 molds on one press
```
Using only the uploaded seed documents, simulate a new Algerian molder with one 120-tonne press that grows from 3 molds at start to 10 by month 9 and 20 by month 18, under Algerian import rules (bank domiciliation before shipment with a 120% provision, import programme filing). Variant: <full molds vs insert-frame tooling; molds from China (3–4 months landed) vs local (about 6 weeks); high-runner vs long-tail demand per part; make-to-order vs 2–4 weeks of finished stock>. Agents should include buyers across sectors, local and Chinese mold makers, the domiciliating bank officer and a customs broker. Predict how buyers react to range breadth and lead times, stock-outs, the number of changeovers the founder must run, cash tied up in molds and bank provisions, and when a second press is justified. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 5: Finished-part import restrictions tighten
```
Using only the uploaded seed documents, simulate the Algerian market for small plastic parts when, from month 3 after November 2026, the state tightens imports of finished plastic parts while a new one-press local molder is operating. Variant: <mechanism: the 60% safeguard duty extended to more chapter-39 lines / import-programme refusals for finished plastic parts / tighter equity cap for resale importers / crackdown on suitcase (cabas) imports; mild (one mechanism) vs severe (all); founder has one press only vs can subcontract overflow to an existing molder>. Agents should include import traders including cabas traders, hardware wholesalers, joinery distributors, irrigation tube makers, group procurement managers, a customs broker and copycat entrants. Predict the change in enquiries and in the import price ceiling, whether the founder can raise prices, capacity shortfalls, new local entrants, and whether traders become distributors of local parts. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 6: Resin +20% / +50% / +100%
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder of small PP/HDPE parts when, at month 4, resin prices rise sharply. Variant: <increase +20% / +50% / +100%; material available at a price vs rationed with two-week gaps; founder holds 0 / 4 / 8 weeks of stock; fixed DZD prices for 3 months vs resin-indexed contracts; 0% vs 20% regrind in non-cosmetic parts>. Agents should include resin distributors, the founder's customers in construction, joinery, irrigation and cosmetics, an incumbent molder and import traders. Predict which customers accept price increases and which leave, production stoppages, which product families stop being viable, and how competitors and importers respond. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent), including the 2021 and 2026 resin shocks described in the seeds.
```

### Scenario 7: Chinese imports become easier
```
Using only the uploaded seed documents, simulate the Algerian market for small B2B plastic parts when, from month 6 after November 2026, import friction eases while a new one-press local molder is operating. Variant: <prior bank domiciliation and 120% provision relaxed / import programme abolished / customs duty on finished plastic articles cut from 30% to 15% / wider official foreign-exchange access for traders; one change vs all>. Agents should include import traders, hardware wholesalers, group procurement managers, Chinese mold makers and the bank officer. Predict which buyers return to imported parts, when and why; the price cuts the founder would need to hold volume; and whether local stock and fast delivery keep customers. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 8: Customers demand 60/90-day credit
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder whose distributor and group customers, from month 3, demand longer payment terms. Variant: <60 vs 90 days; 30% / 60% / 90% of revenue affected; post-dated cheques vs bank-endorsed bills of exchange vs transfers; cheque bounce rate 0% / 5% / 15%; founder accepts / refuses / accepts only with bills of exchange and a one-month exposure cap per customer>. Agents should include hardware wholesalers, joinery distributors, group procurement managers, a public furniture maker and the founder's bank officer. Predict which customers leave if refused, payment delays and bounced cheques, the founder's working-capital need, and survival risk. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 9: Machine fails for 2 / 7 / 30 days
```
Using only the uploaded seed documents, simulate a new Algerian molder whose only 120-tonne press stops in month 8 during a peak delivery period. Variant: <stoppage 2 / 7 / 30 days; cause: heater or thermocouple (spares on hand) vs controller board (1–3 weeks from China) vs hydraulic pump; press bought through a local dealer with technicians vs imported directly with no local technician; 0 / 2 / 4 weeks of finished stock; molds can or cannot run at an existing subcontract molder>. Agents should include the machine dealer, an incumbent subcontract molder, the founder's affected customers and an industrial maintenance manager. Predict late deliveries, which customers switch back to imports or other molders and whether they return, the cost and feasibility of subcontracting the gap, and the effect on reorders. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 10: Location — Algiers vs Sétif/El Eulma vs Bordj Bou Arréridj vs Oran
```
Using only the uploaded seed documents, simulate the first 18 months of the same one-press Algerian plastic-parts start-up located in four alternative places: East Algiers–Boumerdès, Sétif–El Eulma, Bordj Bou Arréridj, or Oran. Variant: <location>. For each location, use the buyers, mold makers, machine dealers, resin distributors and competitors that the seeds place nearby. Agents should include buyers by sector, local mold makers, the machine dealer, a resin distributor, an incumbent molder and copycat entrants. Predict time to the first five customers, ease of mold and machine support, exposure to copying, resin access, and which product families fit each location. Rent and logistics costs are unknown in the seeds and must be reported as unknown, not invented. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 11: Customer funds the mold
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder who asks every customer to pay for the mold of each new part; the customer owns it on paper but it stays at the molder's shop with maintenance included. Variant: <100% upfront / 50% at order and 50% at sample approval / 30% upfront and the rest amortised over the first pieces; owner-led SMEs vs large groups; free mold removal vs buy-out fee and notice; mold bought in China under bank domiciliation vs locally>. Agents should include shampoo factory owners, detergent manufacturers, group procurement managers, maintenance managers, joinery distributors, Chinese and local mold makers and the bank officer. Predict acceptance by buyer type, the number of new parts launched, disputes, and molds moved to other molders. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent), noting that Algerian mold-funding norms are unknown in the seeds.
```

### Scenario 12: We fund the mold
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder who funds and owns all molds and recovers their cost through the part price. Variant: <3 / 6 / 10 molds in year 1; payback target 6 / 12 / 24 months of volume; price premium 0% / 10% / 20%; financed by equity vs overdraft vs leasing>. Agents should include buyers across sectors, Chinese and local mold makers, copycat entrants and the bank officer. Predict which molds win enough orders to pay back, which do not, how buyers respond to the price premium, copying of molder-owned designs, and the founder's cash strain. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 13: Exclusive customer mold
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder who makes a part to one anchor customer's drawing on a mold the customer funds, with exclusivity. Variant: <exclusivity 12 / 24 months / unlimited; no volume commitment vs a minimum annual quantity backed by bills of exchange; anchor is 30% / 50% / 70% of founder revenue; anchor pays at 60 vs 90 days>. Agents should include a group procurement manager (or a detergent manufacturer) as the anchor, copycat entrants, an incumbent molder and the bank officer. Predict the anchor's ordering and payment behaviour, the founder's exposure if the anchor delays or cuts volume, what happens when exclusivity ends (stay, re-tender or make in-house), and copy attempts. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 14: Standard catalogue product
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder that launches a stocked catalogue of standard parts (rebar spacers in several sizes, glazing packers, drainage caps, drip-tape fittings) with free samples and a printed catalogue, sold through hardware and trade wholesalers. Variant: <10 / 20 / 30 SKUs; 2 / 4 / 8 weeks of stock; 2 vs 6 wholesalers vs direct; 48-hour vs 1-week delivery promise>. Agents should include hardware wholesalers, joinery distributors, irrigation tube makers, import traders and copycat entrants. Predict sell-through by part, stock-outs, wholesaler loyalty, copying of catalogue parts, and whether the catalogue grows or shrinks. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

### Scenario 15: Competitor price war
```
Using only the uploaded seed documents, simulate a new Algerian one-press molder whose two main product families are attacked at month 8 by price cuts. Variant: <attacker is an established custom molder with paid-off machines vs a new copycat with debt; cut 20% / 30% / 40%; lasting 3 / 6 / 12 months; founder response: match / partial match plus service / hold price with supply contracts / exit the family and use the press for other parts>. Agents should include the incumbent molder, the copycat, hardware wholesalers, joinery distributors, irrigation tube makers, a group procurement manager and the bank officer. Predict which customers stay and why, how long each response is sustainable, whether the attacker raises prices again, and the founder's survival. Treat [ASSUMPTION] statements as hypotheses. Label every result SIMULATED OUTCOME and compare each with the seed evidence (supports / contradicts / silent).
```

---

## After each run

1. Export the MiroFish report. Save it with the completed reporting template from `scenarios.md` under a dated run folder, for example `mirofish_runs/2026-10-xx_S01_aB/`. Keep the `.env` file out of the repository.
2. Put the simulated decisions (volumes, prices, terms, timing) into the cost model (`model/economics.py` or `06_economics_and_machines.md`) to get utilisation, margin and cash.
3. Turn each "contradicted" or "no evidence" finding into a question in the P3 §7 buyer interview (`research_notes/Phase 2-8/p3_buyer_behavior.md`).
