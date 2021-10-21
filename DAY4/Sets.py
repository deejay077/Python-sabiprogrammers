#{} Sets is a collection which is unordered and unindexed. No duplicate members.

students = {'Triumph', 'Obed','Deji', 'Folarin'}
print(students)
print('Obed' in students)

# methods
# add() --- adds an item to the set
students.add('Miriam')
# update() --- adds multiple items to set
students.update(('Chuks','Tobi','surfy'))
print(students)
# remove() --- removes item from set and raises an error if item is not present
students.remove('Tobi')
print(students)
students.remove('tola')
print(students)
# discard() --- removes item from set and does not raise an error if item is not present
students.discard('Obed')
print(students)
students.discard('tola')
print(students)
# pop() --- removes last item in set
students.pop()
print(students)
# clear() --- returns an empty set
students.clear()
print(students)
# del --- deletes the set
del students
