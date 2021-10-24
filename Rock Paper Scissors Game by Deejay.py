#Rock Paper Scissors Game by Deejay
'''Game Scope
Rock can crush scissors
Paper can wrap rock
Scissors can cut paper'''
import random
while True:
    options = ['rock', 'paper', 'sissors']
    computers_pick = random.choice(options)
    players_pick = input('select one (rock, paper or scissors): ')
    print(f'\nYou picked {players_pick}, computer picked {computers_pick} .\n')

    if players_pick == computers_pick:
        print(f'Both players selected {players_pick}. Its a tie!')
    elif players_pick == 'rock':
        if computers_pick == 'scissor':
            print('Rock crushes scissors! You win!')
        else:
            print('Paper covers rock! You lose!')
    elif players_pick == 'paper':
        if computers_pick == 'rock':
            print('Paper covers rock! You win!')
        else:
            print('Scissors cuts paper! You lose!')
    elif players_pick == 'scissors':
        if computers_pick == 'paper':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose!')

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break