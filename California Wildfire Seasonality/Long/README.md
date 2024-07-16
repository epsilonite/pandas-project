# California Wildfire Seasonality
## Author: Long Le 
---
### Project Overview & Research Question

Does ignition source influence the beginning and end of fire season?
- Man-made causes vs. natural causes
- Average Duration per cause
- Average acreage spread per cause

### Data Pulling

Our team used CalFire API to pull data from the most recent years and some as far back as 2013 to use for our research. We created datasets in Jupyter Notebook to display the fire data. 

### Cleaning and Analyzing

After getting the data from the CalFire API some cleaning were needed to be done to the data. This data contained Alarm dates and Containment dates of the fires and some were formatted incorrectly. We used pandas library and dataframe manipulation to change the formatting to fit our need before continuing to analyzing the data. 

The key components to look for our analysis were the Alarm Dates, Containment Dates, GIS Acres, and the Cause columns of the dataframe. Using the Containment Dates and Alarm Dates we were able to create a separate column called Duration that listed the difference between the two dates to show how long it took to contain each fire. We then created a seperate dataframe to show the average duration, average GIS acres spread, and number of incidents for each cause. These dataframes were created for each year that we analyzed. Then they were exported their own csv files, to be pulled at any time for further analysis. A seperate notebook were then created with all the years merged together into one dataframe to show the overall data for all the years. We also created a dataframe grouping all the man-made causes together and all the natural causes together.

### Barcharts and Boxplots

We created barcharts to display the Average Duration for each cause to compare on average how long a fire last for each cause. Similarly barcharts were created for GIS Acres Spread and number of incidents per cause.
![Duration_bar_all.png](https://github.com/epsilonite/pandas-project/blob/long_branch/California%20Wildfire%20Seasonality/Long/outputs/Duration_bar_all.png)
![manVSnat_incidents_all.png](https://github.com/epsilonite/pandas-project/blob/long_branch/California%20Wildfire%20Seasonality/Long/outputs/manVSnat_incidents_all.png)

We created boxplots to show the range of the acres spread and duration for each cause as well. Although we had the averages the boxplot showed a better representation of the the data as a whole taking in consideration of the outliers in the data. 
![Duration_boxplot_all.png](https://github.com/epsilonite/pandas-project/blob/long_branch/California%20Wildfire%20Seasonality/Long/outputs/Duration_boxplot_all.png)

![acres_boxplot_all.png](https://github.com/epsilonite/pandas-project/blob/long_branch/California%20Wildfire%20Seasonality/Long/outputs/acres_boxplot_all.png)


