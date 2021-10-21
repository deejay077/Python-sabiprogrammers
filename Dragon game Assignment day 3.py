
print('''You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')


Play_again = 'Yes'
while Play_again == 'Yes':
    cave = ""
    while cave != "1" and cave != "2":
        cave = input('Which cave will you go into? (input(1 or 2):')
        print(cave)
    print('''You approach the cave... 
    It is dark and spooky... 
    A large dragon jumps out in front of you! 
    He opens his jaws and... 
    ''')   
    import random
    Comp_cave = random.randint(1,2)
    if cave ==  Comp_cave:
        print('Gives you his treasures')
    else:
        print('Gobbles you down in one bite!')
    print('Do you want to play again?, Yes or No')
    Play_again = input()
    

