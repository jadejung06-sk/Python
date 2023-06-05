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
### int : Fare, Parch SibSp == tf.feature_column.numeric_column
### int to cat : Age == tf.feature_column.bucketized_column
### cat with few types : Sex Embarked Pclass == tf.feature_column.indicator_column
### cat with too many types : Ticket == tf.feature_column.embedding_colum (matrix)

feature_columns = []
tf.feature_column.numeric_column('Fare')
tf.feature_column.numeric_column('Parch')
tf.feature_column.numeric_column('SibSp')
tf.feature_column.numeric_column('Age')




##############################################