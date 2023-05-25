import random 
import numpy as np 
from battleship_player import board_dict 

cpu_board = np.zeros((10,10), dtype = int)

# board_dict = {'A1': (0, 0), 'A2': (0, 1), 'A3': (0, 2), 'A4': (0, 3), 'A5': (0, 4), 'A6': (0, 5), 'A7': (0, 6), 'A8': (0, 7), 'A9': (0, 8), 'A10': (0, 9), 
#               'B1': (1, 0), 'B2': (1, 1), 'B3': (1, 2), 'B4': (1, 3), 'B5': (1, 4), 'B6': (1, 5), 'B7': (1, 6), 'B8': (1, 7), 'B9': (1, 8), 'B10': (1, 9),
#               'C1': (2, 0), 'C2': (2, 1), 'C3': (2, 2), 'C4': (2, 3), 'C5': (2, 4), 'C6': (2, 5), 'C7': (2, 6), 'C8': (2, 7), 'C9': (2, 8), 'C10': (2, 9),
#               'D1': (3, 0), 'D2': (3, 1), 'D3': (3, 2), 'D4': (3, 3), 'D5': (3, 4), 'D6': (3, 5), 'D7': (3, 6), 'D8': (3, 7), 'D9': (3, 8), 'D10': (3, 9), 
#               'E1': (4, 0), 'E2': (4, 1), 'E3': (4, 2), 'E4': (4, 3), 'E5': (4, 4), 'E6': (4, 5), 'E7': (4, 6), 'E8': (4, 7), 'E9': (4, 8), 'E10': (4, 9), 
#               'F1': (5, 0), 'F2': (5, 1), 'F3': (5, 2), 'F4': (5, 3), 'F5': (5, 4), 'F6': (5, 5), 'F7': (5, 6), 'F8': (5, 7), 'F9': (5, 8), 'F10': (5, 9), 
#               'G1': (6, 0), 'G2': (6, 1), 'G3': (6, 2), 'G4': (6, 3), 'G5': (6, 4), 'G6': (6, 5), 'G7': (6, 6), 'G8': (6, 7), 'G9': (6, 8), 'G10': (6, 9), 
#               'H1': (7, 0), 'H2': (7, 1), 'H3': (7, 2), 'H4': (7, 3), 'H5': (7, 4), 'H6': (7, 5), 'H7': (7, 6), 'H8': (7, 7), 'H9': (7, 8), 'H10': (7, 9), 
#               'I1': (8, 0), 'I2': (8, 1), 'I3': (8, 2), 'I4': (8, 3), 'I5': (8, 4), 'I6': (8, 5), 'I7': (8, 6), 'I8': (8, 7), 'I9': (8, 8), 'I10': (8, 9), 
#               'J1': (9, 0), 'J2': (9, 1), 'J3': (9, 2), 'J4': (9, 3), 'J5': (9, 4), 'J6': (9, 5), 'J7': (9, 6), 'J8': (9, 7), 'J9': (9, 8), 'J10': (9, 9)}

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
    bs_randomizer()
    cr_randomizer()
    sb_randomizer()
    ds_randomizer()
    
    print('\nEnemy Deployment Complete')
    
    vertical_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    horizontal_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    print('  ' + ' '.join(horizontal_labels))  # Print horizontal axis labels
    for i, row in enumerate(cpu_board):
     print(vertical_labels[i] + ' ' + ' '.join(str(element) for element in row))


