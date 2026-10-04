# Seed document: UAE SME plant maintenance market, 2026 (facts only)

This document is the seed for a MiroFish simulation. It contains ONLY sourced facts from the study's evidence files (E1–E7). The simulated agents may reason about these facts but must not treat any simulated behaviour as fact.

## Market context
- The UAE has about 33,000 industrial enterprises; 95% are SMEs. There are 2,000+ food & beverage manufacturers and 569 rubber/plastics converters.
- **2026 Strait of Hormuz disruption:**
  - Ship transits fell by more than 90%.
  - UAE shipping costs rose 300–500%.
  - Normalisation is not expected before 2027.
  - Ducab: "Cable could not come easily inside the UAE", so projects switched to local suppliers.
- **Government localisation push:**
  - MIITE 2026 announced AED 180bn of offtakes to localise more than 5,000 products, plus a AED 1bn Industrial Resilience Fund.
  - ADNOC launched "Local+" and "Build-to-Demand".
- **Payment behaviour:** UAE B2B payment terms average 47 days; 58% of credit sales are paid late.
- **Electricity:** the DEWA industrial tariff is 23 fils/kWh up to 10,000 kWh/month and 38 fils above that, plus a fuel surcharge of about 6 fils.

## Pain (practitioner and news evidence)
- OEM machine parts lead times of 12–19 weeks; tool-changer parts took about 9 months. 83% of UK manufacturers report maintenance delays caused by unavailable parts.
- PLCs are replaced because spares can't be found, not because they fail. HMI repair quotes range from $250 to $5,500, or 50–60% of the price of a new unit.
- Compressed-air leaks waste 20–30% of output, and payback on fixing them is typically under 1 year. Practitioners say leak programmes stall because savings are hard to prove and leaks come back.
- A +5 °C chiller can reach +15 °C in under 2 hours at 45 °C ambient. Door gaskets need replacing every 3–12 months.
- Abu Dhabi's food authority (ADAFSA) closed 21 food establishments in 2024; missing fridge and freezer temperature records were among the violations.
- An F&B plant case: a £45 3D-printed part replaced a packaging-arm part whose failures had caused £5,000/day of downtime.

## Incumbents
- **Compressed air:** OEM audits from ELGi UAE and Atlas Copco AIRScan. No independent provider was found that surveys, repairs and re-surveys.
- **3D printing and reverse engineering:** Orbit3D, LayerX, Paradigm3D and Iris 3D, plus Hubs offering instant online quotes. Immensa and Falcon Technologies serve ADNOC.
- **Electronics repair:** WEDIAN (Ajman), Automat, CNC Experts, Indian repair houses, and grey-market traders.
- **Condition monitoring:** Vibrant Electromechanical; Pruftechnik; RMT Reliability (Sensoteq sensors, since August 2024).
- **Cold rooms:** Kelsius and Testo sell sensors and software; classified-ad technicians do repairs. Nobody bundles the two.

## Technology costs (2026)
- Hikmicro AI56 acoustic camera: AED 20,475 in the UAE.
- Handheld 3D scanner: about €1.1–1.4k.
- Engineering-filament printer: $450–2,700.
- igus iglidur A350 / I151 filament: FDA and EU 10/2011 food-compliant; A350 is rated to 180 °C.
- Wireless vibration sensors: $340–500. Temperature sensors: $20–50.
- In the UAE, wireless sensors require TDRA type approval.

## The entrant (subject of the simulation)
"Line Continuity" is a small Sharjah/Dubai company. Its founder has a marketing and AI-automation background and works with one technician and one CAD designer.

| Offer | Pricing |
|---|---|
| Compressed-air leak programme | First survey AED 3.5k (credited); programme about AED 12k/yr including repair labour; monitoring AED 250/month |
| Critical-wear parts (scan → CAD → print/machine) | Triage audit AED 3–5k; reverse engineering AED 1–3.5k per part; digital vault AED 500–1,500/month |
| Legacy automation continuity | Audit AED 3–7.5k; HMI/PLC migration kits AED 15–50k |
| Reliability routes | AED 2–4k per month |
