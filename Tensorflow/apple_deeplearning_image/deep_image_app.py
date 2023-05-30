import matplotlib.pyplot as plt
import tensorflow as tf

##### Data
(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()
# ((trainX, trainY), (testX, testY))
#    Input, Right answer

# print(trainX[0])
# print(trainX.shape) # how many images (60000, 28, 28) 28 data x 28 rows x 60000 sets(images)
# print(trainY) # Right Answer [9 0 0 ... 3 0 5] Category

##### show images
# plt.imshow(trainX[0])
# plt.gray()
# plt.colorbar()
# plt.show()

##### modeling - Prediction of Probability, category - softmax

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape = (28, 28),  activation = "relu"),
    tf.keras.layers.Dense(64, activation= "relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation= 'softmax') # no need to activation, num of categories 10
])
model.summary()
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
# model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
model.fit(trainX, trainY, epochs = 10)