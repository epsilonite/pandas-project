# pandas-project
# California Wildfire Seasonality
## Members:

**Be Han:** Github Master, Data Administrator

**Eduardo Almonte:** Data Analyst / Data Visualization

**Jennifer Jaurequi:** Data Analyst

**Long Le:** Data Analyst /Data Visualization

## Overview: 
Relationship between rainfall timing and volume vs fires and damage / acreage spread, and see if there are direct human contributions, ie. type of ignition source and proximity to infrastructure (powerlines, highways, political regions, fire fighting infrastructure)
### Initial Questions: 
Is there a correlation between the length of fire season and rainy season?  Is there a correlation between density of rainfall and density of fire season?
- Duration of overall fire season
- Average duration per county
- Pull fire data by acreage: Find sum area damaged by wildfire and compare to difference in rainfall compared to historic average for at least 3 yrs (as far as data allows)
- Look at rainfall (beginning, end and monthly density ) and compare to fire season (beginning, end and monthly density) for at least 3 yrs (as far as data allows)
Does ignition source influence the beginning and end of fire season?
- Cause (natural, manmade, etc)
- Average duration per cause/incident
- Average acreage spread per cause 
- Look at human infrastructure layers
### Datasets
Calfire: https://data.ca.gov/dataset/california-fire-perimeters-1950

NRT VIIRS 375 m Active Fire product VNP14IMGT distributed from NASA FIRMS. Available on-line https://earthdata.nasa.gov/firms. doi:10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002
https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html, https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes

Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2023), GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07, Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: [20240711], 10.5067/GPM/IMERG/3B-MONTH/07 https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGM_07/summary

Daymet: Daily Surface Weather Data on a 1-km Grid for North America, Version 4 R1 https://doi.org/10.3334/ORNLDAAC/2129
https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2131, https://daymet.ornl.gov/single-pixel/api#/default/get_api_data, https://daymet.ornl.gov/single-pixel/

## Acknowledgements + Citations
US State Boundaries as geojson polygon from https://public.opendatasoft.com/explore/dataset/us-state-boundaries/export/
