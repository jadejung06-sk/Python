import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import tensorflow as tf


file_lists = os.listdir('D:/2022/Python/Tensorflow/apple_deeplearning_image/GAN/dataset/img_align_celeba/img_align_celeba')
# print(file_lists)

##### data (numpy for preprocessing 178 218 to 64 64) in memory
### memory 16 GB == 50,000~100,000 variables
images = []
for file in file_lists[:50000]:
    numbered_image = Image.open('D:/2022/Python/Tensorflow/apple_deeplearning_image/GAN/dataset/img_align_celeba/img_align_celeba/' + file).crop((20, 30, 160, 180)).convert('L').resize((64,64))
    images.append(np.array(numbered_image)) 
plt.imshow(images[1])
plt.show()
images = np.array(images)
# print(images.shape) # (50000, 64, 64)
#########################

##### images (3 dim to 4 dim) == (50000, 64, 64 to 1)
images = np.divide(images, 255)
images = images.reshape(50000, 64, 64, 1)
# print(images.shape) # (50000, 64, 64, 1)

##### Discriminator images to 1 or 0
discriminator = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), strides = (2,2), padding = 'same', input_shape = (64,64,1)),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Conv2D(64, (3,3), strides = (2, 2), padding = 'same'),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

##### Generator 
noise_shape = 100

generator = tf.keras.models.Sequential([
    tf.keras.layers.Dense(4 * 4 * 256, input_shape = (100,)),
    tf.keras.layers.Reshape((4,4,256)),
    tf.keras.layers.ConV2DTranspose(256, 3, strides = 2, padding = 'same'),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.ConV2DTranspose(256, 3, strides = 2, padding = 'same'),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization()
    tf.keras.layers.ConV2DTranspose(256, 3, strides = 2, padding = 'same'),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.ConV2DTranspose(1, 3, strides = 2, padding = 'same', activation = 'sigmoid')
])

