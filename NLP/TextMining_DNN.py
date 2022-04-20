# pip install tensorflow
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df=pd.read_csv('./sources/dataset/spam.csv')
df['target'] = df['label'].map( {'spam':1, 'ham':0 })
print(df.head())

text_train = np.asarray(df['sms'])
y_train = np.asarray(df['target'])
print(text_train[:3])
print(y_train[:3])

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words="english", min_df=5).fit(text_train)
X_train = vect.transform(text_train)
print(X_train.shape)
print(y_train.shape)
print(y_train[:5])

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=(1602,)),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='softmax')
])

model.compile(optimizer=keras.optimizers.Adam(),
             loss=keras.losses.SparseCategoricalCrossentropy(),
             metrics=['accuracy'])
model.summary()

history = model.fit( X_train,  np.array(y_train) , batch_size=64, epochs=10, verbose=2)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train2, y_test = train_test_split(X_train, y_train , test_size=0.3 , shuffle=False)
history = model.fit(x_train , y_train2, batch_size=64, epochs=10 , validation_data = [x_test,y_test], verbose=2)

sms_test = ['Hi Paul, would you come around tonight']
test_str  = vect.transform(sms_test)

pred = model.predict(test_str)
np.argmax(pred, axis=1)

sms_test = ['Free SMS service for anyone']
test_str  = vect.transform(sms_test)
pred = model.predict(test_str)
np.argmax(pred, axis=1)

import tensorflow as tf
print(tf.test.is_built_with_cuda()) # 判斷CUDA是否可以用
print(tf.test.is_gpu_available(cuda_only=False,min_cuda_compute_capability=None)) # 判斷GPU是否可以用