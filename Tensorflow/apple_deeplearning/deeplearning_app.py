import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))

##### basic    
tensor1 = tf.constant(3)
tensor2 = tf.constant([3,4,5])
print(tensor1) # tf.Tensor(3, shape=(), dtype=int32)
print(tensor2) # tf.Tensor([3 4 5], shape=(3,), dtype=int32) 

##### add tensors
tensor3 = tf.constant([3,4,5])
tensor4 = tf.constant([6,7,8])
print(tf.add(tensor3, tensor4))
print(tensor3 + tensor4) # tf.Tensor([ 9 11 13], shape=(3,), dtype=int32)

##### 2 x 2 shape
tensor5 = tf.constant([[1,2], [3,4]])
print(tensor5) # tf.Tensor([[1 2] [3 4]], shape=(2, 2), dtype=int32)

##### zeros makes the empty tensor
tensor6 = tf.zeros(10)
tensor7 = tf.zeros([2,2])
tensor8 = tf.zeros([2,2,3])
print(tensor6) # tf.Tensor([0. 0. 0. 0. 0. 0. 0. 0. 0. 0.], shape=(10,), dtype=float32)
print(tensor7) # tf.Tensor([[0. 0.] [0. 0.]], shape=(2, 2), dtype=float32)
print(tensor8) # reversed!! 3 zeros > 2 rows > 2 times

##### shape 
print(tensor2.shape) # (3,) == 3 data
print(tensor5.shape) # (2,2) == 2 data > 2 rows
tensor9 = tf.constant([[1,2,3], [4,5,6]])
print(tensor9.shape) # (2, 3) == 3 data > 2 rows
