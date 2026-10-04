# Opportunity database schema (Phase 2+)

CSV columns (one row per candidate product; quote any field containing commas):

product_id,product,family,sector,photo_reference,known_buyers,known_suppliers,current_supply_source,local_or_imported,country_of_origin,pain_evidence,pain_type,pain_source_url,pain_confidence,demand_frequency,moq,lead_time,observed_price_dzd,price_source_url,price_confidence,material,part_weight_g,projected_area_cm2,cavities,shot_weight_g,mold_size_mm,clamp_required_t,machine_fit,mold_type,cycle_time_s,mold_cost_usd,unit_cost_dzd,potential_price_dzd,margin_pct,working_capital,regulatory_difficulty,quality_difficulty,copy_risk,switching_difficulty,buyer_concentration,custom_dimensions_needed,many_variants_needed,local_competition,why_choose_us,overall_confidence,sources,date_checked,next_validation_action,stage_notes

Rules
- Confidence labels: VERIFIED / STRONG SIGNAL / WEAK SIGNAL / ASSUMPTION / UNKNOWN. Never invent prices, buyers, suppliers, shortages or contacts: write UNKNOWN.
- pain_type one of: shortage, MOQ, import_delay, custom_dimensions, quality_failure, colour_unavailable, small_volume, long_lead_time, cash_tied_in_imports, downtime_missing_part, no_local_supplier, price, none_found.
- machine_fit one of: Fits 120T confidently / Borderline 120T / Requires larger injection press / Requires blow molding / Requires thermoforming / Requires extrusion / Other process.

Machine-fit calculation (show numbers in the row)
- clamp_required_t = projected_area_cm2 x cavities x 1.15 (runner allowance) x clamp factor. Clamp factor (t/cm2): PP/HDPE/LDPE 0.30 for wall >=1.5 mm, 0.45 for thin wall <1 mm or long flow; PA/POM/PC/ABS 0.45-0.6. Add 20% safety margin.
- shot_weight_g = part_weight_g x cavities + runner (cold runner: +15-30% for small parts).
- Reference presses (Chinese servo, typical): 
  60T: tie-bar ~310x310 mm, practical PP shot 20-90 g, mold height 120-330.
  80-90T: tie-bar ~360x360, practical PP shot 30-135 g.
  100T: tie-bar ~380x380, practical PP shot 35-160 g.
  120T: tie-bar 410x410, practical PP shot 45-200 g, mold height 150-430.
  160T: tie-bar 470x470, practical PP shot 60-280 g.
- Mold must fit between tie-bars (mold width < tie-bar clearance, or mount through with mold width < clearance) and shot must be within ~20-80% of practical barrel capacity.
- Fits 120T confidently: clamp <= 100 t and shot within range and mold <= ~400 mm wide. Borderline 120T: clamp 100-125 t or shot/size near limits. Larger: beyond.
