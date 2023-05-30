import matplotlib.pyplot as plt
import os
import tensorflow as tf
import shutil

# print(len(os.listdir(r"D:\2022\Python\Tensorflow\apple_deeplearning\kaggle_image_dogscats\train"))) # 25000

##### image preprocessing 
### classify dogs and cats
## make dir
# os.makedirs(r"D:\2022\Python\Tensorflow\apple_deeplearning\kaggle_image_dogscats\dataset\cat")
# os.makedirs(r"D:\2022\Python\Tensorflow\apple_deeplearning\kaggle_image_dogscats\dataset\dog")
## move files
# for i in os.listdir("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/"):
#     if 'cat' in i:
#         shutil.copyfile("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/" + i , "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/cat/" + i)
#     if 'dog' in i:
#         shutil.copyfile("D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/train/" + i , "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/dog/" + i)
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
    image_size = (64, 64),
    batch_size= 64,
    subset = 'training',
    validation_split = 0.2,
    seed = 1234
    )

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
    image_size = (64, 64),
    batch_size= 64,
    subset = 'validation',
    validation_split = 0.2,
    seed = 1234
    )
##### preprocessing
def standarization(images, labels):
    images = tf.cast(images / 255.0, tf.float32)
    return images, labels
train_ds = train_ds.map(standarization)
val_ds = val_ds.map(standarization)


##### check batch data
## ((xxxxx), (yyyyy)) : y one hot encoding
# print(train_ds) # 64 batch > 1 image
# for images, labels in train_ds.take(1):
#     print(images) # 64
#     print(labels) # 64
#     plt.imshow(images[0].numpy().astype('uint8')) # Tensor to numpy
#     plt.show()


##### modeling w/o augmentation
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = 'relu', input_shape = (64, 64, 3)), # color
#     tf.keras.layers.MaxPooling2D( (2, 2)),
#     tf.keras.layers.Conv2D(64, (3, 3), padding = "same", activation = 'relu'), # color    
#     tf.keras.layers.MaxPooling2D( (2, 2)),
#     tf.keras.layers.Dropout(0.2), # overfitting == drop some of all nodes
#     tf.keras.layers.Conv2D(128, (3, 3), padding = "same", activation = 'relu'), 
#     tf.keras.layers.MaxPooling2D( (2, 2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation= "relu"),
#     tf.keras.layers.Dropout(0.2), # overfitting == drop some of all nodes
#     tf.keras.layers.Dense(1, activation= 'sigmoid') # binary - sigmoid
# ])
# model.summary()
# model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
# model.fit(train_ds, validation_data = val_ds, epochs = 5)

##### modeling w/ augmentation every epoch
model = tf.keras.Sequential([

    tf.keras.layers.experimental.preprocessing.RandomFlip('horizontal', input_shape = (64, 64, 3)), # input_shape
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.1),
    tf.keras.layers.experimental.preprocessing.RandomZoom(0.1),
    
    tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = 'relu'), # input_shape
    tf.keras.layers.MaxPooling2D( (2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), padding = "same", activation = 'relu'), # color    
    tf.keras.layers.MaxPooling2D( (2, 2)),
    tf.keras.layers.Dropout(0.2), # overfitting == drop some of all nodes
    tf.keras.layers.Conv2D(128, (3, 3), padding = "same", activation = 'relu'), 
    tf.keras.layers.MaxPooling2D( (2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation= "relu"),
    tf.keras.layers.Dropout(0.2), # overfitting == drop some of all nodes
    tf.keras.layers.Dense(1, activation= 'sigmoid') # binary - sigmoid
])
model.summary()
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics= ['accuracy'] )
model.fit(train_ds, validation_data = val_ds, epochs = 5)