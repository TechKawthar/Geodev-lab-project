# My project brief 

## The Question
Where are populations in Nigeria most vulnerable to loss of access to essential healthcare during climate-related hazards?

## Why It Matters
Public health planners at the Federal Ministry of Health and national disaster response agencies (such as NEMA) require clear, real-time spatial intelligence to deploy emergency medical services during severe weather events. Without route-level access modeling, disaster response teams struggle to identify communities isolated by seasonal flooding, leaving at-risk populations stranded without emergency medical care. By isolating flood-prone, low-accessibility communities before disaster strikes, planning agencies can pre-position mobile medical units and prioritize resilient infrastructure investments.

## The data I need
1. Primary Health Care Locations: Point vector dataset containing health facility locations, operational statuses, and facility levels across Nigeria.

2. Population Distribution: 100-meter resolution gridded population count raster.

3. Routable Transport Network: Detailed road network vector data with functional road classes and speed attributes.

4. Flood occurrence: Historical Water Extent & Surface Water: 30-meter resolution water recurrence and maximum surface water extent rasters.

5. Topography & Elevation: 30-meter digital elevation model (DEM) for terrain and slope derivation.

6. Administrative Boundaries: Subnational vector boundaries (State, LGA, and Ward levels).

## Where each Datasetn comes from

1. Primary Health Care Locations: GRID3 Data Hub — https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-

2. Population Distribution: WorldPop Data Hub — https://hub.worldpop.org/geodata/summary?id=28031

3. Routable Transport Network: Geofabrik OpenStreetMap Extracts — https://download.geofabrik.de/africa/nigeria.html

4.  Water Extent: Google Earth Engine / JRC Global Surface Water — https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater

5. Topography & Elevation: OpenTopography Copernicus GLO-30 DEM — https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.3

6. Administrative Boundaries: HDX / OCHA Nigeria Administrative Boundaries — https://data.humdata.org/dataset/cod-ab-nga

## What You Would Build
An automated, web-based GeoAI dashboard and API service that dynamically re-routes network access models during severe weather events. The system takes satellite-derived rainfall and flood updates, dynamically intersects them with the road network, and flags communities facing severe travel-time delays to primary care. Local health officers can query specific local government areas (LGAs) to view automated vulnerability scores and receive automated alerts when critical access corridors are breached.