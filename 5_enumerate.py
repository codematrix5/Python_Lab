# USe of enumerate key word

word='abcdef'

for items in enumerate(word):
    print(items)

# ============================================================

for index,letter in enumerate(word):
    print(index,letter)

# ==============================================================


list=["q","r","s","t"]


for items in enumerate(list):
    print(items)
    
for index,letter in enumerate(list):
    print(index,letter)