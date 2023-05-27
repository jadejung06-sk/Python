##### learning : only digit not image and text
## rgb 0 ~ 255
## gray scale == a single 0 ~ 255
## a single pixel has only one color 
'''
plt.imshow(trainX[0])
plt.gray()
plt.colorbar()
plt.show()
'''

##### no show matplotlib
## > reinstall > tcl/tk and IDLE > NEXT

##### Probability of category
## Sequential of model : num of nodes == num of categories & softmax
## categorical_crossentropy == one hot encoding
## sparse_categorical_crossentropy == int 0 1 2 3 ...
'''
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation = "relu"),
    tf.keras.layers.Dense(64, activation= "relu"),
    tf.keras.layers.Dense(10, activation= 'softmax') # no need to activation, num of categories 10
])


model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
model.fit(trainX, trainY, epochs = 10)
'''

#####  in summary
#    raise ValueError(
# ValueError: This model has not yet been built. Build the model first by calling `build()` or by calling the model on a batch of data.
## input_shape == trainX 60000, 28, 28 
'''
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape = (28, 28),  activation = "relu"),
    tf.keras.layers.Dense(64, activation= "relu"),
    tf.keras.layers.Dense(10, activation= 'softmax') # no need to activation, num of categories 10
])
model.summary()
'''
##### understand the summary 
## (None, 28, 128) == very much, 28 rows, 128 data
## (None, 28, 10) > (10) 
# > Flatten 2D, 3D > 1D
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 28, 128)           3712
#  dense_1 (Dense)             (None, 28, 64)            8256
#  dense_2 (Dense)             (None, 28, 10)            650
# =================================================================
# Total params: 12,618
# Trainable params: 12,618
# Non-trainable params: 0
# _________________________________________________________________
'''
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape = (28, 28),  activation = "relu"),
    tf.keras.layers.Dense(64, activation= "relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation= 'softmax') # no need to activation, num of categories 10
])
model.summary()
'''
## > 3712 == num of w and b
# Model: "sequential"
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 28, 128)           3712

#  dense_1 (Dense)             (None, 28, 64)            8256

#  flatten (Flatten)           (None, 1792)              0

#  dense_2 (Dense)             (None, 10)                17930

# =================================================================
# Total params: 29,898
# Trainable params: 29,898
# Non-trainable params: 0
# _________________________________________________________________


##### ValueError: Shapes (32, 1) and (32, 10) are incompatible
## model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
## one hot encoding == tf.keras.utils.to_categorical()
'''
model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
'''