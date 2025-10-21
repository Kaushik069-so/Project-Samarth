# Data sources & schema

This file records the key data resources used by Project Samarth. Replace the placeholders below with the actual resource IDs and URLs from data.gov.in.

## Crop Production Dataset
- Schema (canonical): state | district | crop | year | production_tonnes
- Notes: production units should be converted to tonnes if necessary (some sources may use quintals).
- Resource placeholder:
  - Name: Ministry of Agriculture - Crop Production (placeholder)
  - Resource ID / URL: <RESOURCE_ID_OR_URL_PLACEHOLDER>

## Rainfall Dataset
- Schema (canonical): state | year | month | rainfall_mm | latitude | longitude (latitude/longitude optional)
- Notes: monthly rainfall entries; to compute annual rainfall, sum months across a year. Some datasets report daily or station-level data; perform spatial aggregation to state-level.
- Resource placeholder:
  - Name: IMD Rainfall (placeholder)
  - Resource ID / URL: <RESOURCE_ID_OR_URL_PLACEHOLDER>

## Provenance & citation conventions
For every numeric claim, include:
- dataset name
- resource ID or URL
- the exact query / filter used (e.g., "state=Maharashtra AND year>=2018 AND year<=2022")
- any normalization or unit conversions performed

Example citation entry:
- IMD Rainfall (https://data.gov.in/resource/xxx) — Aggregated monthly station-level data to state-year totals for 2018–2022.
