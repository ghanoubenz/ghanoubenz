# E1 — Practitioner pain intelligence (Phase 1)

How this was collected: about 53 WebSearch queries. Reddit is blocked in WebSearch ("domain not accessible") and through the container proxy, so practitioner voice comes from search summaries of specialist forums: plctalk.net, practicalmachinist.com, eng-tips.com, hvac-talk.com, diysolarforum.com, solarpaneltalk.com, refrigeration-engineer.com, expatforum.com and expatwoman.com. **No page could be opened.** Every snippet is the search engine's summary.

Labels: **PV** = practitioner voice · **NEWS** · **VENDOR** · **RESEARCH**

## Obsolete industrial electronics
- **P1 — PLCs are replaced because spares run out, not because they fail.** Users say the PLCs themselves rarely fail; capacitors, relays and LEDs wear out. RoHS made premium PLCs obsolete, forcing migrations of systems that still worked. [plctalk](https://www.plctalk.net/forums/threads/are-plcs-being-replaced-more-due-to-failures-or-lack-of-spare-parts.124110/) · PV · high
- **P2 — HMI touchscreens.** PanelView Plus, Red Lion G3 and Siemens TP700/TP170A digitisers fail while the unit still works with a mouse.
  - Costs quoted: $5,500 by a Rockwell distributor; repair houses at 50–60% of new; a 15" PanelView repair at no more than $1,500; a 6" C-More screen at $250.
  - Workarounds: eBay used units, or sourcing the digitiser itself (one RoHS "obsolete" panel turned up for about £50).
  - Sources: [plctalk 1](https://www.plctalk.net/forums/threads/hmi-repair-services.137296/), [plctalk 2](https://www.plctalk.net/forums/threads/replacing-the-touch-screen-on-a-g3-red-lion-hmi.136582/), [plctalk 3](https://www.plctalk.net/forums/threads/siemens-hmi-tp700-comfort-panel-touch-screen-not-working.143369/) · PV · high
- **P3 — Obsolete drives.** Out-of-production components carry high mark-ups. Drives under 5 HP are usually not worth repairing. OEM response times of "a week or two or more". [plctalk](https://www.plctalk.net/forums/threads/drive-repair-refurbishing.104832/), [eng-tips](https://www.eng-tips.com/threads/vfd-reliability.416507/) · PV · high
- **P4 — Heat and dust kill drive cabinets.** Filters plug within days, IGBTs trip on over-temperature, and opening over-cooled panels causes condensation. Electrolytic capacitor life halves for every +10 °C. [plctalk](https://www.plctalk.net/forums/threads/reliable-cabinet-coolers.72592/), [eng-tips](https://www.eng-tips.com/threads/using-fans-to-cool-an-industrial-control-panel.501282/) · PV · medium
- **P5 — UAE component-level repair already exists (competition, not pain).**
  - Automat Electronic Services: over 30,000 sq ft across UAE, KSA, Oman and Bahrain.
  - WEDIAN (Ajman) and Horizon Elect Devices (Sharjah).
  - VENDOR

## Spare parts, lead times, 3D printing
- **P6 — OEM lead times for machine-tool parts.** These ran to months.
  - Cases: a DMG spindle took 16 weeks (19 weeks of downtime in total); a Fanuc 21iT board took 18 weeks plus shipping; tool-changer parts took about 9 months.
  - Parts support typically lasts about 7 years after end of production.
  - Sources: [practicalmachinist 1](https://practicalmachinist.com/forum/threads/long-lead-times-on-cnc-parts.242449/), [practicalmachinist 2](https://www.practicalmachinist.com/forum/threads/parts-availability-for-machinery-is-it-20-years.72657/) · PV · high
- **P7 — UK manufacturer survey (Fluke).** 83% report maintenance delays from unavailable parts, 22% of spares inventory is obsolete, and 68% had unplanned downtime in the last 12 months. [Fluke](https://pressroom.fluke.com/fluke-study-83-of-uk-manufacturers-report-maintenance-delays-due-to-unavailable-parts/) · vendor-commissioned survey · medium
- **P8 — Hormuz 2026.**
  - Disruption: transits fell more than 90%, and normalisation is not expected until 2027. Mechanics in Kuwait cannot find parts. Maintenance of local exhaust ventilation (LEV) was disrupted.
  - UAE response at MIITE 2026:
    - AED 180bn in offtakes to localise 5,000+ products
    - AED 1bn Industrial Resilience Fund
    - EDGE–ICAPE electronics localisation
    - Oliver Wyman: local sourcing is "strongest where downtime is costly"
  - Sources: [Khaleej Times](https://www.khaleejtimes.com/business/hormuz-disruption-strains-supply-chains-as-iran-conflict-forces-costly-rerouting), [Kuwait Times](https://kuwaittimes.com/article/47255/kuwait/other-news/spare-parts-shortage-drives-up-repair-costs-delays-vehicle-servicing-in-kuwait/), [SupplyChainBrain](https://www.supplychainbrain.com/blogs/1-think-tank/post/44322-how-the-strait-of-hormuz-closure-has-impacted-workplace-conditions), [EnterpriseAM](https://enterpriseam.com/uae/2026/05/11/how-miite-2026-became-an-inflection-point-for-the-uaes-industrial-strategy-amid-regional-disruption/), [Oliver Wyman](https://www.oliverwyman.com/media-center/2026/may/frederic-ozier-on-uae-local-procurement-shift.html), [TradeArabia](https://tradearabia.com/News/462273/UAE-plans-%2449bn-industrial-procurement-drive-to-localise-5-000-products) · NEWS · high
- **P9 — 3D-printed parts and heat.** PLA has a Tg of about 55–60 °C and PETG about 80 °C, while sun-exposed interiors exceed 70 °C, so ASA or engineering polymers are needed. Printers need tuning. [practicalmachinist](https://www.practicalmachinist.com/forum/threads/how-many-of-you-are-using-3d-printers-at-your-shop.446631/) · PV · medium. *No industrial in-service failure accounts found.*

## Commercial kitchens
- **P10 — Ice machines lose output in hot kitchens.** Ratings assume 70 °F air and 50 °F water. Fixes: a remote or water-cooled condenser and clean coils. [hvac-talk](https://hvac-talk.com/vbb/threads/102797-3rd-machine-and-it-still-won-t-make-ice-help!!) · PV · medium-high
- **P11 — Heat-wave refrigeration breakdowns outnumber engineers.** Claimed: "up to 500% increase" (CloudFM, a vendor). Gulf News says a +5 °C chiller reaches +15 °C in under 2 hours at 45 °C ambient. [Gulf News](https://gulfnews.com/uae/is-your-fridge-spoiling-your-food-in-uae-summers-experts-reveal-early-warning-signs-and-health-risks-at-45c-1.500588332) · low-medium
- **P12 — Hard water in Dubai.** Claimed TDS of 200–400 mg/L. Sponsored-style article · low. *No UAE operator voice on Rational ovens, technicians or ice machines.*

## HVAC and BMS
- **P13 — Summer AC collapse in UAE buildings.**
  - The Greens: residents spent up to Dh6,000, and AC firms saw a 100% jump in demand within a week.
  - Expat forums: unresponsive landlords, RERA complaints, and district-cooling fee disputes.
  - Sources: [Khaleej Times](https://khaleejtimes.com/uae/uae-ac-issues-in-summer-see-some-residents-spend-up-to-dh6000-on-upgrades), [Gulf News](https://gulfnews.com/uae/acs-break-down-as-temperature-goes-up-1.1865999) · NEWS + resident PV · high
- **P14 — EC/ECM fan failures cluster in summer.** "Anyone know of a place that repairs ECM modules?" points to a repair gap. [hvac-talk 1](https://www.hvac-talk.com/threads/ebm-papst-fan-failures.2241739/), [hvac-talk 2](https://hvac-talk.com/vbb/threads/2234722-Anyone-know-of-a-place-that-repairs-ECM-modules) · PV · medium-high
- **P15 — High ambient and coastal corrosion.** R410A runs at about 2,840 kPa at 50 °C. Seawater-cooled condensers deplete anodes, and coastal coil fins corrode. [refrigeration-engineer](https://www.refrigeration-engineer.com/forum/technical-refrigeration/fundamentals/38446-r410a-in-a-r404a-compressor) · PV · medium
- **P16 — BMS lock-in.** Owners describe being "locked into service for life" when only the original contractor has the software. [hvac-talk](https://hvac-talk.com/vbb/threads/2237784-IT-Group-Managing-BMS-Laptops) · PV · medium. *No UAE evidence.*
- **P17 — FCU condensate overflow damages ceilings.** Vendor blog · low

## Compressed air, VFDs
- **P18 — Leak programmes stall.** The savings are hard to prove and leaks recur. Typical leakage is 20–30% of output with payback under 1 year (Compressed Air Challenge). [eng-tips](https://www.eng-tips.com/threads/air-leak-or-steam-leak-survey.29953/), [CAC](https://www.compressedairchallenge.org/data/sites/1/media/library/factsheets/factsheet07.pdf) · medium
- **P19 — VFD savings are often overclaimed when pumps run near full flow.** SME barriers are capital, information, and having no energy manager. [plctalk](https://www.plctalk.net/forums/threads/energy-savings-with-vfds.80063/) · medium

## Water
- **P20 — Hidden villa leaks produce huge DEWA bills.**
  - The Lakes: over Dh22,000 in 2 months.
  - Arabian Ranches: Dh54,000.
  - Older villas with underground tanks and irrigation are the hardest to diagnose.
  - Sources: [Gulf News](https://gulfnews.com/amp/story/uae%2Flakes-resident-gets-dh22000-bill-after-water-leakage-from-broken-pipe-1.1329443), [The National](https://thenational-the-national-prod.cdn.arcpublishing.com/uae/2022/07/16/dubai-residents-urged-to-check-for-water-leaks-to-avoid-exorbitant-bills) · NEWS · high
- **P21 — Palm Jumeirah pools evaporate over 600 million litres a year.** Covers cut evaporation by about 95%. [RGS](https://www.rgs.org/about-us/our-work/latest-news/research-spotlight-water-loss-uae) · RESEARCH
- **P22 — About 70% of Middle East seawater RO plants suffer biofouling.** RESEARCH, no operator voice

## Solar, EV, cold storage, skills
- **P23 — Soiling.** Panels lose 13% after 3 months uncleaned and 4% when cleaned every 15 days; utility plants clean 40–45 times a year. [UAEU](https://research.uaeu.ac.ae/en/publications/the-influence-of-cleaning-frequency-of-photovoltaic-modules-on-po/) · high (but cleaning is commoditised)
- **P24 — Inverter heat derating.** Output loss of 10–22%, and warranty swaps take months. [solarpaneltalk](https://www.solarpaneltalk.com/forum/solar-panels-for-home/solar-panels-for-your-home/434905-derating-solar-panels-and-inverters-in-hot-weather-6-2kw-is-really-4-9kw), [diysolarforum](https://diysolarforum.com/threads/luxpower-eg4-temperature-de-rating-on-a-stupid-hot-climate.100974/) · PV · high
- **P25 — Mismatched or counterfeit MC4 connectors are the "#1 cause of solar fires".** [diysolarforum](https://diysolarforum.com/threads/melted-mc4-what-happened.42848/) · PV · high
- **P26/P27 — EV charger uptime.**
  - US: about 73% real uptime. [Electrek](https://electrek.co/2022/06/16/study-finds-more-than-fourth-charging-stations-were-non-functional/)
  - Dubai: 1,860 points in January 2026, targeting 10,000 by December 2026.
  - Reports of UAE chargers "under maintenance" come only via an indirect Reddit summary.
- **P28 — Walk-in coolers.** Door infiltration is the most common cause of iced coils. PV · medium
- **P29 — GCC maintenance skills gap.** In Kuwait, 60% of shortages are in mechanical maintenance and instrument technician roles. [Gulf News](https://gulfnews.com/business/analysis/the-widening-skills-gap-in-gulfs-construction-sector-1.2166474) · medium

## Evidence gaps (honest)
- No Reddit content.
- No UAE factory-floor voice on obsolete electronics or repairs sent abroad.
- No UAE commercial kitchen operator voice.
- No UAE commercial and industrial (C&I) solar O&M evidence.
- No UAE EV-charger O&M data.
- No direct UAE quotes that technicians "just replace parts".
- No UAE SME compressed-air evidence.

**These gaps must be closed in field validation (Phase 6).**
