import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

##### Data
(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()

trainX = trainX / 255.0
testX = testX / 255.0

trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
testX = testX.reshape((testX.shape[0], 28, 28, 1))

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = 'relu', input_shape = (28, 28, 1)),
    tf.keras.layers.MaxPooling2D( (2, 2)),
    # tf.keras.layers.Conv2D(64, (3, 3), padding = "same", activation = 'relu'),#, input_shape = (28, 28, 1)),
    # tf.keras.layers.MaxPooling2D( (2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation= "relu"),
    tf.keras.layers.Dense(10, activation= 'softmax') # no need to activation, num of categories 10
])


##### save method 2
callback = tf.keras.callbacks.ModelCheckpoint(
    filepath= r'D:\2022\Python\Tensorflow\apple_deeplearning\checkpoint\mnist',
    save_weights_only= True,
    save_freq= 'epoch'
)
model.summary()
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
# model.fit(trainX, trainY, validation_data = (testX, testY), epochs = 3)
model.fit(trainX, trainY, validation_data = (testX, testY), epochs = 3, callbacks = [callback]) # overwrite

# model.fit(trainX, trainY, epochs = 5)
# score = model.evaluate(testX, testY)
# print(score)


##### save model
## method 1 == save all data
# model.save(r'D:\2022\Python\Tensorflow\apple_deeplearning\save\model1') # folder == model1
# load_model = tf.keras.models.load_model(r'D:\2022\Python\Tensorflow\apple_deeplearning\save\model1')
# load_model.summary()
# load_model.evaluate(testX, testY)
# load_model.predict()
# load_model.fit()

## method 2 == save only weights == checkpoint
# callback = tf.keras.callbacks.ModelCheckpoint(
#     filepath= r'D:\2022\Python\Tensorflow\apple_deeplearning\checkpoint\mnist',
#     save_weights_only= True,
#     save_freq= 'epoch'
# )
# model.fit(trainX, trainY, validation_data = (testX, testY), epochs = 3, callbacks = [callback])