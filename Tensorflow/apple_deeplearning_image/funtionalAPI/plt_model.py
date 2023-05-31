import tensorflow as tf 
import pydot
import graphviz
import numpy as np

(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()

trainX = trainX / 255.0
testX = testX / 255.0

trainX = trainX.reshape( (trainX.shape[0], 28,28,1) )
testX = testX.reshape( (testX.shape[0], 28,28,1) )

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28) ),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax'),
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
# model.fit(trainX, trainY, validation_data=(testX, testY), epochs=3)

tf.keras.utils.plot_model(model, to_file='D:/2022/Python/Tensorflow/apple_deeplearning_image/funtionalAPI/model.png', show_shapes=True, show_layer_names=True)