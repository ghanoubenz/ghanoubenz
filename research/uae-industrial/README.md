# UAE Engineering + Industrial + AI-Enabled Opportunity Discovery

October 2026. This is a separate project from the earlier "boring businesses" research.

## Bottom line

**The best opportunity found is "Line Continuity".** It is a small Sharjah/Dubai engineering-services company for the UAE's roughly 33,000 mostly-SME industrial plants, starting with food & beverage, bottling, packaging and plastics. It solves the one fear every maintenance manager shares: *"the line stops and we can't get it running fast enough."*

| Role | Offer | Why |
|---|---|---|
| **Wedge** (gets you into the plant) | **I3 Compressed-air leak-to-savings programme.** Acoustic survey, we fix the leaks, re-survey every quarter, AED-verified savings | Kit is available locally (Hikmicro AI56, AED 20.5k). Payback is weeks. No independent UAE provider was found. OEM audits give the survey away to sell compressors, so revenue must come from repairs and the programme |
| **Margin + moat** | **I1 Critical-wear parts.** Paid line triage → scan → CAD → print, machine or cast in 48–72 h → curated per-plant digital vault. Food-zone parts use FDA/EU 10/2011 igus iglidur A350/I151 | 12–19 week OEM lead times. The 2026 Hormuz disruption pushed UAE shipping costs up 300–500%. ADNOC and RTA have proved the model. Immensa serves oil & gas but nobody serves SMEs. Capex has collapsed to about AED 15–90k |
| **Margin + moat** | **I4 Legacy automation continuity.** Obsolescence audit, drop-in HMI/PLC migration kits, repair-exchange, bilingual part-number SEO + WhatsApp quoting | Strong practitioner pain: PLCs replaced because spares are unavailable, HMI repair quoted at $250–5.5k. UAE repair labs are opaque. Founder's document-AI, SEO and marketing skills are a real advantage. Start asset-light: broker repairs, contract engineer |
| **Recurring add-on** | **I2 Reliability routes + approved wireless sensors** | Weak on its own (Vibrant and RMT/Sensoteq are incumbents), but sold on the same visit to the same buyer |

**Capability ladder:** survey kit → scanner and printer → vacuum casting and soft tooling → low-volume moulding (ICV, tier-2 to ADNOC Local+ manufacturers) → regional GCC service hub. This is how "injection moulding" eventually becomes justified. **Do not start with a moulding factory.**

**Alternative path:** **J1 cold-room reliability bundle** for hotels, central kitchens and food chains. It has the best standalone economics (breaks even at 52% of the base case) and the fastest revenue. But it is service-operations heavy, likely to be copied within 6–12 months, and serves a different buyer.

**Biggest uncertainty:** the cross-sell from I3 into I1 and I4. If at least 30% of plants buy parts or automation work, this is a company. If fewer than 25% do, it is a low-moat leak-fixing business. The **6-week field validation (Phase 6)** is designed to measure exactly this for about **AED 25–35k**.

## Read in this order
| File | What it contains |
|---|---|
| `00-tool-setup.md` | Phase 0: Agent Reach and MiroFish install, diagnostics, what is blocked and why |
| `01-phase1-pain-map.md` | Phase 1: UAE technical pain map, 20 preliminary opportunities, what was killed |
| `appendix-opportunity-universe.md` | All 182 hypotheses, clustered, with kill reasons |
| `02-phase2-global-analogues.md` | Phase 2: what other countries figured out; improved ideas; capability ladders |
| `03-phase3-uae-competition-demand.md` | Phase 3: UAE competitors and demand; 29-criterion scoring; 10 → 5 |
| `04-phase4-technical-feasibility.md` | Phase 4: equipment, people, capex, unit economics, the 17-field profiles for the top 5 |
| `05-phase5-simulation.md` | Phase 5: **SIMULATED OUTCOME** persona simulation (MiroFish could not run) |
| `06-phase6-field-validation.md` | Phase 6: who to call, where to go, questions, samples, pilots, kill/go criteria |
| `evidence/E1–E7` | Source evidence with URLs and confidence labels |
| `scoring/` | Re-runnable scoring and unit-economics models |
| `mirofish/` | Seed document, simulation requirements and an API runner for the real MiroFish run |

## Honest limitations (please read)
1. **Agent Reach could not reach its sources.** The container's network policy blocked Reddit, Jina, Exa, YouTube, Google, LinkedIn, X and the UAE news and government sites. Research ran on about 400 web searches that return **result summaries only**. No page was opened in full.
2. **Reddit was not read at all.** Practitioner voice comes from summaries of specialist forums: plctalk, Practical Machinist, eng-tips, hvac-talk, diysolarforum and expat forums. **Direct voice from UAE factory floors is the biggest evidence gap.**
3. **No UAE prices in AED** surfaced for most of these services. This is consistent with the "hidden prices, relationship-driven" market, but it is unverified. Phase 6 phone calls must fill it in.
4. **MiroFish was installed and verified but not run** (no LLM or Zep keys; endpoints blocked). Phase 5 is a labelled substitute.
5. Scores and unit economics are structured judgement. Score differences under about 0.4 are noise.

**To rerun with full Agent Reach and MiroFish capability:** widen the environment's network access, provide a Reddit cookie from a secondary account (needed for Agent Reach's Reddit channel), and add LLM and Zep Cloud keys for MiroFish. See `00-tool-setup.md`.
