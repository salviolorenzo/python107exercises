string = (input("Please enter a string: ")).split()
dict_1 = {}
for word in string:
    if word in dict_1:
        dict_1[word] +=1
    else: 
        dict_1[word]=1
print(dict_1)

val_list=[]
for keys in dict_1.items():
    for val in keys:
        if type(val) is int:
            val_list.append(val)

counter = 0
while counter < 3:
    maxi = max(val_list)
    print(list(dict_1.keys())[list(dict_1.values()).index(maxi)], end=": ")
    print(maxi)
    val_list.remove(maxi)
    counter +=1



