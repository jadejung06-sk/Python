import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import urllib.request
##### get data
# urllib.request.urlretrieve("https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt", "D:/2022/Python/Tensorflow/apple_deeplearning_seq/cleanbot/shopping.txt")

#### read file
raw = pd.read_table("D:/2022/Python/Tensorflow/apple_deeplearning_seq/cleanbot/shopping.txt", names = ['rating', 'review'])
# print(raw)
##### labeling : good 1 bad 0
raw['label'] = np.where(raw['rating'] > 3, 1, 0) # condition True False
# print(raw)

########### string to number
# Try all below
### word to number
### letter to number

##### preprocessing
raw['review'] = raw['review'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9 ]', '') # [^ == not]
# print(raw.isnull().sum()) # all 0 
raw.drop_duplicates(subset = ['review'], inplace = True)
# print(raw)

##### bag of words (Korean)
unique_text = raw['review'].tolist()
unique_text = ''.join(unique_text)
unique_text = list(set(unique_text)) # 3210
unique_text.sort() 
# print(unique_text[:100])
##### tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level = True, oov_token= '<OOV>' )
string_list = raw['review'].tolist()
tokenizer.fit_on_texts(string_list)
# print(tokenizer.word_index) # dict
# print(string_list[:10])
### string to number
train_seq = tokenizer.texts_to_sequences(string_list)
# print(train_seq[:10])
Y = raw['label'].tolist()
# print(Y[:10])
### the length
raw['length'] = raw['review'].str.len()
# print(raw.head())
# print(raw.describe()) # label 50 50 good! # length max 140 
# print(raw['length'][raw['length'] < 100].count()) # total 199425 / 190496
X = tf.keras.preprocessing.sequence.pad_sequences(train_seq, maxlen = 100)
X = X.tolist()

##### train / test / val (list to numpy)
trainX, valX, trainY, valY = train_test_split(X, Y, test_size = 0.2, random_state= 42)
# print(len(trainX)) # 159540
# print(np.array(trainX).shape) # (159540, 100)
##### modeling of input (the same length and shape)
### no one hot encoding
# print(trainX[:5])

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(len(tokenizer.word_index) + 1, 16), # 3210 vector 0~1 16 ea.
    tf.keras.layers.LSTM(100),
    tf.keras.layers.Dense(1, activation = 'sigmoid') # softmax == (sparse_)catogorical_crossentropy
    ])
# model.summary()
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy']) # one hot encoding == not sparse
model.fit(trainX, trainY, validation_data=(valX, valY), batch_size = 64, epochs = 5, verbose = 2) # update weights more frequently ## 40 ~ 100 verbose 2 (print)
# acc 91.93 %
model.save(r"D:\2022\Python\Tensorflow\apple_deeplearning_seq\cleanbot\model1")
