import numpy as np
import pandas as pd
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
unique_text = list(set(unique_text))
unique_text.sort()
# print(unique_text[:100])