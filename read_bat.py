#Read and clean historical batting data

#Imports
import pandas as pd 
import numpy as np

def read_batting_data():
    #import historicals
    d_2016 = pd.read_excel('Data\\2016_BAT.xlsx')
    d_2017 = pd.read_excel('Data\\2017_BAT.xlsx')
    d_2018 = pd.read_excel('Data\\2018_BAT.xlsx')
    d_2019 = pd.read_excel('Data\\2019_BAT.xlsx')
    d_2020 = pd.read_excel('Data\\2020_BAT.xlsx')

    #import projections
    p_2021 = pd.read_excel('Data\\2021_BAT.xlsx')
    z = p_2021.drop(columns=['PA','Team'])

    #clean data
    master = pd.concat([d_2016,d_2017,d_2018,d_2019,d_2020])
    master.reset_index(drop=True,inplace=True)
    y = master['R']
    X = master.drop(columns=['PA','R','Team'])

    return X,y,z,p_2021
