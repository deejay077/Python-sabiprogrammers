# Tuples is a collection which is ordered and unchangeable. Allows duplicate members.

furniture = ('Table','chair','bin bags', 'sofa', 'chair', 'light','Sink','Chair', 'sink')
print(furniture)

print(furniture[1]) # indexing
# methods
# len()
print(len(furniture))
# count() --- returns how many times an item occurs in a tuple
print(furniture.count('chair'))
# index() --- returns first index of an item
print(furniture.index('Sink'))