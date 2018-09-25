string = (input("Please enter a string: ")).split()
print(string)
dict_1 = {}
for word in string:
    if word in dict_1:
        dict_1[word] +=1
    else: 
        dict_1[word]=1
print(dict_1)