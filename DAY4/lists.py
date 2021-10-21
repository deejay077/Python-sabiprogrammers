# Lists is a collection which is ordered and changeable. Allows duplicate members.

food_stuff = ['fish','eggs','oil','banana', 'oil']
# indexing
print(food_stuff[:-2])

# Changing items
'''food_stuff[-1] = 'palm oil'
print(food_stuff)

# methods
# len() ---- length of the list
print(len(food_stuff))

# append() ---- adds items to end of a list
food_stuff.append('Golden Morn')
food_stuff.append(['soap','perfume','makeup'])
#print(food_stuff)
beauty = ['soap','perfume','makeup']
market = food_stuff.append(beauty)
print(market)
print(food_stuff[6][1])

# insert() ---- inserts at a given index
food_stuff.insert(3,'meat')
print(food_stuff)

# remove --- removes a specific item from list
food_stuff.remove('oil')
print(food_stuff)

# pop --- removes last item in list
food_stuff.pop()
print(food_stuff)

# clear --- removes all items in list and returns empty list
food_stuff.clear()
print(food_stuff)

# del --- deletes the list
del food_stuff
print(food_stuff)

# list constructor
food = ['spag', 'beans','rice']
food2 = list(('spag', 'beans','rice'))
print(food, food2)'''

