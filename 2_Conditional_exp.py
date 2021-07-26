Num1= int(input("Enter the Number 1 : "))
Num2= int(input("Enter the Number 2 : "))
Num3= int(input("Enter the Number 3 : "))
Num4= int(input("Enter the Number 4 : "))

if (Num1>Num2 and Num1>Num3 and Num1>Num4):
    print("Num1 is greatest ")
elif (Num2>Num1 and Num2>Num3 and Num2>Num4):
    print("Num2 is greatest ")
elif (Num3>Num2 and Num3>Num1 and Num3>Num4):
    print("Num3 is greatest ")
# elif (Num4>Num2 and Num4>Num3 and Num4>Num2):
#     print("Num4 is greatest ")
else:
    print("Num4 is greatest")

# second method

if (Num1>Num2):
    n1=Num1
else:
    n1=Num2
if(Num3>Num4):
    n2=Num3
else:
    n2=Num4

if (n1>n2):

    print(str(n1) + " Is greatest")
else:
    print(str(n2) + " Is greatest")