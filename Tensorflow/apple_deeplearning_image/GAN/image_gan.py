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

##### Generator 100 random numbers to 1 image
### Conv2D + upsampling (bigger size of images)
noise_shape = 100

generator = tf.keras.models.Sequential([
    tf.keras.layers.Dense(4 * 4 * 256, input_shape = (100,)),
    tf.keras.layers.Reshape((4,4,256)), # size of images
    tf.keras.layers.Conv2DTranspose(256, 3, strides = 2, padding = 'same'), # upsampling two times and Conv
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization(), # covariate shift
    tf.keras.layers.Conv2DTranspose(128, 3, strides = 2, padding = 'same'), # output size = (input size -1) * strides - 2*padding + (kernel size -1) + 1
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2DTranspose(64, 3, strides = 2, padding = 'same'),
    tf.keras.layers.LeakyReLU(alpha = 0.2),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2DTranspose(1, 3, strides = 2, padding = 'same', activation = 'sigmoid') # 64 64 1 gray scale
    # Conv2DTranspose(3, 3, strides=2, padding='same', activation='sigmoid') # color scale
])

generator.summary()

##### GAN models and compile
GAN = tf.keras.models.Sequential([generator, discriminator])
discriminator.compile(optimizer= 'adam', loss = 'binary_crossentropy') # once

discriminator.trainable = False # discriminator only classified not trained
# for layer in discriminator.layers: 
#   layer.trainable = False
GAN.compile(optimizer='adam', loss = 'binary_crossentropy')


##### predictation
def predict_pic():
    random_num = np.random.uniform(-1, 1, size = (10, 100)) # 8 sets 100 data
    pred = generator.predict(random_num)
    # print(pred.shape, pred) # (8, 64, 64, 1)
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(pred[i].reshape(64, 64), cmap = 'gray') #  color 64 64 3
        plt.axis('off')
    plt.tight_layout()
    plt.show() # save() for local computer 
###################################

###### 300 epochs
for _ in range(300):
    print(f"[Epoch : {_} / 300]")
    predict_pic()
    ##### all images training (1 epoch)
    for i in range(50000//128):
        if i % 100 == 0:
            print(f"[Batch : {i}]")
        ##### Training of discriminator
        X_data = images
        real_images = X_data[i*128:(i+1)*128]
        all_one = np.ones(shape = (128,1))
        loss1 = discriminator.train_on_batch(real_images, all_one) # real images 1
        #######################################################
        random_num128 = np.random.uniform(-1, 1, size = (128, 100))
        fake_images = generator.predict(random_num128)
        all_zero = np.zeros(shape = (128,1))
        loss2 = discriminator.train_on_batch(fake_images, all_zero) # fake images 0
        ###### training of generator
        loss3 = GAN.train_on_batch(random_num128, all_one)
    print(f"[Discriminator loss : {loss1+loss2}] [GAN loss : {loss3}]")
    
    
# [Epoch : 15 / 300] Discriminator loss : 1.2226955890655518] [GAN loss : 1.1557810306549072]