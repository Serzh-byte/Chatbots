import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Initialization of Tensors
x = tf.constant(4, shape=(1, 1), dtype=tf.float32)  # --> initialization of constants
y = tf.constant([[1, 2, 3], [4, 5, 6]])  # --> Two dimensional tensor

z = tf.ones((3, 3))  # --> 3x3 dimensional tensor of ones
a = tf.eye(3)  # --> I(eye) for identity matrix (i.e. ones diagonally and zero everywhere else)
b = tf.random.normal((3, 3), mean=0, stddev=1)
c = tf.random.uniform((1, 3), minval=0, maxval=1)
d = tf.range(start=1, limit=10, delta=2)  # --> tensor from 1 to 9
# Limit is for the end, start is for the start and delta is for the step
e = tf.cast(d, dtype=tf.float32)  # --> changing the type

# Mathematical Operations
x = tf.constant([1, 2, 3])
y = tf.constant([9, 8, 7])

z = tf.add(x, y)  # adding each value
z = tf.subtract(x, y)  # subtracting the values

z = tf.multiply(x, y)  # multiplying each value
z = tf.divide(x, y)  # dividing each value

z = tf.tensordot(x, y, axes=1)  # performing dot product along specified axes

x = tf.random.normal((2, 3))
y = tf.random.normal((3, 4))
z = tf.matmul(x, y)

# Indexing
x = tf.constant([0, 1, 1, 2, 3, 1, 2, 3])
# print(x[:])  # printing all the elements
# print(x[1:])  # printing everything except the one on the 0 index
# print(x[1:3])  # printing everything from index 1 to 3(not inclusive)
# print(x[::2])  # slices with two steps
# print(x[::-1])  # printing in reverse order

indices = tf.constant([0, 3])
x_ind = tf.gather(x, indices)  # gathers the first index and the 3rd index

# Corrected part
x = tf.constant([[1, 2], [3, 4], [5, 6]])  # 2D tensor

#print(x[0])  # prints the first row of the tensor
#print(x[0,:]) # does the same thing as above
#print(x[0:2, :1]) # print the first and second row of the tensor, the ,: specifies which characters we tak from each row

x = tf.range(9)
print(x)

x = tf.reshape(x, (3, 3)) #reshaping the tesnor

x = tf.transpose(x, perm=[1,0]) #this will swap the axis