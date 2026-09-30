# Month 1 Summary
![GEODEV_study_area](map.png)
## Question
Where in Ibadan Metropolis are populations most exposed to both flood risk and poor geographic access to primary healthcare facilities, and how does this exposure map onto population density?

## Operation
Reprojected all datasets to EPSG:32631 (UTM Zone 31N), generated 1 km catchment buffers around primary healthcare facilities (PHCs) without dissolving to preserve facility-level granularity, and executed Zonal Statistics on WorldPop population rasters to estimate population denominators served per facility alongside 10-year (RP10) and 100-year (RP100) flood hazard raster overlays.

## Expected
A clear spatial mismatch: high-density central wards have abundant healthcare coverage but significant riverine flood exposure, while peripheral wards have low physical access to healthcare.

## Got
Extracted population service denominators for all primary healthcare facilities, identifying dense urban clusters with overlapping 1 km service zones; however, unclassified raster symbology and initial projected CRS mismatches (EPSG:4326 vs. EPSG:32631) temporarily hid real flood hazard extents along major drainage corridors.

## What Surprised Me
Initial raw join keys between spatial boundaries and attribute tables silently failed on character formatting differences (e.g., spaces vs. hyphens), and default raster symbology rendered dry land as solid fill rather than transparent NoData, completely obscuring underlying population heatmaps and river channels.

## What Data I Still Need
- High-resolution road network data to transition from Euclidean straight-line distance buffers to realistic network-based travel time catchments (e.g., 15-minute walking/driving isolines).
- Updated facility-level operational status and bed capacity datasets to distinguish fully functioning primary health centers from under-resourced clinics.
- Fine-scale localized elevation (DEM) or urban drainage vector layers to improve flood inundation accuracy across informal settlement areas.
-Flood hazard data
