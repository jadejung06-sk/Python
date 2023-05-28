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
    validation_split = 0.2
    )

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "D:/2022/Python/Tensorflow/apple_deeplearning/kaggle_image_dogscats/dataset/",
    image_size = (64, 64),
    batch_size= 64,
    subset = 'validation',
    validation_split = 0.2
    )


## ((xxxxx), (yyyyy)) : y one hot encoding