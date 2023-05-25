from battleship_cpuopp import cpu_board 
from battleship_player import player_board, board_dict
import random

def validate_guess(guess):
    if guess.upper() not in board_dict.keys():
        raise ValueError(print('INVALID GUESS - The coordinate you guessed was invalid. Remember - the coordinates of this board are indicated by letters A-J on the vertical axis and number 1-10 on the horizontal axis.'))
    else:
        pass
    
    for k,v in board_dict.items():
        if guess.upper() == k:
            if cpu_board[v] == 1:
                return True
            else: 
                raise ValueError(print('INCORRECT GUESS - There was no parts of a ship in that coordinate'))

def cpu_guess(): 
    x = random.randint(0,9)
    y = random.randint(0,9)
    guess = (x, y)
    
    
    
    
def initialize_integration():
    while True:
        try:
            guess = input('\nAt which coordinate do you think a ship may be placed?:\n')
            validate_guess(guess)
            if validate_guess(guess) == True:
                print('this while loop is working')
            break
        except ValueError:
            continue 
        