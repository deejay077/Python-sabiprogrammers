# for loops
'''for someting(variable) in something(variable, range):
    do something
OR
for iterating_value in sequence:
    do something
    '''

name = 'triumph'
for letter in name:
    print(letter)

# print out even numbers
for num in range(0,11,2): #(start, stop, step)
    print(num)

# odd numbers
for num in range(1,11,2): #(start, stop, step)
    print(num)

# Even and Odd numbers
for num in range(11):
    if num%2 == 0:
        print(num,'is even')
    else:
        print(num, 'is odd')

# for loops for 1 multiplication table (1-12)
number = int(input('Enter what number you want to see: '))
for j in range(1,13):
        print(number, '*', j, '=', number*j)

# Nested for loops or multiple multiplication table 
for i in range(1,number+1):
    for j in range(1,13):
        print(i,'*',j, '=', i*j)
    print()

# Sample Assignment
import random
num = random.randint(1,20)

name = input('Nmae?')
print('i\'m thinking of a number, take a guess')
guess = int(input())
if guess == num:
    print('that is right')
elif guess < num:
    print('too low')
else:
    print('too high')

