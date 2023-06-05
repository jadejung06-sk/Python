import pandas as pd
import tensorflow as tf

##### Data
data = pd.read_csv(r"D:\2022\Python\Tensorflow\apple_deeplearning_seq\Titanic\train.csv")
# print(data.isnull().sum()) # age 177 Embarked 
# print(data) 
mean = data['Age'].mean() # 29.699
data["Age"].fillna(value = 30, inplace = True)
mode = data['Embarked'].mode()
data['Embarked'].fillna(value = 'S', inplace= True)
# print(data.isnull().sum())
##############################################


##### preprocessing
answer = data.pop('Survived')
ds = tf.data.Dataset.from_tensor_slices((dict(data), answer))
# print(ds) # <_TensorSliceDataset element_spec...
# for i, l in ds.take(1):
    # print(i) # {'PassengerId': <tf.Tensor: shape=(), dtype=int64, numpy=1>,  ...
    # print(l) # tf.Tensor(0, shape=(), dtype=int64)
##### feature columns (int - int / cat - encoding)
# > https://www.tensorflow.org/guide/migrate/migrating_feature_columns?hl=ko
### int : Fare, Parch SibSp == tf.feature_column.numeric_column
### int to cat : Age == tf.feature_column.bucketized_column
### cat with few types : Sex Embarked Pclass == tf.feature_column.indicator_column
### cat with too many types : Ticket == tf.feature_column.embedding_colum (matrix)
feature_columns = []
feature_columns.append(tf.feature_column.numeric_column('Fare'))
feature_columns.append(tf.feature_column.numeric_column('Parch'))
feature_columns.append(tf.feature_column.numeric_column('SibSp'))
# tf.keras.layers.Normalization(mean=2.0, variance=1.0) 
# feature_columns.append(tf.feature_column.numeric_column('Age'))
Age = tf.feature_column.numeric_column('Age')
feature_columns.append(tf.feature_column.bucketized_column(Age, boundaries=[10, 20, 30, 40, 50, 60]))
# print(feature_columns)
## cat with few types
vocab = data['Sex'].unique()
cat = tf.feature_column.categorical_column_with_vocabulary_list('Sex', vocab)
one_hot = tf.feature_column.indicator_column(cat)
feature_columns.append(one_hot)

vocab = data['Embarked'].unique()
cat = tf.feature_column.categorical_column_with_vocabulary_list('Embarked', vocab)
one_hot = tf.feature_column.indicator_column(cat)
feature_columns.append(one_hot)

vocab = data['Pclass'].unique()
cat = tf.feature_column.categorical_column_with_vocabulary_list('Pclass', vocab)
one_hot = tf.feature_column.indicator_column(cat)
feature_columns.append(one_hot)
## embedding
vocab = data['Ticket'].unique()
cat = tf.feature_column.categorical_column_with_vocabulary_list('Ticket', vocab)
one_hot = tf.feature_column.embedding_column(cat, dimension=9)
feature_columns.append(one_hot)
##############################################

##### modeling
model = tf.keras.Sequential([
    tf.keras.layers.DenseFeatures(feature_columns),
    tf.keras.layers.Dense(128, activation= 'relu'),
    tf.keras.layers.Dense(64, activation= 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation= 'sigmoid')
])
model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['acc'])
ds_batch = ds.batch(32)
model.fit(ds_batch, shuffle = True, epochs = 20)
