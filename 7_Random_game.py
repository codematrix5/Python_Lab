# Programe on guess the random no 

import random
n=20

n= int(n * random.random()) +1

guess =0
while guess!= n:
    guess=int(input("Enter No : "))
    if guess < n:
        print("No is too small")
    elif guess > n:
         print("No is too large")
    else:
        print ("congrats")

print(" GD bye")
        
