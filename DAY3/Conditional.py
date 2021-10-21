# Flow Control
# condition and clause (code block)
'''if condition:
       do something
   elif another condition:
       do something
    else:
        do something'''

name = input('Enter your name: ').lower()
if name == 'triumph':
    print('Welcome')
elif name == 'deji':
    print(f"welcome {name}, how is akure today")
else:
    print('Who are you?')

# Weac grading
score = int(input('Enter your score: '))
subject = input('Enter the subject: ')
max_score = 100
if score >= 70 and score <= max_score:
    print(f'You had A in {subject}')
elif score >= 60 and score < 70:
    print(f'You had B in {subject}')
elif score >=50 and score < 60:
    print(f'You had C in {subject}')
elif score >=45 and score < 50:
    print(f'You had D in {subject}')
else:
    print(f'You had F in {subject}')

# Nested ifs
name = input('Enter you name: ').lower()

if name == 'triumph' or 'deji':
    print(f'Hi {name}, what is your level?')
    level = int(input('Enter your level: '))
    if level >= 3:
        print('Welcome, now tell me your password')
        password = input()
        if name == 'triumph' and password == '1234':
            print(f'Oh its actually you {name}')
        elif name == 'deji' and password == '4321':
            print(f'Oh its actually you {name}')
        else:
            print('wrong password')
    elif level < 3:
        print('Please use the systems on floor 1, you can\'t access this')
    else:
        print('Lower levels don\'t have access')
else:
    print('Biko, who you be?')