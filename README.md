# MLB_Win_Projections
 This project was developed to create 2021 MLB Win Projections using python.
 
 ## Packages Needed
 ```
 pip install pandas
 pip install numpy
 pip install math
 pip install matplotlib
 pip install sklearn
 pip install keras
 ```

 ## Data
 Fangraphs was the data source used to create the projections. The Data/ folder contains
 5 years of historical batting and pitching data as well as 2022 projected team statistics 
 stored in individual Excel Workbooks. Historical team data can be found at the link below:

 [Historical Team Data](https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season=2020&month=0&season1=2020&ind=0&team=0,ts&rost=&age=&filter=&players=0)

 5 hitting metrics and 8 pitching metrics were selected to modeled against
 runs scored and runs allowed.

 ### Batting
 - Batting Average (AVG)
 - On Base Percentage (OBG)
 - Slugging Percentage (SLUG)
 - Weight On Base Average (wOBA)
 - Wins Above Replacement (WAR)

 ### Pitching
 - Strikeouts/Nine Innings Pitch (K/9)
 - Walks Allowed/Nine Innings Pitch (BB/9)
 - Home Runs Allowed/Nine Innings Pitch (HR/9)
 - Batting Average Allowed on Balls in Play (BABIP)
 - Percent of Runners Left on Base (LOB%)
 - Earned Run Average (ERA)
 - Fielding Independent Pitching (FIP)
 - Wins Above Replacement (WAR)

2022 projected team batting and team pitching metrics were taken from the Fangraphs Team Depth Chart aggregate batting and pitching projections. Fangraphs Team Depth Chart projections can be found at the link below:

[Fangraphs Projected Depth Charts](https://www.fangraphs.com/depthcharts.aspx?position=ALL&teamid=1)

## Methodology
The methodology used to create team win projections for 2022 was to model runs scored and runs allowed using historical team statistics to project win/loss records with pythagorean expectation.

Bill James' pythagorean expectation can be applied to projected runs scored and runs against to estimate how many wins and losses each team should have in a 162 game season.

Win % = (Runs Scored)<sup>2</sup> / ((Runs Scored)<sup>2</sup> + (Runs Allowed)<sup>2</sup>)

Testing conducted to compare the results of the linear regressions to projections created with a neural net using the Keras API. 

The results between the two models varied slightly, however, the general trend of predicting runs scored and runs allowed linearly to projected WAR was maintaned in both cases. The keras_model_testing.py module contains the neural network used to predict runs scored. 

## Results
Results are written to the Results/ folder. 

![Win Projections](/Pictures/Neural_Net_Projections_2022.PNG)

The results from the neural net line up closely with 2022 Vegas win totals.

## Model Improvements
- Include more batting and pitching metrics in regression
- Determine ideal historical lookback period
    - 5 years may be too far back given rule and performance changes
    - 5 years also may not provide a sufficient sample size
- Compare 2022 statistical player projections from Frangraphs against other sources
    - Or create my own team statistical projections
- Test other model parameters in neural net for comparrison of results 
