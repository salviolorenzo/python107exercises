word = input('Please enter a word: ')
dict_1 = {}
for letter in word:
    if letter in dict_1:
        dict_1[letter] +=1
    else:
        dict_1[letter] = 1
            
print(dict_1)
    