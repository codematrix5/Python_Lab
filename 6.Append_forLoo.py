string ="Hello world"

mylist=[]

for items in string:
    mylist.append(items)
print(mylist)

# Easier methof by breaking for loop

mylist= [letters for  letters in string ]

print(mylist)

# ===========================================================

# Another type of operation in appending a list

list2=[]

list2=[num**2 for num in range(1,11)]   # will append squares of numbers in list for range 1 to 10

# Now lets say i want to capture square of no that are even

list2=[num**2 for num in range(1,11) if num%2==0]   # will return only square of number that are  even


print(list2)