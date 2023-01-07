myvar= {'name':'Murad', 'age': 27}
#update the value of the dictionary
myvar.update({'name': 'Ali'}) 
#updating in another way
myvar['age'] = 28

#to see the output remove the hash tag of the following line
#print(myvar)

#to clear a dictionary
#print(myvar.clear())

#lists into a dictionary
list1 = ['Jhon', 'Smith', 'Ali']
list2 = [10, 20, 50]

#accumulate two lists using zip and convert into dictionary
newvar = dict(zip(list1,list2))

#print the dictionary
#print(newvar)

#to get a value
getvar = newvar.get(list1[0])

#print the key
#print(getvar)

#formkeys in python dictionary
#declaring the keys
alphabates = ['a', 'e', 'i', 'o', 'u']
#declearing the value
character = 'vowel'

output = dict.fromkeys(alphabates, character)

#print(output)



