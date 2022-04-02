#Imports
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from read_bat import read_batting_data
from read_pitch import read_pitching_data

#load data
hist_batting = read_batting_data()[0]
hist_rs = read_batting_data()[1]
proj_batting = read_batting_data()[2]
out_batting = read_batting_data()[3]

hist_pitching = read_pitching_data()[0]
hist_ra = read_pitching_data()[1]
proj_pitching = read_pitching_data()[2]
out_pitching = read_pitching_data()[3]

#define regressions
reg_bat = LinearRegression().fit(hist_batting, hist_rs)
reg_pitch = LinearRegression().fit(hist_pitching, hist_ra)

#projections
runs_scored = reg_bat.predict(proj_batting)
runs_against = reg_pitch.predict(proj_pitching)

out_batting['RS'] = runs_scored
out_pitching['RA'] = runs_against

#output to excel
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Results\Raw_Linear_Results_2022.xlsx')

out_batting.to_excel(writer, sheet_name='BATTING')
out_pitching.to_excel(writer, sheet_name='PITCHING')

writer.save()

#print r-squared
bat_r2 = str(reg_bat.score(hist_batting, hist_rs))
pitch_r2 = str(reg_pitch.score(hist_pitching, hist_ra))

print('Batting R2: ' + bat_r2)
print('Pitching R2: ' + pitch_r2)