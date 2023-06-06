import random 
import numpy as np 
from battleship_player import board_dict, print_board

cpu_board = np.zeros((10,10), dtype = int)


def cpu_check4space(coord_ledger):
    for i in coord_ledger:
        if cpu_board[i] == 1:
            raise ValueError('INVALID COORDINATE AND/OR DIRECTION - The coordinate and/or direction chosen is invalid. Either the input was invalid or there is no more space in this direction.')
        else:
            continue  

def ac_randomizer():
    print('\nEnemy deploying aircraft carrier')
    
    def ac_board_fill():
        for i in coord_ledger:
            for j in board_dict.values():
                if i not in board_dict.values():
                    raise ValueError('non-valid coordinates')
                else:
                    continue
            

    def ac_ledger_fill(coord, direction, coord_ledger):
        if direction == 'up':
            for i in range(0,4):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x - 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'down':
            for i in range(0,4):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x + 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'left':
            for i in range(0,4):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y - 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'right':
            for i in range(0,4):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y + 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)

    
    while True:
        try:    
            directions = ['left', 'right', 'up', 'down']
            coord_ledger = []
            x = random.randint(0,9)
            y = random.randint(0,9)
            strt_coord = (x, y)
            # print(strt_coord)
            coord_ledger.append(strt_coord)
            direction = random.choice(directions)
            # print(direction)
            ac_ledger_fill(strt_coord, direction, coord_ledger)
            ac_board_fill()
            cpu_check4space(coord_ledger)
            break
        except ValueError:
            continue 
            
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == v:
                cpu_board[v] = 1
                
    
def bs_randomizer():
    print('\nEnemy deploying battleship')
    
    def bs_board_fill():
        for i in coord_ledger:
            for j in board_dict.values():
                if i not in board_dict.values():
                    raise ValueError('non-valid coordinates')
                else:
                    continue
            

    def bs_ledger_fill(coord, direction, coord_ledger):
        if direction == 'up':
            for i in range(0,3):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x - 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'down':
            for i in range(0,3):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x + 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'left':
            for i in range(0,3):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y - 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'right':
            for i in range(0,3):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y + 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)

    
    while True:
        try:    
            directions = ['left', 'right', 'up', 'down']
            coord_ledger = []
            x = random.randint(0,9)
            y = random.randint(0,9)
            strt_coord = (x, y)
            # print(strt_coord)
            coord_ledger.append(strt_coord)
            direction = random.choice(directions)
            # print(direction)
            bs_ledger_fill(strt_coord, direction, coord_ledger)
            bs_board_fill()
            cpu_check4space(coord_ledger)
            break
        except ValueError:
            continue 
            
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == v:
                cpu_board[v] = 1
                
    

def cr_randomizer():
    print('\nEnemy deploying cruiser')
    
    def cr_board_fill():
        for i in coord_ledger:
            for j in board_dict.values():
                if i not in board_dict.values():
                    raise ValueError('non-valid coordinates')
                else:
                    continue
            

    def cr_ledger_fill(coord, direction, coord_ledger):
        if direction == 'up':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x - 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'down':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x + 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'left':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y - 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'right':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y + 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)

    
    while True:
        try:    
            directions = ['left', 'right', 'up', 'down']
            coord_ledger = []
            x = random.randint(0,9)
            y = random.randint(0,9)
            strt_coord = (x, y)
            # print(strt_coord)
            coord_ledger.append(strt_coord)
            direction = random.choice(directions)
            # print(direction)
            cr_ledger_fill(strt_coord, direction, coord_ledger)
            cr_board_fill()
            cpu_check4space(coord_ledger)
            break
        except ValueError:
            continue 
            
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == v:
                cpu_board[v] = 1
                

def sb_randomizer():
    print('\nEnemy deploying submarine')   
    
    def sb_board_fill():
        for i in coord_ledger:
            for j in board_dict.values():
                if i not in board_dict.values():
                    raise ValueError('non-valid coordinates')
                else:
                    continue
            

    def sb_ledger_fill(coord, direction, coord_ledger):
        if direction == 'up':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x - 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'down':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x + 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'left':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y - 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'right':
            for i in range(0,2):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y + 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)

    
    while True:
        try:    
            directions = ['left', 'right', 'up', 'down']
            coord_ledger = []
            x = random.randint(0,9)
            y = random.randint(0,9)
            strt_coord = (x, y)
            # print(strt_coord)
            coord_ledger.append(strt_coord)
            direction = random.choice(directions)
            # print(direction)
            sb_ledger_fill(strt_coord, direction, coord_ledger)
            sb_board_fill()
            cpu_check4space(coord_ledger)
            break
        except ValueError:
            continue 
            
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == v:
                cpu_board[v] = 1
                
   
def ds_randomizer():
    print('\nEnemy deploying destroyer')
    
    def ds_board_fill():
        for i in coord_ledger:
            for j in board_dict.values():
                if i not in board_dict.values():
                    raise ValueError('non-valid coordinates')
                else:
                    continue
            

    def ds_ledger_fill(coord, direction, coord_ledger):
        if direction == 'up':
            for i in range(0,1):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x - 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'down':
            for i in range(0,1):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x + 1, y)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
        if direction == 'left':
            for i in range(0,1):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y - 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)
                    break
        if direction == 'right':
            for i in range(0,1):
                    x = coord_ledger[-1][0]
                    y = coord_ledger[-1][1]
                    mut_coord =  (x, y + 1)
                    coord_ledger.append(mut_coord)     
                    # print(coord_ledger)

    
    while True:
        try:    
            directions = ['left', 'right', 'up', 'down']
            coord_ledger = []
            x = random.randint(0,9)
            y = random.randint(0,9)
            strt_coord = (x, y)
            # print(strt_coord)
            coord_ledger.append(strt_coord)
            direction = random.choice(directions)
            # print(direction)
            ds_ledger_fill(strt_coord, direction, coord_ledger)
            ds_board_fill()
            cpu_check4space(coord_ledger)
            break
        except ValueError:
            continue 
            
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == v:
                cpu_board[v] = 1
                

def initialize_cpu():
    ac_randomizer()
    # bs_randomizer()
    # cr_randomizer()
    # sb_randomizer()
    # ds_randomizer()
    
    print('\nEnemy Deployment Complete')
    
    print('\nenemy board: ')
    print_board(cpu_board)
    print('\n')


