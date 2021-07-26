#  onvert temp into farenhite from celcius and save it in list(more complex formulas for list append method) // List Comprehesion//

celcius=[0,5,10,12,15]


farenhite=[((9/5)*temp +32) for temp in celcius]

print(farenhite)


#  do same thing from for loop
farenhite=[]
for temp in celcius:
    temp = (9/5)*temp +32

    farenhite.append(temp)

print(farenhite)