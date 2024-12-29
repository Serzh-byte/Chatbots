import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #ignore the information messsages from tensorflow

import tensorflow as tf
from tensorflow import keras # keras is for neural networks
from tensorflow.keras import layers # type: ignore
from tensorflow.keras.datasets import mnist # type: ignore

(x_train, y_train), (x_test, y_test) = mnist.load_data() # loading the data from mnist
print(x_train.shape)