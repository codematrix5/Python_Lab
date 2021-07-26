# Sum of first n natural numbers using while loop and for loop

num = int(input("Enter the number :"))
sum = 0
i=0

# Using for loop

for i in range (1, num+1):
    sum=sum+i
print(f"Sum of first {num} natural numbers is {sum}")


#  from while loop

while i in range (num+1):
     sum=sum+i
     i+=1
print(f"Sum of first {num} natural number is : {sum}")
     