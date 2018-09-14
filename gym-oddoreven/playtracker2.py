#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 19:10:28 2018

@author: abhijith
"""

import random
from keras.models import Sequential
from keras.layers import Dense,InputLayer
from keras.layers import LSTM
from numpy import array
from keras.layers import TimeDistributed
def sequence_gen(n):
    n=5
    generate=array([random.randint(1,5) for x in range(0,n)]) #computer generating random numbers for learning and total 100 numbers in range 1-5 is generated
    user_input=[int(input("enter a number")) for y in range(0,n)] #enter the user input
    binary_train = array([0]*n)
    for i in range(0,n):
        if(generate[i] == user_input[i]):
            binary_train[i]=1
    print(user_input,generate,binary_train) 
    generate = generate.reshape(1,n,1)
    binary_train= binary_train.reshape(1,n,1)
    return generate,binary_train       
model = Sequential()
model.add(LSTM(20, input_shape=(5, 1), return_sequences=True))
model.add(TimeDistributed(Dense(1, activation='sigmoid')))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
for epoch in range(100):
    generate,binary_train=sequence_gen(5)
    model.fit(generate,binary_train,epochs=1,batch_size=1,verbose=2)
gen_test,ytest=sequence_gen(5)
pred = model.predict_classes(gen_test, verbose=0)
for i in range(5):
	print('Expected:', ytest[0, i], 'Predicted', pred[0, i])
print(gen_test,ytest)

