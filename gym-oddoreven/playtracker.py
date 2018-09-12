import random
from keras.models import Sequential
from keras.layers import Dense,InputLayer
n=100
generate=[random.randint(1,5) for x in range(0,n)] #computer generating random numbers for learning and total 100 numbers in range 1-5 is generated
user_input=[int(input("enter a number")) for y in range(0,n)] #enter the user input
binary_train = [0]*n
for i in range(0,n):
    if(generate[i] == user_input[i]):
        binary_train[i]=1
print(user_input,generate,binary_train)        
model = Sequential()
model.add(Dense(2, input_dim=1, kernel_initializer='normal', activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(generate,binary_train,epochs=10,verbose=0)
gen_test=[random.randint(1,5) for x in range(0,n)]
ytest=[int(input("enter the numbers for testing")) for y in range(0,n)]
binary_test=[0]*n
for i in range(0,n):
    if(gen_test[i]==ytest[i]):
       binary_test[i]=1 
loss, acc = model.evaluate(gen_test, binary_test, verbose=0)
print(gen_test,ytest)
print(loss,acc)
