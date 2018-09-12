import random
n=100
generate=[random.randint(1,5) for x in range(0,n)] #computer generating random numbers for learning and total 100 numbers in range 1-5 is generated
user_input=[int(input("enter a number")) for y in range(0,n)] #enter the user input
c = [0]*n
for i in range(0,n):
    if(generate[i] == user_input[i]):
        c[i]=1
print(user_input,generate,c)        
