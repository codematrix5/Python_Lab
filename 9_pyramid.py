# Print Pyramid triangle

for i in range (4):
    
    for j in range(4-i):
         print(' ',end='')
    for j in range(i):
        print('*',end="")
    for j in range(i):
        print('*',end="")
    print("*")


