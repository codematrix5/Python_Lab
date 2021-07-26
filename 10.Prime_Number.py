num = int(input("Enter thr number : "))
prime = True
for i in range (2,num):
    if num%i==0:
       prime= False
       break
if prime is True:
    print(f"{num} is  prime")

else:
    print(f"{num} is  not  prime")