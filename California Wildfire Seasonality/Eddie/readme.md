# California Wildfire Seasonality
## Author: Eduardo Almonte, July 15, 2024
---
### Project Overview & Research Question

Relationship between rainfall timing and volume vs fires and damage / acreage spread, and see if there are direct human contributions by looking at wildfire causes)

Is there a correlation between the length of fire season and rainy season?  Is there a correlation between density of rainfall and density of fire season?

### Data Pulling

To analyze fire data efficiently, our team leveraged the CalFire API to pull comprehensive fire incident information directly from the source. This approach ensured we had the most accurate and up-to-date data available. Using Jupyter Notebooks, we processed this data with the pandas library, which is well-suited for handling and analyzing large datasets.

### Analyzing and Cleaning the Data

Our first step involved filtering the raw dataset to include only the essential columns: “Alarm Date” (indicating when the fire started), “Containment Date” (indicating when the fire was contained), the total acres burned, and the cause of the fire. By focusing on these key columns, we created a streamlined DataFrame that provided critical insights into each fire incident.

### Filtering and Exporting

Next, we grouped this filtered data by month to analyze trends and patterns over time. This aggregation allowed us to calculate the total number of fire incidents and the cumulative acres burned for each month. By exporting this summarized data to a CSV file, we ensured it was easily accessible for further analysis and reporting.

### Creating a Bar Chart

For the 2013 monthly summary, we continued this data processing workflow in another Jupyter Notebook. Using pandas, we finalized the data for the entire year, creating a comprehensive monthly summary. This summary DataFrame included the total number of fire incidents and the total acres burned for each month, providing a clear overview of fire activity throughout 2013. This detailed monthly summary helped us identify seasonal trends and assess the impact of fire incidents over the year.

![monthlysummary2013.png](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Eddie/outputs/monthly_summary_2013.png)

