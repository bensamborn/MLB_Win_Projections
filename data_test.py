#Imports
import pandas as pd 
import numpy as np
from read_bat import read_batting_data
from read_pitch import read_pitching_data

#data test
#load data
hist_batting = read_batting_data()[0]
hist_rs = read_batting_data()[1]
proj_batting = read_batting_data()[2]
out_batting = read_batting_data()[3]

hist_pitching = read_pitching_data()[0]
hist_ra = read_pitching_data()[1]
proj_pitching = read_pitching_data()[2]
out_pitching = read_pitching_data()[3]

#output to excel
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Results\Data_Test.xlsx')

hist_batting.to_excel(writer, sheet_name='In')
hist_rs.to_excel(writer, sheet_name='Out')

writer.save()