#Read and clean historical pitching data

#Imports
import pandas as pd 
import numpy as np

def read_pitching_data():
    #import historicals
    #pure pitching data
    d_2016 = pd.read_excel('Data\\2016_PITCH.xlsx')
    d_2017 = pd.read_excel('Data\\2017_PITCH.xlsx')
    d_2018 = pd.read_excel('Data\\2018_PITCH.xlsx')
    d_2019 = pd.read_excel('Data\\2019_PITCH.xlsx')
    d_2020 = pd.read_excel('Data\\2020_PITCH.xlsx')
    #runs
    r_2016 = pd.read_excel('Data\\2016_RUNS_AGAINST.xlsx')
    r_2017 = pd.read_excel('Data\\2017_RUNS_AGAINST.xlsx')
    r_2018 = pd.read_excel('Data\\2018_RUNS_AGAINST.xlsx')
    r_2019 = pd.read_excel('Data\\2019_RUNS_AGAINST.xlsx')
    r_2020 = pd.read_excel('Data\\2020_RUNS_AGAINST.xlsx')
    r_2016 = r_2016[['Team','R']].copy()
    r_2017 = r_2017[['Team','R']].copy()
    r_2018 = r_2018[['Team','R']].copy()
    r_2019 = r_2019[['Team','R']].copy()
    r_2020 = r_2020[['Team','R']].copy()
    #merge
    d_2016 = pd.merge(d_2016,r_2016,on=['Team'])
    d_2017 = pd.merge(d_2017,r_2017,on=['Team'])
    d_2018 = pd.merge(d_2018,r_2018,on=['Team'])
    d_2019 = pd.merge(d_2019,r_2019,on=['Team'])
    d_2020 = pd.merge(d_2020,r_2020,on=['Team'])

    # #import projections
    p_2021 = pd.read_excel('Data\\2021_PITCH.xlsx')
    z = p_2021.drop(columns=['IP','Team'])

    #clean data
    master = pd.concat([d_2016,d_2017,d_2018,d_2019,d_2020])
    master.reset_index(drop=True,inplace=True)
    y = master['R']
    X = master.drop(columns=['Team','W','L','SV','G','GS','IP','GB%','HR/FB','EV','xFIP','R'])

    return X,y,z,p_2021