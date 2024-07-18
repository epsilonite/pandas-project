# California Wildfire Analysis

## Table of Contents
- [Project Description](#project-description)
- [Results](#results)

## Project Description

This project analyzes wildfire data from California covering the period from 2020 to 2023. The analysis includes a detailed examination of fire occurrences, categorized by cause and year. Key insights include a notable decrease in fires in 2020, which was consistent with reduced lightning activity and pandemic-related lockdowns. In contrast, 2021 saw a surge in fires, particularly from unknown causes, while lightning activity dropped significantly in 2022. The project visualizes these trends through various charts and plots, providing a comprehensive overview of the factors influencing wildfire frequency and severity over these years.

#### 2020-2023 Fires Line Plot

The analysis begins with a scatter plot depicting the number of fires from 2020 to 2023. In 2020, the number of fires was notably lower, which was consistent with the reduced lightning activity recorded that year. The COVID-19 pandemic and associated lockdowns likely contributed to fewer fires, but even natural lightning activity was significantly reduced. In contrast, there was a notable increase in fires in 2021, followed by a significant decrease afterward. Lightning activity dropped considerably in 2022, while arson and vehicle fires saw an increase.

![Summary 2020-2023 Fire Data](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig1.png)

#### 2021 Bar Chart

The bar chart illustrates the number of observed fires in 2021 by cause. The highest number of incidents were attributed to unknown causes. Among the known causes, the top five were lightning, equipment use, miscellaneous factors, vehicle-related fires, and debris. Arson ranked just below debris.

![Bar chart of number of observed fires in 2021 by cause](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig2.png)

#### 2021 Line Plots

The first line plot displayed the number of observed fires per month in 2021, categorized by cause. It was evident that fires of unknown origin constituted a significant portion of the data.

![Number of fires in 2021 per month by cause](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig3.png)

When focusing on known causes, a notable spike in debris-related fires occurred in April, with no other month showing a comparable peak for debis fires. As expected, most other causes of fire increased during the summer months, particularly from May to August, with notable peaks in June and July. Equipment use and miscellaneous causes followed lightning in frequency, aligning with the bar chart data.

![Number of fires in 2021 per month by known causes](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig4.png)

By categorizing causes into three groups—man-made, natural, and unknown—the scatter plot revealed that fires of unknown origin often surpassed those caused by man-made or natural factors. Additionally, there were more fires attributed to man-made causes compared to natural ones.

![Number of fires in 2021 per month: man-made, natural, and unknown](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig6.png)

#### 2021 Man-Made vs. Natural Pie Charts

The first pie chart highlights that a significant number of fires in 2021 were caused by man-made factors. Conversely, the second pie chart showed that natural causes, primarily lightning, resulted in a greater number of acres burned.

![Natural vs Man-made Fire Cause Ratio](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig7.png)

![Natural vs Man-Made Acres Burned Ratio](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig8.png)

#### Conclusions

**2020 Fire Reduction**: In 2020, the number of fires was significantly lower, correlating with reduced lightning activity and the impact of COVID-19 lockdowns, which likely reduced human activities and fire incidents.

**Increase in 2021**: There was a significant increase in the number of fires in 2021. Unknown causes were the most frequent, while known causes like lightning, equipment use, and debris were also notable.

**2022 Fires**: Lightning activity, a major cause of fires, dropped significantly in 2022, contributing to a decrease in overall fire incidents.  In contrast, arson and vehicle-related fires increased.  

**Seasonal Patterns**: Debris fires were particularly high in April.  As expected, fires generally spiked during the summer months (May to August), with notable peaks in June and July. 

**Man-Made vs. Natural Causes**: While man-made causes led to a higher number of fires, natural causes, lightning in particular, resulted in more acres burned.

**Unknown Causes Predominance**: Fires of unknown origin consistently surpassed those attributed to man-made or natural causes in both frequency and impact.

#### Future Research

In future research, I plan to investigate the patterns associated with unknown fires more thoroughly. Specifically, I aim to explore whether there is a relationship between the time of day and the occurrence of these fires compared to those with known causes. Additionally, I will examine whether these fires tend to occur in specific locations, such as forests or near highways. 

## Results

#### 2020-2023 Fires Line Plot

![Summary 2020-2023 Fire Data](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig1.png)

#### 2021 Bar Chart

![Bar chart of number of observed fires in 2021 by cuase](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig2.png)

#### 2021 Line plots

![Number of fires in 2021 per month by cause](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig3.png) 

![Number of fires in 2021 per month by known causes](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig4.png)

![Number of fires in 2021 per month: man-made, natural, and unknown](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig6.png)

#### 2021 Man-made vs Natural Pie charts

![Natural vs Man-made Fire Cause Ratio](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig7.png)

![Natural vs Man-Made Acres Burned Ratio](https://github.com/epsilonite/pandas-project/blob/main/California%20Wildfire%20Seasonality/Jenny/output/Fig8.png)
