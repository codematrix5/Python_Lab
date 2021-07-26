for i in range(5,1,-1):
    j=i
    while j==i:
        print("Hi", i*j)
        i+=1
    if i+j>10:
        continue
    print(i**2)

else:
    print("Loops is done")