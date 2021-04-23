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
hist_rs = np.reshape(hist_rs.to_list(), (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(hist_batting))
xscaler = scaler_x.transform(hist_batting)
print(scaler_y.fit(hist_rs))
yscaler = scaler_y.transform(hist_rs)

train_hit_in, test_hit_in = train_test_split(xscaler, test_size=0.2)
train_hit_out, test_hit_out = train_test_split(yscaler, test_size=0.2)

#define model
model = Sequential()
model.add(Dense(12, input_dim=5, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(train_hit_in, train_hit_out, epochs=150, batch_size=50,  verbose=1, validation_split=0.2)
score = model.evaluate(test_hit_in, test_hit_out, verbose=100)

print('Test loss:', round(score[0], 3))
print('Test accuracy:', round(score[1], 3))

# # plot "Loss"
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('Model Loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Validation'], loc='upper left')
# plt.show()

#Predict
#Xnew = np.array([[40, 0, 26, 9000, 8000]])
Xnew= scaler_x.transform(proj_batting)
ynew= model.predict(Xnew)
#invert normalize
ynew = scaler_y.inverse_transform(ynew) 
Xnew = scaler_x.inverse_transform(Xnew)
#print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
out_batting['Proj Runs'] = pd.Series(ynew[:,0])
out_batting.to_excel('Results/Keras_Batting.xlsx')

# #output to excel
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('Results\Raw_Linear_Results.xlsx')

# out_batting.to_excel(writer, sheet_name='BATTING')
# out_pitching.to_excel(writer, sheet_name='PITCHING')

# writer.save()