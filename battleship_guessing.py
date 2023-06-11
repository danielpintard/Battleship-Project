import numpy as np 
import random
from battleship_player import player_board, board_dict, initialize_player, print_board
from battleship_cpuopp import cpu_board, initialize_cpu

guess_board = np.zeros((10,10), dtype=int)

game_over = False
player_points = 0
cpu_points = 0

#need to add smart fetaure to this 
# def cpu_guessing():
#     print('\n_________________________________________________________________________________________________________________________')
#     print("\nIt is the enemy's turn to guess\n")
#     global cpu_points
    
#     #initialize hit_pos to keep track of the hit position
#     hit_pos = None
    
#     #randomly generate guesses
#     cpu_guess = (random.randint(0,9), random.randint(0,9))
    
#     key = next((k for k, v in board_dict.items() if v == cpu_guess), None)

#     if player_board[cpu_guess] == 0:
#         player_board[cpu_guess] = 2
#         print('Enemy missed at', key)
#         print('Enemy points: ', cpu_points)
#     #if it hits a part of a ship 
#     elif player_board[cpu_guess] == 1:
#         player_board[cpu_guess] = 3
#         hit_pos = cpu_guess
#         cpu_points += 1
#         print('Enemy hit at', key)
#         print('Enemy points: ', cpu_points)
            
#     print('\nYour Board')    
#     print_board(player_board)

def cpu_guessing():
    print('\n_________________________________________________________________________________________________________________________')
    print("\nIt is the enemy's turn to guess\n")
    global cpu_points
    
    hit_pos = None     
    
    while True:
        if hit_pos is None:
            cpu_guess = (random.randint(0,9), random.randint(0,9))
        else:
            adj_pos = [((hit_pos[0] - 1), hit_pos[1]), ((hit_pos[0] + 1), hit_pos[1]), (hit_pos[0], (hit_pos[1] - 1)), (hit_pos[0], (hit_pos[1] + 1))]
            random.shuffle(adj_pos)
            cpu_guess = adj_pos[0]
        
        key = next((k for k, v in board_dict.items() if v == cpu_guess), None)
        
        if player_board[cpu_guess] == 1:
            hit_pos = cpu_guess
            player_board[cpu_guess] = 3
            cpu_points += 1
            print('Enemy hit at', key)
            print('Enemy points: ', cpu_points)
            adj_pos = [((hit_pos[0] - 1), hit_pos[1]), ((hit_pos[0] + 1), hit_pos[1]), (hit_pos[0], (hit_pos[1] - 1)), (hit_pos[0], (hit_pos[1] + 1))]
            if all(player_board[pos[0], pos[1]] != 1 for pos in adj_pos):
                hit_pos = None
        elif player_board[cpu_guess] == 0:
            player_board[cpu_guess] = 2
            print('Enemy missed at', key)
            print('Enemy points: ', cpu_points)
            break
            
    print('\nYour board:\n')
    print_board(player_board)       
        
          
def validate_guess(guess):
    for k,v in board_dict.items():
        if guess.upper() == k:
            guess_coord = v
            if guess_board[guess_coord] == 3 or guess_board[guess_coord] == 2:
                raise ValueError(print('\nINVALID GUESS - You have already guessed at this coordinate. Please  enter a new coordinate.\n'))
            else:
                pass
        

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
        
    
    print('\nGuess Board:\n')    
    print_board(guess_board)
        
    
#this works as it should 
def initialize_guessing():
    global game_over
    print('\nGuess Board:\n')
    print_board(guess_board) 
    player_turn = True
    
    while game_over == False:
        if player_turn == True:
            player_guessing()
        else:
            cpu_guessing()
        
        player_turn = not player_turn
       
        # end game logic
        if cpu_points == 17:
            game_over = True
            print('\nYou have lost the war')
        elif player_points == 17:
            game_over = True
            print('\nCongratulations General, you have won the war!')
        
        if game_over == True:
            break 

