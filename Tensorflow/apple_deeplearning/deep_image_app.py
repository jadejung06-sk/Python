import matplotlib.pyplot as plt
import tensorflow as tf


(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()
# ((trainX, trainY), (testX, testY))
#    Input, Right answer

# print(trainX[0])
# print(trainX.shape) # how many images (60000, 28, 28) 28 data x 28 rows x 60000 sets(images)
# print(trainY) # Right Answer [9 0 0 ... 3 0 5] Category

##### show images
plt.imshow(trainX[0])
plt.gray()
plt.colorbar()
plt.show()