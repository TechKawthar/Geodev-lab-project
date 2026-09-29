# Data note
## Grid3 Nigeria Operational LGA Boundaries V4.0
-Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
-Downloaded:08/09/2026
-774 feature
-Columns: globalid, uniq_id, timestamp, editor, lganame, lgacode, statename, statecode, source, amapcod
-No Null
-Cover all states

## Global river flood hazard maps
-Source: https://data.jrc.ec.europa.eu/dataset/jrc-floods-floodmapgl_rp50y-tif
-Downloaded: 28/09/2026
-Extracted files- RP100 and RP10 = Nigeria Boundary
N20_W0: 10°N–20°N, 0°E–10°E
N10_W0: 0°N–10°N, 0°E–10°E
N20_E10: 10°N–20°N, 10°E–20°E
N10_E10: 0°N–10°N, 10°E–20°E
-Coverage looks good

## Grid3 NGA_Health_Facility_V3
-Source: https://data.grid3.org/datasets/827e3638dc204f4b9ddbbd19b00954d6/about
-Downloaded:28/09/2026
-41,000+ feature 
- PHCs extracted, including 39000+ feature

## Worldpop NGA_population_v2
-Source: https://data.worldpop.org/repo/wopr/NGA/population/v2.1/
-Downloaded: 28/09/2026
-Coverage looks good

## NGA_Road and Waterways via OpenStreetMap 
-Source: https://download.geofabrik.de/africa/nigeria-latest-free.gpkg.zip
-Downloaded: 08/09/2026
-13626 features, lines 
-Coverage looks good

## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Lagos Island, extracted from GRID3 lga
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N)
- Area check: Lagos Island 5.05 km2, matches published figure
- Working files in data/processed/study area, raw files untouched
