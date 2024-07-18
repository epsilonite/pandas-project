### pandas-project
---
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
[Data Processing](#data-processing)<br>
[Data Visualization](#data-visualization)<br>
[Results](#results)<br>
[Acknowledgements](#acknowledgements--citations)

---
## Methodology and Process:

This project analyzes wildfire data from California covering the period from 2020 to 2023. The analysis includes a detailed examination of fire occurrences, categorized by cause and year. Key insights include a notable decrease in fires in 2020, which was consistent with reduced lightning activity and pandemic-related lockdowns. In contrast, 2021 saw a surge in fires, particularly from unknown causes, while lightning activity dropped significantly in 2022. The project visualizes these trends through various charts and plots, providing a comprehensive overview of the factors influencing wildfire frequency and severity over these years.

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
Data was collected from 4 different sources: CalFire, NOAA NCEI, NASA FIRMS, NASA GESDISC.



### Datasets
Calfire: https://data.ca.gov/dataset/california-fire-perimeters-1950

NRT VIIRS 375 m Active Fire product VNP14IMGT distributed from NASA FIRMS. Available on-line https://earthdata.nasa.gov/firms. doi:10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002
https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html, https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes

Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2023), GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07, Greenbelt, MD, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: [20240711], 10.5067/GPM/IMERG/3B-MONTH/07 https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGM_07/summary

Daymet: Daily Surface Weather Data on a 1-km Grid for North America, Version 4 R1 https://doi.org/10.3334/ORNLDAAC/2129
https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2131, https://daymet.ornl.gov/single-pixel/api#/default/get_api_data, https://daymet.ornl.gov/single-pixel/

## Data Processing

## Data Analysis

## Data Visualization

## Results
Ignition source has a great influence on the duration of the fire and the acreage spread of fire. After researching and analyzing 8 years of fire activities in California. We found that lightning has the most impact overall with its duration lasting the longest before being contained and its acreage spread being one of the greatest compared to the other sources (as displayed on the boxplot). We also analyzed man-made cause vs. natural causes and the result was still the same with natural (lightning) having the higher average duration, and acreage spread, though their highs and low points were relatively equal (display box plot man vs nat duration and acreage). Although it seems that the natural source of fire has a bigger impact than man-made fires, we have no control over them. Our data showed that man-made fire incidents makes up 67.99% of fire incidents in California throughout the year and is responsible for 27.33% of the fire acreage spread amounting to around 239,151 acres a year. 

## Acknowledgements + Citations
US State Boundaries as geojson polygon from https://public.opendatasoft.com/explore/dataset/us-state-boundaries/export/




