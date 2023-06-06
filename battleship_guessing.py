import numpy as np 
import random
from battleship_player import player_board, board_dict, initialize_player, print_board
from battleship_cpuopp import cpu_board, initialize_cpu

guess_board = np.zeros((10,10), dtype=int)

game_over = False
player_points = 0
cpu_points = 0

## OG cpu_guessing()
# def cpu_guessing():
#     print('\n_________________________________________________________________________________________________________________________')
#     print("\nIt is the enemy's turn to guess\n")
#     global cpu_points
    
#     hit_pos = None
#     cpu_guess = (random.randint(0,9), random.randint(0,9))
#     adj_pos = [((cpu_guess[0] - 1), cpu_guess[1]), 
#                ((cpu_guess[0] + 1),cpu_guess[1]), 
#                (cpu_guess[0],(cpu_guess[1] - 1)), 
#                (cpu_guess[0],(cpu_guess[1] + 1))]
#     # guesses = []
#     # guesses.append(cpu_guess)
#     # print(guesses)
    
#     key = next((k for k, v in board_dict.items() if v == cpu_guess), None)

    

#     if player_board[cpu_guess] == 0:
#         player_board[cpu_guess] = 2
#         print('Enemy missed at', key)
#         print('Enemy points: ', cpu_points)
#     elif player_board[cpu_guess] == 1:
#         player_board[cpu_guess] = 3
#         cpu_points += 1
#         print('Enemy missed at', key)
#         print('Enemy points: ', cpu_points)
            
#     print('\nYour Board')    
#     print_board(player_board)

def cpu_guessing():
    print('\n_________________________________________________________________________________________________________________________')
    print("\nIt is the enemy's turn to guess\n")
    global cpu_points

    hit_pos = None
    hit_ship = False

    while not hit_ship:
        adj_pos = []
        if hit_pos is None:
            # Randomly select a position for initial guess
            cpu_guess = (random.randint(0, 9), random.randint(0, 9))
        else:
            # Guess adjacent positions of the previously hit position
            adj_pos = [((hit_pos[0] - 1), hit_pos[1]),
                       ((hit_pos[0] + 1), hit_pos[1]),
                       (hit_pos[0], (hit_pos[1] - 1)),
                       (hit_pos[0], (hit_pos[1] + 1))]
            cpu_guess = random.choice(adj_pos)

        key = next((k for k, v in board_dict.items() if v == cpu_guess), None)

        if player_board[cpu_guess] == 0:
            player_board[cpu_guess] = 2
            print('Enemy missed at', key)
            print('Enemy points: ', cpu_points)
            hit_ship = False  # Continue guessing
        elif player_board[cpu_guess] == 1:
            player_board[cpu_guess] = 3
            cpu_points += 1
            print('Enemy missed at', key)
            print('Enemy points: ', cpu_points)
            hit_pos = cpu_guess  # Remember the hit position
            hit_ship = all(player_board[pos] != 1 for pos in adj_pos)  # Check if ship is destroyed

        print('\nYour Board')
        print_board(player_board)

          
def validate_guess(guess):
    if guess.upper() in board_dict.keys():
        return guess
    else:
        raise ValueError(print('\nINVALID INPUT - Remember the coordinates are indicated by letters A-J on the vertical axis and numbers 1-10 on the horizontal axis.\n'))


def player_guessing():
    global player_points
    while True:
        try:
            player_guess = input('\nEnter your guess as to where a part of any of your enemy ships is located: ')
            validate_guess(player_guess)
            break
        except ValueError:
            continue 
        
    for k,v in board_dict.items():
        if player_guess.upper() == k:
            guess_coord = v
    
    if cpu_board[guess_coord] == 1:
        guess_board[guess_coord] = 3
        player_points += 1
        print('\nYou have hit a part of a ship at', player_guess.upper())
        print('Your points: ', player_points)
    else:
        guess_board[guess_coord] = 2
        print('\nThere was no part of a ship at', player_guess.upper())
        print('Your points: ', player_points)
        
    
    print('\nGuess Board')    
    print_board(guess_board)
    
    
    
    
    

def initialize_guessing():
    global game_over
    while game_over == False:
        cpu_guessing()
        player_guessing()
       
        # end game logic
        if cpu_points == 17:
            game_over = True
            print('\nYou have lost the war')
        elif player_points == 17:
            game_over = True
            print('\nCongratulations General, you have won the war!')
        
        if game_over == True:
            break 

