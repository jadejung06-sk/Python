import numpy as np
import pandas as pd
import tensorflow as tf


##### preprocessing
data = pd.read_csv(r"D:\2022\Python\Tensorflow\apple_deeplearning\gpascore.csv")
# print('Before :\n', data.isnull().sum())
data = data.dropna()
# data = data.fillna(100)
# print('After :\n', data.isnull().sum())
# print(data[['gre']].max())
# print(data[['gre']].count())
# print(data[['gre', 'gpa', 'rank']])
# exit() # convinient !!


##### shaping of x & y
y = data['admit'].values # <class 'numpy.ndarray'>
# print(y, type(y))
x = []
for i, rows in data.iterrows():
    x.append([rows['gre'], rows['gpa'], rows['rank']])
    # print([rows['gre'], rows['gpa'], rows['rank']]) # [710.0, 3.82, 3.0]
    # print(rows)
    # print(rows['gre'])
    # print(rows['gpa'])
    # print(rows['rank'])
# print(x)
# exit()


##### Make a model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation= 'tanh'), # hidden layer sigmoid, tanh
    tf.keras.layers.Dense(128, activation= 'tanh'),
    tf.keras.layers.Dense(128, activation= 'tanh'),
    tf.keras.layers.Dense(1, activation= 'sigmoid') # output node (float 0.0 ~ 1.0 == sigmoid)
])
model.compile(optimizer='adam', loss= 'binary_crossentropy', metrics = ['accuracy']) # changable w1 adam adagrad sgd, binary_crossentropy (probability)
model.fit(np.array(x), y, epochs = 1000) # model.fit(x= train_x , y = real_y )
# x = [[380, 3.21, 3] [660, 3.67, 3] [] []]
# y = [[0] [1] [] []]

##### Predictation
pred_y = model.predict([[750, 3.70, 3 ],[400, 2.2, 1]]  )
print(pred_y) # [[0.76684576] [0.02732842]] 76%, 2%