# While loops
'''while condition:
     do something'''

num = 1
while num < 10:
    print(num)
    num = num + 1
    if num == 10:
        print('you have reached the end')
# using break statement

while True:
    name = input('Enter your name: ')
    if name == 'Triumph':
        break

# using continue statement
while True:
    name = input('Enter your name: ')
    if name == 'Triumph':
        continue
    if name == 'deji':
        break

# elevator going up
current = int(input('Enter your current floor: '))
destination = int(input('Enter your destination floor: '))
while current < destination:
    print('Now, You are on floor', current)
    current = current + 1

    if current == destination:
        print('We have arrived at floor', destination)

# Try yours for going down