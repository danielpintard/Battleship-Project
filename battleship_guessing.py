import numpy as np 
import random
from battleship_player import player_board, board_dict, initialize_player, print_board
from battleship_cpuopp import cpu_board, initialize_cpu

guess_board = np.zeros((10,10), dtype=int)

game_over = False

def cpu_guessing():
    cpu_points = 0
    x = random.randint(0,9)
    y = random.randint(0,9)
    #cpu_guess = (y, x)
    cpu_guess = (0,0)

    if player_board[cpu_guess] == 1:
        player_board[cpu_guess] = 3
        cpu_points += 1
        print('enemy score: ', cpu_points) 
    elif player_board[cpu_guess] == 0: 
        player_board[cpu_guess] = 2
        print('Enemy has failed to target a part of any of your ships')
        
    print_board(player_board)
       
def validate_guess(guess):
    if guess.upper() in board_dict.keys():
        return guess
    else:
        raise ValueError(print('INVALID INPUT - Remember the coordinates are indicated by letters A-J on the vertical axis and numbers 1-10 on the horizontal axis.'))


def player_guessing():
    player_points = 0
    while True:
        try:
            player_guess = input('Enter your guess as to where a part of any of your enemy ships is located: ')
            validate_guess(player_guess)
            break
        except ValueError:
            continue 
        
    for k,v in board_dict.items():
        if player_guess.upper() == k:
            guess_coord = v
            player_points += 1
            print('Your points: ', player_points)
    if cpu_board[guess_coord] == 1:
        guess_board[guess_coord] = 3
    else:
        guess_board[guess_coord] = 2
    
    
    
    
    

def initialize_guessing():
    while game_over == False:
        player_guessing()
        cpu_guessing()
        
        # #end game logic
        # if cpu_points == 17:
        #     game_over == True
        # elif player_points == 17:
        #     game_over == True
            
        # if game_over == True:
        #     break 
        
        
