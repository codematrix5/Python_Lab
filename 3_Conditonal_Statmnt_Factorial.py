# Factorial of a number
fact = 1
x= int(input("Enter the number : "))


while x!=0 :
    if x<0 :
        print("NUmber must be positive")
        break
    if x>0 :
       fact= fact * x
       x -= 1

print(f"factorial of {x} is {fact}")


#  For loop for factorial

if x<0:
    print("Number must be positive")
elif x==1:
    print( "Factorial = 1")
else :
    for i in range (1,x+1):
        fact = fact*i
    print(f"factorial of {x} is {fact}")