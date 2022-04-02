#Imports
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt
from read_bat import read_batting_data
from read_pitch import read_pitching_data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

#load data
hist_batting = read_batting_data()[0]
hist_rs = read_batting_data()[1]
proj_batting = read_batting_data()[2]
out_batting = read_batting_data()[3]

hist_pitching = read_pitching_data()[0]
hist_ra = read_pitching_data()[1]
proj_pitching = read_pitching_data()[2]
out_pitching = read_pitching_data()[3]

# normalize data and split into train and test sets
hist_ra = np.reshape(hist_ra.to_list(), (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(hist_pitching))
xscaler = scaler_x.transform(hist_pitching)
print(scaler_y.fit(hist_ra))
yscaler = scaler_y.transform(hist_ra)

train_pit_in, test_pit_in, train_pit_out, test_pit_out = train_test_split(xscaler, yscaler, test_size=0.2)

#define model
model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])
history = model.fit(train_pit_in, train_pit_out, epochs=150, batch_size=50,  verbose=1, validation_split=0.2)
score = model.evaluate(test_pit_in, test_pit_out, verbose=100)

print('Test loss:', round(score[0], 3))
print('Test accuracy:', round(score[1], 3))

#Predict
Xnew= scaler_x.transform(proj_pitching)
ynew= model.predict(Xnew)
#invert normalize
ynew = scaler_y.inverse_transform(ynew) 
Xnew = scaler_x.inverse_transform(Xnew)
out_pitching['Proj Runs'] = pd.Series(ynew[:,0])
out_pitching.to_excel('Results/Keras_Pitching_2022.xlsx')