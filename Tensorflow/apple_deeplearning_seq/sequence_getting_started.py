# 1. vector to sequence (이미지 자동 캡션)
# 2. sequence to vector (글의 감정분석하기, 악플검사하기)
# 3. sequence to sequence (번역)
# > http://dmqm.korea.ac.kr/activity/seminar/283 
# > https://ko.khanacademy.org/math 
# 선형대수/확률통계 편도

# Simple Recurrent Neural Network (재발하는)
# : Input – activation – output
# : low accuracy due to diminishing gradient (첫 글자의 중요도가 희석)

# Long Short Term Memory
# H1 & CELL STATE

### LSTM or GRU
## 1 LSTM
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(100, input_shape = (25, 31)),
    tf.keras.layers.Dense(31, activation = 'softmax') # softmax == (sparse_)catogorical_crossentropy
    ])
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam') # one hot encoding == not sparse
'''

## > 2 LSTM return_sequeces = True
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(100, input_shape = (25, 31), return_sequences= True), # node, a single sample
    tf.keras.layers.LSTM(100), 
    tf.keras.layers.Dense(31, activation = 'softmax') # softmax == (sparse_)catogorical_crossentropy
    ])
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam') # one hot encoding == not sparse
'''

##### raise ValueError(
# ValueError: Input 0 of layer "sequential" is incompatible with the layer: expected shape=(None, 25, 31), found shape=(None, 31)
# first_pred = Pmodel1.predict(first_input)
'''
first_input = tf.expand_dims(first_input, axis = 0)
first_pred = Pmodel1.predict(first_input)
'''

##### TypeError: _vhstack_dispatcher() takes 1 positional argument but 2 were given
# next_input = first_input.numpy()[0][1:] # numpy
# one_hot_num = tf.one_hot(pred, 31) # Tensor
# first_input = np.vstack(next_input, one_hot_num.numpy())
'''
first_input = np.vstack([next_input, one_hot_num.numpy()])
'''

##### prediction randomly
# pred = Pmodel1.predict(first_input)
# pred = np.argmax(pred[0])
# music.append(pred)
'''
pred = np.random.choice(unique_text, 1, p = pred[0])
pred = text_to_num[str(pred[0])]
music.append(pred)
'''

##### tokenizer
###
## char_level True == letter
## char_level False == word
### 
## <OOV> or 없는단어 == no letter preproceesed

'''
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level = True, oov_token="<OOV>" )
tokenizer = Tokenizer( 1000, char_level=True, oov_token="<OOV>") # limit of number
'''


##### duplicated_words 
# only one word
'''
import itertools
raw['review'] = raw['review'].applymap(lambda x: ''.join(ch for ch, _ in itertools.groupby(x)))
'''
'''
df["Col"] = df["Col"].str.replace(r"\s+(.)\1+\b", "").str.strip()
'''

##### Korean NLP
# Hannanum, Kkma, Mecab, Okt
'''
from konlpy.tag import Mecab
mecab = Mecab()
stopwords = ['는','은','다','을','를']
raw['tokenized'] = raw['reviews'].apply(mecab.morphs) 
raw['tokenized'] = raw['tokenized'].apply(lambda x: [item for item in x if item not in stopwords])
x데이터 = raw['tokenized'].values
'''
## Grammer
'''
from hanspell import spell_checker
hangul = "마춤법 검사 하면 문장이 깔끔해지구 학습이 잘됀다"
hangul2 = spell_checker.check(hangul)
print(hangul2.checked)
'''

## same pronunciation but different meaning
# ELMO


##### raise ValueError(
# ValueError: Failed to find data adapter that can handle input: <class 'numpy.ndarray'>, (<class 'list'> containing values of types {"<class 'int'>"})
'''
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level = True, oov_token= '<OOV>' )
string_list = raw['review'].tolist()
tokenizer.fit_on_texts(string_list)
train_seq = tokenizer.texts_to_sequences(string_list)
Y = raw['label'].tolist()
X = tf.keras.preprocessing.sequence.pad_sequences(train_seq, maxlen = 100)
X = X.tolist()
trainX, valX, trainY, valY = train_test_split(X, Y, test_size = 0.2, random_state= 42)
'''

##### timeseries
# stationary

#####   ValueError: Exception encountered when calling layer 'dense_features' (type DenseFeatures).
# Feature (key: Age) cannot have rank 0. Given: Tensor("sequential/dense_features/Cast:0", shape=(), dtype=float32)
'''
ds = tf.data.Dataset.from_tensor_slices((dict(data), answer))
ds_batch = ds.batch(32)
model.fit(ds_batch, shuffle = True, epochs = 20)
'''

##### DenseFeatures
'''
ds_batch = ds.batch(32)
# next(iter(ds_batch))[0]
feature_layer = tf.keras.layers.DenseFeatures(tf.feature_column.numeric_column("Fare"))
feature_layer(next(iter(ds_batch))[0])
'''

##### Nomarlizing
'''
def normalize(x):
    min = data['Fare'].min()
    max = data['Fare'].max()
    return (x - min) / (max - min) 
tf.feature_column.numeric_column('Fare', normalizer_fn = normalize)
'''

##### validation_data
# model.fit(ds, validation_split = 0.2) # Error
'''
from sklearn.preprocessing import Tra

model.fit()
'''


