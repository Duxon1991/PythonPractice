from random import randint
import sys,os
os.system("cls")

t = ['rock','paper','scissors']

computer = t[randint(0,2)]

player = False

while(player == False):
    player = input('Rock,Paper,Scissors?')

    if(player == computer):
        print('Tie!')
    elif(player == 'rock'):
        if(computer == 'paper'):
            print('Player',player,'Computer',computer,)
            print('You Lose!')
        elif(computer == 'scissors'):
            print('Player',player,'Computer',computer,)
            print('You Win!')
    elif(player == 'paper'):
        if(computer == 'rock'):
            print('Player',player,'Computer',computer,)
            print('You Lose!')
        elif(computer == 'scissors'):
            print('Player',player,'Computer',computer,)
            print('You Win!')
    elif(player == 'scissors'):
        if(computer == 'rock'):
            print('Player',player,'Computer',computer,)
            print('You Lose!')
        elif(computer == 'paper'):
            print('Player',player,'Computer',computer,)
            print('You Win!')
    elif(player == 'exit'):
        print('Exit')
        break
    else:
        print('Player gave invalid input:',player)

    player = False
    computer = t[randint(0,2)]
    print()
    wait = input('Press Enter to continue')
    os.system("cls") 
    