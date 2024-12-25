import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations

import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.metrics import accuracy_score

# Load and preprocess data
df = pd.read_csv('Churn.csv')
X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build and compile the model
model = Sequential([
    Input(shape=(len(X_train.columns),)),  # Explicitly define input shape
    Dense(units=32, activation='relu'),
    Dense(units=64, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=200, batch_size=32)

