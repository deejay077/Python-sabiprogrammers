# Dictionaries is a collection which is unordered, changeable and indexed. No duplicate members
# dict = {key:value}

student = {'name': 'Triumph','age':12,'color':'white','country':'UK'}
print(student)

students = {
    'Names':['Triumph','Deji','Obed'], 
    'Age': (12, 13, 14),
    'color':{'green':'vert','white':'blanc','red':'rogue'}, 
    'country':{'Uk','Canada','Nigeria'}
    }
'''print(students)

# methods in dictionary
# len()
print(len(students))

# accessing or indexing
print(students['color'])
print(students['Names'][0]) # accessing elements of Names(list)
print(students['color']['green']) # accessing elements of color(dictionary)
print(students['Age'][1]) # accessing elements of Age(tuple)

# get()
x = students.get('Age')
print(x)

# pop() --- removes the item at a speciifed key
students.pop('Age')
print(students)

# popitem() --- removes the item at the last key
students.popitem()
print(students)'''

# clear --- returns an empty dictionary
student.clear()
print(student)

# del
del students['Names'] # delete a key
print(students)

del students # delete entire dictionary
print(students)