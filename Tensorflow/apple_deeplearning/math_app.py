import tensorflow as tf


##### math 0
# height = [170, 180, 175, 160]
# shoes = [260, 270, 265, 255]
# y = ax + b

##### math 1
# height = 170
# shoes = 260
# # shoes = height * a + b
# a = tf.Variable(0.1)
# b = tf.Variable(0.2)
# def loss_func():
#     yhat = height * a + b # a single value
#     return tf.square(260 - yhat)
# opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
# # opt.minimize(loss=loss_func , var_list= [a , b]) # only once, all weight varialbes
# for i in range(300):
#     opt.minimize(loss=loss_func , var_list= [a , b])
#     # print(a, b)
#     print(a.numpy(), b.numpy())    
##### math 2 - learning (w/o hidden layers)
train_x = [1,2,3,4,5,6,7]
train_y = [3, 5, 7, 9, 11, 13, 15]

# a = tf.Variable(0.1, tf.int32) # 0.1 > Randomize
a = tf.Variable(0.1) # 0.1 > Randomize
b = tf.Variable(0.1) # 0.1 > Randomize

# def loss_func():
def loss_func(a, b):
    pred_y = train_x * a + b
    return tf.keras.losses.mse(train_y, pred_y) # list list

opt = tf.keras.optimizers.Adam(learning_rate=0.01) # 0.001 0.01
for i in range(2900): # 300 600 900 2900
    # opt.minimize(loss_func, var_list= [a, b])
    opt.minimize(lambda: loss_func(a, b), var_list= [a, b]) # 
    print(a.numpy(), b.numpy())
