### pandas-project
# California Wildfire Analysis
### Team: Be Han, Eduardo Almonte, Jennifer Jaurequi, Long Le
Wildfires in California and the greater Pacific Northwest, has immense financial, environmental, and health impacts at both the individual and societal level. As a team, we are interested in growing our awareness and understanding of wildfires by exploring the factors that may contribute to the phenomena in order to contribute to mitigation strategies. Our initial inquiry will be to analyze wildfires by ignition source to identify what mitigation strategies are possible, then to search for correlations between fire season and precipitation to explore the potential on how precipitatio and other weather data can inform future research into creating predictive models for wildfires.

### Project Query
**How does wildfire ignition source relate to observable metrics of wildfires?**<br>
*Metrics and Comparisons to explore: Durations, Areas, Totals, etc*<br>
**Are there correlations between fire season and precipitation?**<br>
*Metrics and Comparisons to explore: Intensity, Duration, Volumes/Areas, etc*<br>

---
# Contents
[Data Source and Resources](#data-source-and-resources)<br>
[Methodolology and Process](#methodology-and-process)<br>

---
# Data Source and Resources [⇧](#pandas-project)
## Datasets
**CALFIRE:**<br>
https://data.ca.gov/dataset/california-fire-perimeters-1950<br>
https://gis.data.cnra.ca.gov/datasets/CALFIRE-Forestry::california-fire-perimeters-1950/explore?location=37.569332%2C-122.356309%2C12.00&showTable=true

**NOAA NCEI: Global Historical Climatology Network - Daily (GHCN-Daily), Version 32. FIPS:06 PRCP (2012)**<br>
NOAA National Climatic Data Center. doi:10.7289/V5D21VHZ [2024-07]<br>
Menne, Matthew J., Imke Durre, Bryant Korzeniewski, Shelley McNeill, Kristy Thomas, Xungang Yin, Steven Anthony, Ron Ray, Russell S. Vose, Byron E.Gleason, and Tamara G. Houston<br>
https://www.ncdc.noaa.gov/cdo-web/webservices/v2#data<br>
https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf<br>
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

**NASA FIRMS: NRT VIIRS 375m Active Fire product VNP14IMGT**<br>
NASA FIRMS. doi:10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002 [2024-7]<br>
Available on-line https://earthdata.nasa.gov/firms<br>
https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html<br>
https://www.earthdata.nasa.gov/s3fs-public/2024-07/VIIRS_C2_AF-375m_User_Guide_1.0.pdf<br>
https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes

**NASA GESDISC: GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07 (2023)**<br>
Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), doi:10.5067/GPM/IMERG/3B-MONTH/07 [2024-07]<br>
Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan<br>
https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGM_07/summary

## Resources
US State Boundaries as geojson polygon<br>
https://public.opendatasoft.com/explore/dataset/us-state-boundaries/export/

---
# Methodology and Process [⇧](#pandas-project)
## API Requests
CalFire:
TBD




