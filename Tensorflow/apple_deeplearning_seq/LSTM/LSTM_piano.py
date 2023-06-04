import tensorflow as tf
import numpy as np

##### read text file
text = open(r"D:\2022\Python\Tensorflow\apple_deeplearning_seq\LSTM\pianoabc.txt", "r").read()
unique_text = list(set(text))
unique_text.sort()
# print(unique_text)

##### utilities
### encoding (def or dict)
text_to_num = {}
num_to_text = {}
for i, data in enumerate(unique_text):
    text_to_num[data] = i
    num_to_text[i] = data 
# print(text_to_num)
# print(num_to_text[3])
numbered_text = []
for i in text:
    numbered_text.append(text_to_num[i])
    
##### sequence to vector
# ### Trial1 : trainX trainY == 25 data next data
# trainX, trainY = [], []
# for i in range(len(numbered_text) // 25 + 1):
#     trainX.append([])
#     trainY.append([])
# for idx, data in enumerate(numbered_text):
#     if idx % 25 == 0 :
#         trainY[idx // 25].append(data)
#     else:
#         trainX[idx // 25].append(data)
# print(len(trainX), len(trainY)) # 11681 * 25 11681 * 25 
### Trial2 : 
X = []
Y = []
for i in range(0, len(numbered_text) - 25): # 
    X.append(numbered_text[i: i+25])
    Y.append(numbered_text[i+25])
# print(len(X), len(Y)) # 291997 291997
# print(Y[:5]) # [17, 0, 14, 5, 27]
### shape Tensor or np.array()
# print(np.array(X).shape)

##### one hot encoding == unique string 
X = tf.one_hot(X, 31) # num of unique string
Y = tf.one_hot(Y, 31)
print(X[:2]) #  shape=(2, 25, 31)
### too much unique string == embedding layer

# /*  modeling                  */ #
### LSTM or GRU
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(100, input_shape = (25, 31)),
    tf.keras.layers.Dense(31, activation = 'softmax') # softmax == (sparse_)catogorical_crossentropy
    ])

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy']) # one hot encoding == not sparse
model.fit(X, Y, batch_size = 64, epochs = 40, verbose = 2) # update weights more frequently ## 40 ~ 100 verbose 2 (print)
model.save(r"D:\2022\Python\Tensorflow\apple_deeplearning_seq\LSTM\model1")
