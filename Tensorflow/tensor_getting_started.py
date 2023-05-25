##### python version
## 3.X 64 bit
# > Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
'''
python
'''

##### pip install tensorflow
'''
pip install tensorflow
'''

##### GPU
## GPU List
# >>> https://developer.nvidia.com/cuda-gpus
## My Desktop
# >>> https://gbworld.tistory.com/720
# cmd > dxdiag > display > name : AMD Radeon RX 6600 (no gpu being used)
# > not CUDA but OpenCL 
'''
Radeon > ROCm or directml
'''

##### ml
## get the greatest weight

##### hidden layer
## place to think 

##### Loss Function (Cost Function)
## get the lowest error

##### activation of neural net
## non-linearity and complexity

##### w1 = w1 - gredient of w1
## get E
## w1
## get E
## w1 
## get E

##### w1 = w1 - learning rate * gredient of w1 (Trial and Error)
## global minimum

##### Optimizer of learning rate (Trial and Error) - Adam
## dynimic learning rate
## Adagrad : big different w1 gets smaller,  the small different w1 gets bigger (local minima)

##### back 
## update 
# 
# w6 w5 w4 w3 w2 w1 

##### + - * / tensors
## dot product == tf.matmul()
'''
tf.add(tensor1, tensor2)
tf.subtract(tensor1, tensor2)
tf.divide(tensor1, tensor2)
tf.multiply(tensor1, tensor2)
tf.matmul(tensor1, tensor2)
'''

##### zeros makes the empty tensor
## [2,2,3] : reversed!! 3 zeros > 2 rows > 2 times
'''
tensor6 = tf.zeros(10)
tensor7 = tf.zeros([2,2])
tensor8 = tf.zeros([2,2,3])
print(tensor6) # tf.Tensor([0. 0. 0. 0. 0. 0. 0. 0. 0. 0.], shape=(10,), dtype=float32)
print(tensor7) # tf.Tensor([[0. 0.] [0. 0.]], shape=(2, 2), dtype=float32)
print(tensor8) # reversed!! 3 zeros > 2 rows > 2 times
'''

##### dtype float32 rather than int32
## [3.0, 4, 5]
## [3,4,5], tf.float32
## tf.cast()
'''
tensor10 = tf.constant([3,4,5], tf.float32)
print(tensor10)
'''

##### Variable == weight
## tf.Variable(1).assign(2).numpy()
'''
tf.Variable()
tf.Variable(1.0) <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
print(w.numpy()) # 1.0
w.assign(2)
print(w, w.numpy()) # <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>
'''