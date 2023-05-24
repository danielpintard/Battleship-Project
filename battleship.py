import numpy as np 

# #creating the player board
# matrix = np.zeros((10,10), dtype = str)
# letters = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# numbers = np.arange(1,11)
# #got this line of code from ChatGPT - it replaces all of the zeros from the original matrix with the coordinates of the battleship board
# player_board = np.core.defchararray.add(np.expand_dims(letters, axis=1), np.char.mod('%d', numbers))  

player_board = np.zeros((10,10), dtype=int)
vertical_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
horizontal_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Print the matrix with coordinate labels
print('  ' + ' '.join(horizontal_labels))  # Print horizontal axis labels
for i, row in enumerate(player_board):
    print(vertical_labels[i] + ' ' + ' '.join(str(element) for element in row))

# grid_dict = {}
# for letter in 'ABCDEFGHIJ':
#     for number in range(1, 11):
#         key = letter + str(number)
#         value = (ord(letter) - ord('A'), number - 1)
#         grid_dict[key] = value

board_dict = {'A1': (0, 0), 'A2': (0, 1), 'A3': (0, 2), 'A4': (0, 3), 'A5': (0, 4), 'A6': (0, 5), 'A7': (0, 6), 'A8': (0, 7), 'A9': (0, 8), 'A10': (0, 9), 
              'B1': (1, 0), 'B2': (1, 1), 'B3': (1, 2), 'B4': (1, 3), 'B5': (1, 4), 'B6': (1, 5), 'B7': (1, 6), 'B8': (1, 7), 'B9': (1, 8), 'B10': (1, 9),
              'C1': (2, 0), 'C2': (2, 1), 'C3': (2, 2), 'C4': (2, 3), 'C5': (2, 4), 'C6': (2, 5), 'C7': (2, 6), 'C8': (2, 7), 'C9': (2, 8), 'C10': (2, 9),
              'D1': (3, 0), 'D2': (3, 1), 'D3': (3, 2), 'D4': (3, 3), 'D5': (3, 4), 'D6': (3, 5), 'D7': (3, 6), 'D8': (3, 7), 'D9': (3, 8), 'D10': (3, 9), 
              'E1': (4, 0), 'E2': (4, 1), 'E3': (4, 2), 'E4': (4, 3), 'E5': (4, 4), 'E6': (4, 5), 'E7': (4, 6), 'E8': (4, 7), 'E9': (4, 8), 'E10': (4, 9), 
              'F1': (5, 0), 'F2': (5, 1), 'F3': (5, 2), 'F4': (5, 3), 'F5': (5, 4), 'F6': (5, 5), 'F7': (5, 6), 'F8': (5, 7), 'F9': (5, 8), 'F10': (5, 9), 
              'G1': (6, 0), 'G2': (6, 1), 'G3': (6, 2), 'G4': (6, 3), 'G5': (6, 4), 'G6': (6, 5), 'G7': (6, 6), 'G8': (6, 7), 'G9': (6, 8), 'G10': (6, 9), 
              'H1': (7, 0), 'H2': (7, 1), 'H3': (7, 2), 'H4': (7, 3), 'H5': (7, 4), 'H6': (7, 5), 'H7': (7, 6), 'H8': (7, 7), 'H9': (7, 8), 'H10': (7, 9), 
              'I1': (8, 0), 'I2': (8, 1), 'I3': (8, 2), 'I4': (8, 3), 'I5': (8, 4), 'I6': (8, 5), 'I7': (8, 6), 'I8': (8, 7), 'I9': (8, 8), 'I10': (8, 9), 
              'J1': (9, 0), 'J2': (9, 1), 'J3': (9, 2), 'J4': (9, 3), 'J5': (9, 4), 'J6': (9, 5), 'J7': (9, 6), 'J8': (9, 7), 'J9': (9, 8), 'J10': (9, 9)}


def validate_coord_ledger(coord_ledger):
    for i in coord_ledger:
        for j in board_dict.keys():
            if i not in board_dict.keys():
                raise ValueError(print('validate_coord_ledger: INVALID COORDINATE AND/OR DIRECTION - The coordinate and/or direction chosen is invalid. Either the input was invalid or there is no more space in this direction.'))
            else:
                pass

def aircraft_carrier():
    print('\nPreparing to deploy the aircraft carrier (5-units long) - ■ ■ ■ ■ ■')
    
    def ac_move(coord, direc, coord_ledger):
        if direc.lower() == 'left':    
            for i in range(0,4):
                letter = coord_ledger[-1][0]
                number = coord_ledger[-1][1:]
                mut_coord =  letter + str(int(number) - 1)
                coord_ledger.append(mut_coord)    
        elif direc.lower() == 'right':
            for i in range(0,4):
                letter = coord_ledger[-1][0]
                number = coord_ledger[-1][1:]
                mut_coord =  letter + str(int(number) + 1)
                coord_ledger.append(mut_coord)    
        elif direc.lower() == 'up':
            for i in range(0,4):
                    letter = coord_ledger[-1][0]
                    number = coord_ledger[-1][1:]
                    mut_coord =  chr(ord(letter) - 1) + number
                    coord_ledger.append(mut_coord)     
        elif direc.lower() == 'down':
            for i in range(0,4):
                    letter = coord_ledger[-1][0]
                    number = coord_ledger[-1][1:]
                    mut_coord =  chr(ord(letter) + 1) + number
                    coord_ledger.append(mut_coord)    
        else:
            raise ValueError(print('ac_move: INVALID COORDINATE AND/OR DIRECTION - The coordinate and/or direction chosen is invalid. Either the input was invalid or there is no more space in this direction.'))
        
        print(coord_ledger)
    
    while True:
        try:
            coord = input('At which coordinate would you like to begin placing the aircraft carrier: ')
            direction = input('In which direction would you like to place the aircraft carrier in relation to the starting coordinate: ')
            coord_ledger = []
            coord_ledger.append(coord.upper())
            ac_move(coord, direction, coord_ledger)
            validate_coord_ledger(coord_ledger)
            break
        except ValueError:
            continue 
        
    for i in coord_ledger:
        for k,v in board_dict.items():
            if i == k:
                player_board[v] = 1
    
    vertical_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    horizontal_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # Print the matrix with coordinate labels
    print('  ' + ' '.join(horizontal_labels))  # Print horizontal axis labels
    for i, row in enumerate(player_board):
        print(vertical_labels[i] + ' ' + ' '.join(str(element) for element in row))

def battleship():
    pass

def cruiser():
    pass

def submarine():
    pass

def destroyer():
    pass

def initialize_game():
    #**NOTE** Add an Introduction to game and explanation of rules here
    
    #Initial Prompting
    while True:
        try:
            ship = input('\nWhich ship would you like to place down first?\nEnter "1" for the aircraft carrier (this ship takes up 5 units on the board)\nEnter "2" for the battleship (this ship takes up 4 units on the board)\nEnter "3" for the cruiser (this ship takes up 3 units on the board)\nEnter "4" for the submarine (this ship takes up 3 units on the board)\nEnter "5" for the destroyer (this ship takes up 2 units on the board)\nType the number and Press Enter/Return: ')
            if ship not in ['1', '2', '3', '4', '5']:
                raise ValueError(print('\nINVALID INPUT - Please enter "1", "2", "3", "4" or "5" to determine which ship is placed first' ))
            break
        except ValueError:
            continue
        
    if ship == '1':
        aircraft_carrier()
    elif ship == '2':
        battleship()
    elif ship == '3':
        cruiser()
    elif ship == '4':
        submarine()
    elif ship == '5':
        destroyer()
    
    while True:
        try:
            ship2 = input('\nWhich ship would you like to place down second?\nEnter "1" for the aircraft carrier (this ship takes up 5 units on the board)\nEnter "2" for the battleship (this ship takes up 4 units on the board)\nEnter "3" for the cruiser (this ship takes up 3 units on the board)\nEnter "4" for the submarine (this ship takes up 3 units on the board)\nEnter "5" for the destroyer (this ship takes up 2 units on the board)\nType the number and Press Enter/Return: ')
            if ship2 not in ['1', '2', '3', '4', '5'] or ship2 == ship:
                raise ValueError(print('\nINVALID INPUT - That ship may have already been placed or the input was invalid. Please enter "1", "2", "3", "4" or "5" to determine which ship is placed next' ))
            break
        except ValueError:
            continue
        
    if ship2 == '1':
        aircraft_carrier()
    elif ship2 == '2':
        battleship()
    elif ship2 == '3':
        cruiser()
    elif ship2 == '4':
        submarine()
    elif ship2 == '5':
        destroyer()

     
    while True:
        try:
            ship3 = input('\nWhich ship would you like to place down third?\nEnter "1" for the aircraft carrier (this ship takes up 5 units on the board)\nEnter "2" for the battleship (this ship takes up 4 units on the board)\nEnter "3" for the cruiser (this ship takes up 3 units on the board)\nEnter "4" for the submarine (this ship takes up 3 units on the board)\nEnter "5" for the destroyer (this ship takes up 2 units on the board)\nType the number and Press Enter/Return: ')
            if ship3 not in ['1', '2', '3', '4', '5'] or ship3 == ship or ship3 == ship2:
                raise ValueError(print('\nINVALID INPUT - That ship may have already been placed or the input was invalid. Please enter "1", "2", "3", "4" or "5" to determine which ship is placed next' ))
            break
        except ValueError:
            continue
     
                
    if ship3 == '1':
        aircraft_carrier()
    elif ship3 == '2':
        battleship()
    elif ship3 == '3':
        cruiser()
    elif ship3 == '4':
        submarine()
    elif ship3 == '5':
        destroyer()
    
    while True:
        try:
            ship4 = input('\nWhich ship would you like to place down fourth?\nEnter "1" for the aircraft carrier (this ship takes up 5 units on the board)\nEnter "2" for the battleship (this ship takes up 4 units on the board)\nEnter "3" for the cruiser (this ship takes up 3 units on the board)\nEnter "4" for the submarine (this ship takes up 3 units on the board)\nEnter "5" for the destroyer (this ship takes up 2 units on the board)\nType the number and Press Enter/Return: ')
            if ship4 not in ['1', '2', '3', '4', '5'] or ship4 == ship or ship4 == ship2 or ship4 == ship3:
                raise ValueError(print('\nINVALID INPUT - That ship may have already been placed or the input was invalid. Please enter "1", "2", "3", "4" or "5" to determine which ship is placed next' ))
            break
        except ValueError:
            continue
     
                
    if ship4 == '1':
        aircraft_carrier()
    elif ship4 == '2':
        battleship()
    elif ship4 == '3':
        cruiser()
    elif ship4 == '4':
        submarine()
    elif ship4 == '5':
        destroyer()

    while True:
        try:
            ship5 = input('\nWhich ship would you like to place down third?\nEnter "1" for the aircraft carrier (this ship takes up 5 units on the board)\nEnter "2" for the battleship (this ship takes up 4 units on the board)\nEnter "3" for the cruiser (this ship takes up 3 units on the board)\nEnter "4" for the submarine (this ship takes up 3 units on the board)\nEnter "5" for the destroyer (this ship takes up 2 units on the board)\nType the number and Press Enter/Return: ')
            if ship5 not in ['1', '2', '3', '4', '5'] or ship5 == ship or ship5 == ship2 or ship5 == ship3 or ship5 == ship4:
                raise ValueError(print('\nINVALID INPUT - That ship may have already been placed or the input was invalid. Please enter "1", "2", "3", "4" or "5" to determine which ship is placed next' ))
            break
        except ValueError:
            continue
     
                
    if ship5 == '1':
        aircraft_carrier()
    elif ship5 == '2':
        battleship()
    elif ship5 == '3':
        cruiser()
    elif ship5 == '4':
        submarine()
    elif ship5 == '5':
        destroyer()





initialize_game()

#As of May 23rd 2023 8:00 PM - So I cleaned up the project immensely, quite literally overhauling all of the code so that less functions were being used and 
#so that any existing functions were either more multifaceted/covered more functionality in fewer lines of code. 
#Essentially, the aircraft_carier function is complete, so I would eseentially just have to copy, paste and tweak for each of the 
#other functions. The only other thing I need to account for is when placing down ships on the board, particular positions need to logged/memorized in some way as to raise an error if I try to place a ship somewhere and there is another ship already there that is c
#taking up space



