### pandas-project
# California Wildfire Analysis

**Be Han:** Github+Data Administrator / Data Engineer<br>
**Eduardo Almonte:** Data Analyst / Data Visualization<br>
**Jennifer Jaurequi:** Data Analyst / Data Visualization<br>
**Long Le:** Data Analyst / Data Visualization

---
## Overview: 
Wildfires in California and the greater Pacific Northwest, has immense financial, environmental, and health impacts at both the individual and societal level. As a team, we are interested in growing our awareness and understanding of wildfires by exploring the factors that may contribute to the phenomena in order to contribute to mitigation strategies. Our initial inquiry will be to analyze wildfires by ignition source to identify what mitigation strategies are possible, then to search for correlations between fire season and precipitation to inform future research into creating predictive models for wildfires.

---
## Contents
[Methodolology and Process](#methodology-and-process)<br>
[Data Acquisition](#data-acquisition)<br>
[Acknowledgements](#acknowledgements--citations)

---
## Methodology and Process:

### Initial Questions:
Is there a correlation between the length of fire season and rainy season?  Is there a correlation between density of rainfall and density of fire season?
>Duration of overall fire season<br>Average duration per county<br>
Fire data by acreage: Find sum area damaged by wildfire and compare to difference in rainfall compared to historic average for at least 3 yrs (as far as data allows)<br>
Look at rainfall (beginning, end and monthly density ) and compare to fire season (beginning, end and monthly density) for at least 3 yrs (as far as data allows)

Does ignition source influence the beginning and end of fire season?
>Cause (natural, manmade, etc)<br>
Average duration per cause/incident<br>
Average acreage spread per cause<br>
Look at human infrastructure layers<br>

## Data Acquisition
Data was collected from 4 different sources: CalFire, NOAA NCEI, NASA FIRMS, NASA GESDISC, using `pandas` and `wget`

### Datasets

#### CALFIRE:
https://data.ca.gov/dataset/california-fire-perimeters-1950
https://gis.data.cnra.ca.gov/datasets/CALFIRE-Forestry::california-fire-perimeters-1950/explore?location=37.569332%2C-122.356309%2C12.00&showTable=true

#### NOAA NCEI:
Menne, Matthew J., Imke Durre, Bryant Korzeniewski, Shelley McNeill, Kristy Thomas, Xungang Yin, Steven Anthony, Ron Ray, Russell S. Vose, Byron E.Gleason, and Tamara G. Houston (2012): Global Historical Climatology Network - Daily (GHCN-Daily), Version 32. FIPS:06 PRCP.
NOAA National Climatic Data Center. doi:10.7289/V5D21VHZ [2024-07].<br>
Matthew J. Menne, Imke Durre, Russell S. Vose, Byron E. Gleason, and Tamara G. Houston, 2012: An Overview of the Global Historical Climatology Network-Daily Database. J. Atmos. Oceanic Technol., 29, 897-910. doi:10.1175/JTECH-D-11-00103.1.

https://www.ncdc.noaa.gov/cdo-web/webservices/v2#data
https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

#### NASA FIRMS:
NRT VIIRS 375 m Active Fire product VNP14IMGT distributed from NASA FIRMS. Available on-line https://earthdata.nasa.gov/firms. doi:10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002 

https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html
https://www.earthdata.nasa.gov/s3fs-public/2024-07/VIIRS_C2_AF-375m_User_Guide_1.0.pdf
https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes

#### NASA GESDISC:
Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2023), GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07, Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: [20240711], 10.5067/GPM/IMERG/3B-MONTH/07 https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGM_07/summary




## Acknowledgements + Citations
US State Boundaries as geojson polygon from https://public.opendatasoft.com/explore/dataset/us-state-boundaries/export/




