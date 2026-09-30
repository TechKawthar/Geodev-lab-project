# My project brief 

## The Question
Where in Nigeria are populations most exposed to a combination of flood risk and poor geographic access to primary healthcare facilities, and how does this exposure map onto population density?

## Why It Matters
Flooding in Nigeria is no longer a distant risk but an active, worsening crisis — the 2024 flood season alone affected 34 states, triggering bridge collapses, school closures, and restricted access to hospitals and markets, which is the exact disruption pattern this study sets out to model. This matters more in Nigeria than almost anywhere else because the health system is already under severe strain: the country carries the world's largest malaria burden, contributing nearly 26% of global cases and over 30% of global malaria deaths, meaning climate shocks compound an already-stretched system rather than disrupting a healthy baseline. The same pattern — floods and extreme weather overwhelming water, sanitation, and health infrastructure — recurs across sub-Saharan Africa, which means a well-built vulnerability model for Nigeria isn't just a national case study but a template other countries in the region could adapt. And practically, disaster response in Nigeria today is largely reactive, responding after a flood hits; a pre-built, geospatially grounded vulnerability model — especially one that can later incorporate near-real-time satellite flood detection — offers a path toward anticipating which primary healthcare catchments are likely to lose access before the flood peaks, not after.

## The data I need
1. Primary Health Care Locations: Point vector dataset containing health facility locations, operational statuses, and facility levels across Nigeria.

2. Population Distribution: 100-meter resolution gridded population count raster.

3. Routable Transport Network: Detailed road network vector data with functional road classes and speed attributes.

4. Flood occurrence: Historical Water Extent & Surface Water: 30-meter resolution water recurrence and maximum surface water extent rasters.

6. Administrative Boundaries: Subnational vector boundaries (State, LGA, and Ward levels).

## Where each Datasetn comes from

1. Primary Health Care Locations: GRID3 Data Hub — https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-

2. Population Distribution: WorldPop Data Hub — https://hub.worldpop.org/geodata/summary?id=28031

3. Routable Transport Network: Geofabrik OpenStreetMap Extracts — https://download.geofabrik.de/africa/nigeria.html

4.  Water Extent: JRC Global Surface Water — https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater

6. Administrative Boundaries: HDX / OCHA Nigeria Administrative Boundaries — https://data.humdata.org/dataset/cod-ab-nga

## What You Would Build
An automated, web-based GeoAI dashboard and API service that dynamically re-routes network access models during severe weather events. The system takes satellite-derived rainfall and flood updates, dynamically intersects them with the road network, and flags communities facing severe travel-time delays to primary care. Local health officers can query specific local government areas (LGAs) to view automated vulnerability scores and receive automated alerts when critical access corridors are breached.
