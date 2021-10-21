import random
num = random.randint(1,20)
Trial = 5
Name = input('Hello, what is your name?')
print('Well,',Name, 'I am thinking of a number between 1 and 20.')
count = 0
while count < 6:
    guess = int(input('Take a guess'))
    if guess == num:
        print('Correct')
    elif guess < num:
        print("that's below")
    else:
        print("Too high")
    count = count+1
    Trial -=1
    print('You have',Trial, 'time left')
if count == 5:
    print('You have exhausted your trials','i was thinking of', num)

