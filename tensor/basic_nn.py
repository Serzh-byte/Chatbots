import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Ignore the information messages from TensorFlow

import tensorflow as tf
from tensorflow import keras  # Keras is for neural networks
from tensorflow.keras import layers  # Type: ignore
from tensorflow.keras.datasets import mnist  # Type: ignore

(x_train, y_train), (x_test, y_test) = mnist.load_data()  # Loading the data from MNIST
x_train = x_train.reshape(-1, 784).astype('float32') / 255.0  # Flattening the data, -1 means keep the 60000, 784 is 28x28
x_test = x_test.reshape(-1, 784).astype('float32') / 255.0  # Dividing by 255 makes the values between 0 and 1

# Sequential API by Keras (Very convenient, not very flexible)
# It's one input to one output

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=(784,)),  # Adding input_shape to specify input dimensions
    layers.Dense(256, activation='relu'),
    layers.Dense(10)  # Output layer for 10 classes
])

model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),  # from_logits=True, because the output is not softmax
              optimizer=keras.optimizers.Adam(learning_rate=0.001),  # Changed lr to learning_rate
              metrics=['accuracy'])  # Corrected 'metric' to 'metrics'

model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)  # Training the model
model.evaluate(x_test, y_test, batch_size=32, verbose=2)  # Evaluating the model