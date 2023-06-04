import tensorflow as tf
import numpy as np

Pmodel1 = tf.keras.models.load_model(r'D:\2022\Python\Tensorflow\apple_deeplearning_seq\LSTM\model1')
##### read text file
text = open(r"D:\2022\Python\Tensorflow\apple_deeplearning_seq\LSTM\pianoabc.txt", "r").read()
unique_text = list(set(text))
unique_text.sort()
##### utilities
### encoding (def or dict)
text_to_num = {}
num_to_text = {}
for i, data in enumerate(unique_text):
    text_to_num[data] = i
    num_to_text[i] = data 

numbered_text = []
for i in text:  
    numbered_text.append(text_to_num[i])
# print(numbered_text[117: 117+25])
first_input = numbered_text[117: 117+25]
first_input = tf.one_hot(first_input, 31)
first_input = tf.expand_dims(first_input, axis = 0)
# print(first_input)

##### prediction (test)
# first_pred = Pmodel1.predict(first_input)
# print(np.argmax(first_pred)) # index 5
# # print(first_pred) # propotion
# # print(num_to_text) #  
# print('Predictional value :', num_to_text[5]) # 
# print('Real :', numbered_text[117+25])

##### 
## Trial 1:
# outputs = []
# for idx in range(len(numbered_text) - 25):
#     inputs = numbered_text[idx : idx+ 25]
#     inputs = tf.one_hot(inputs, 31)
#     inputs = tf.expand_dims(inputs, axis = 0)
#     outputs.append(Pmodel1.predict(inputs))
# print(outputs)

## Trial 2:
music = []
for i in range(200):
    pred = Pmodel1.predict(first_input)
    # pred = np.argmax(pred[0]) #  27 int
    # print(pred, type(pred))
    pred = np.random.choice(unique_text, 1, p = pred[0])
    pred = text_to_num[str(pred[0])]
    music.append(pred)
    # print(first_input.numpy()[0][1:]) # 25 lists - 24 lists
    next_input = first_input.numpy()[0][1:] # numpy
    one_hot_num = tf.one_hot(pred, 31) # Tensor
    # print('one_hot_num :', one_hot_num) # [0. 0. 0. 0. ...  0. 0. 0. 0. 0. 0. 0.], shape=(31,), dtype=float32)
    first_input = np.vstack([next_input, one_hot_num.numpy()])
    first_input = tf.expand_dims(first_input, axis = 0)
    # print(first_input.shape) # 1 25 31
# print(first_input)
# print(music)

music_text = []
for data in music:
    music_text.append(num_to_text[data])
print(''.join(music_text))