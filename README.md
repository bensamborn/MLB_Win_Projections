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
 The data source used to create the projections was Fangraphs. The Data/ folder contains
 5 years of historical batting and pitching data as well as 2021 projected team statistics 
 stored in individual Excel Workbooks. Historical team data can be found at the link below:

 [Historical Team Data](https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season=2020&month=0&season1=2020&ind=0&team=0,ts&rost=&age=&filter=&players=0)

 5 hitting metrics and 8 pitching metrics were selected to regressed against
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

2021 projected team batting and team pitching metrics were taken from the Fangraphs Team Depth Chart aggregate batting and pitching projections. Fangraphs Team Depth Chart projections can be found at the link below:

[Fangraphs Projected Depth Charts](https://www.fangraphs.com/depthcharts.aspx?position=ALL&teamid=1)

## Methodology
The primary methodology used to create team win projections for 2021 was to run a linear regression on team batting and team pitching statistics against runs scored and runs allowed respectively. The regression can then be used to project runs scored and runs against with a teams 2021 projected statistical performance.

Bill James' pythagorean expectation can be applied to projected runs scored and runs against to estimate how many wins and losses each team should have in a 162 game season.

Win % = (Runs Scored)<sup>2</sup> / ((Runs Scored)<sup>2</sup> + (Runs Allowed)<sup>2</sup>)

Testing was also conducted to compare the results of the linear regressions to projections created with a neural net using the Keras API. 

Results were inclusive but the keras_model_testing.py is there to play with for those that are curious. 

## Results
Results are written to the Results/ folder. 

![Win Projections](/Pictures/Wins.PNG)

The results line up closely with 2021 Vegas win totals.

## Model Improvements
- Include more batting and pitching metrics in regression
- Determine ideal historical lookback period
    - 5 years may be too far back given rule and performance changes
    - 5 years also may not provide a sufficient sample size
- Compare 2021 statistical projection against other sources
    - Or create my own team statistical projections
- Improve neural net for comparrison of results 









