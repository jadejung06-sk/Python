import time
import tensorflow as tf
import numpy as np

(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()
trainX = trainX / 255.0
testX = testX / 255.0
trainX = trainX.reshape( (trainX.shape[0], 28,28,1) )
testX = testX.reshape( (testX.shape[0], 28,28,1) )

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax'),
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
model.fit(trainX, trainY, validation_data=(testX, testY), epochs=3)
'''
##### condtion 1
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3), padding = 'same', activation = 'relu', input_shape = (28,28,1) ),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
    ])
tensorboard = tf.keras.callbacks.TensorBoard(log_dir = f'logs/first{str(int(time.time()))}' ) # accuracy loss
model.fit(trainX, trainY, validation_data=(testX, testY), epochs = 3 ,callbacks= [tensorboard])

##### condition 2
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3), padding = 'same', activation = 'relu', input_shape = (28,28,1) ),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(32,(3,3), padding = 'same', activation = 'relu', input_shape = (28,28,1) ),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
    ])
tensorboard = tf.keras.callbacks.TensorBoard(log_dir = f'logs/conv_2times{str(int(time.time()))}' ) # accuracy loss
model.fit(trainX, trainY, validation_data=(testX, testY), epochs = 3 ,callbacks= [tensorboard])

'''
##### for
def make_model():
    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3), padding = 'same', activation = 'relu', input_shape = (28,28,1) ),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(32,(3,3), padding = 'same', activation = 'relu', input_shape = (28,28,1) ),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
    ])
    return model
##### Tensorboard 1 - coLab
'''
%load_ext tensorboard
%tensorboard --logdir logs
'''
##### Tensorboard 2 - local
## tenminal
'''
tensorboard --logdir logs
'''
##### EarlyStopping
'''
es = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', patience = 3) # stop no changes on the next 3 epochs
es = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', patience = 5, mode = 'min') # stop no changes on the next 3 epochs when it comes to min
es = tf.keras.callbacks.EarlyStopping(monitor = 'val_accuracy', patience = 5, mode = 'max') # stop no changes on the next 3 epochs when it comes to max
model.fit(trainX, trainY, validation_data=(testX, testY), epochs = 3 ,callbacks= [tensorboard, es])
'''