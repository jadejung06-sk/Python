# 1. vector to sequence (이미지 자동 캡션)
# 2. sequence to vector (글의 감정분석하기, 악플검사하기)
# 3. sequence to sequence (번역)


# Simple Recurrent Neural Network (재발하는)
# : Input – activation – output
# : low accuracy due to diminishing gradient (첫 글자의 중요도가 희석)

# Long Short Term Memory
# H1 & CELL STATE

### LSTM or GRU
## 1 LSTM
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(100, input_shape = (25, 31)),
    tf.keras.layers.Dense(31, activation = 'softmax') # softmax == (sparse_)catogorical_crossentropy
    ])
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam') # one hot encoding == not sparse
'''

## > 2 LSTM return_sequeces = True
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(100, input_shape = (25, 31), return_sequences= True), # node, a single sample
    tf.keras.layers.LSTM(100), 
    tf.keras.layers.Dense(31, activation = 'softmax') # softmax == (sparse_)catogorical_crossentropy
    ])
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam') # one hot encoding == not sparse
'''