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
# > Flatten 2D, 3D > 1D, there is a limit of the data that does not look like a image.
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

##### solution of the limit of Flatten() == convolutional layer
## copies 20 images with a kind of feature == feature extraction == important color
## convolutional layer == feature map
# kernel > 1 0 -1
# > Conv2D(16, (3,3)) # 16 copies
# > Conv2D(32, (3,3)) # 32 copies

'''

## sharpen kernel (clearer)
-1 -1 -1
-1  5 -1
-1 -1 -1
## gaussian blur kernel (blur)
1 2 1
2 4 2
1 2 1 
x1/16 (mean)
## height kernel
1 0 -1
1 0 -1
1 0 -1
'''

##### 0-255 > 0-1
'''
trainX = trainX / 255.0
testX = testX / 255.0
'''

##### solution of the limit of convolutional layer == pOOLING LAYER
# Conv2D remembers the position of feature == translation invariance
# > Pooling layer moves the important features to the center
# > Max pooling (more usable), Average pooling
# padding keeps the size of images
# relu does not have negative numbers so it ueses images.
##### Input 0 of layer "conv2d" is incompatible with the layer: expected min_ndim=4, found ndim=3. Full shape received: (32, 28, 28)
    # Call arguments received by layer 'sequential' (type Sequential):
    #   • inputs=tf.Tensor(shape=(32, 28, 28), dtype=uint8)
    #   • training=True
    #   • mask=None
# tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = 'relu')
## conv2D needs data in 4-dimensional space == gray (60000, 28, 28, 1) or color (60000, 28, 28, 3)
## conv1D, conv2D, conv3D
# > trainX = trainX.reshape((60000, 28, 28, 1))
'''
trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
testX = testX.reshape((testX.shape[0], 28, 28, 1))
tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = 'relu' input_shape = (28, 28, 1)),
'''

##### layers
# > Conv > Pooling > Flatten > Dense
##### evaulate
# Epoch 5/5 (overfitting of training dataset)
# 1875/1875 [==============================] - 12s 6ms/step - loss: 0.1578 - accuracy: 0.9415
# 313/313 [==============================] - 1s 2ms/step - loss: 0.2557 - accuracy: 0.9112
# [0.2557179629802704, 0.9111999869346619]
## block from overfitting
# > stop epochs when test or val accracy decreses.
## more correct
# model.fit(trainX, trainY, epochs = 5)
# score = model.evaluate(testX, testY)
# print(score)
'''
model.fit(trainX, trainY, validation_data = (testX, testY), epochs = 5)
# Epoch 5/5
# 1875/1875 [==============================] - 12s 6ms/step - loss: 0.1534 - accuracy: 0.9430 - val_loss: 0.2584 - val_accuracy: 0.9149
'''
######################### Dataset
##### kaggle
## os.environ['KAGGLE_CONFIG_DIR'] = '/content/
# !kaggle competitions download -c dogs-vs-cats-redux-kernels-edition
# !unzip -q train.zip -d .

##### images to numbers
## 1. opencv
## 2. tf.keras

##### image preprocessing 
### classify dogs and cats
## make dir
'''
os.makedirs(r"D:\2022\Python\Tensorflow\apple_deeplearning\kaggle_image_dogscats\dataset\cat")
os.makedirs(r"D:\2022\Python\Tensorflow\apple_deeplearning\kaggle_image_dogscats\dataset\dog")
'''
## move files
'''
for i in os.listdir("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/"):
    if 'cat' in i:
        shutil.copyfile("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/" + i , "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/dataset/cat/" + i)
    if 'dog' in i:
        shutil.copyfile("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/" + i , "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/dataset/dog/" + i)
'''
## tf.keras.preprocessing.image_dataset_from_directory
# no validation
'''
# train_ds = tf.keras.preprocessing.image_dataset_from_directory(
#     "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
#     image_size = (64, 64),
#     batch_size= 64,
#     seed = 1234)
'''
'''
# train_ds = tf.keras.preprocessing.image_dataset_from_directory(
#     "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
#     image_size = (64, 64),
#     batch_size= 64,
#     subset = 'training'
#     validation_split = 0.2)

# val_ds = tf.keras.preprocessing.image_dataset_from_directory(
#     "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
#     image_size = (64, 64),
#     batch_size= 64,
#     subset = 'validation',
#     validation_split = 0.2
#     )
'''
#####     raise ValueError(
# ValueError: If using `validation_split` and shuffling the data, you must provide a `seed` argument, to make sure that there is no overlap between the training and validation subset.
'''
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
    image_size = (64, 64),
    batch_size= 64,
    subset = 'training'
    validation_split = 0.2,
    seed = 1234)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
    image_size = (64, 64),
    batch_size= 64,
    subset = 'validation',
    validation_split = 0.2,
    seed = 1234
    )
'''