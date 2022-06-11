'''Logan Hitchcock, Tic Tac Toe'''

def main():
    player = players_turn('')
    square_number = size_of_gameboard()
    show_game(square_number)
    player = players_turn(player)
    player_move(player, square_number)
    show_game(square_number)

def size_of_gameboard():
    square_number = []
    for i in range(9):
        square_number.append(i + 1)
    return square_number

def show_game(square_number):
    print(f"{square_number[0]}|{square_number[1]}|{square_number[2]}")
    print("-----")
    print(f"{square_number[3]}|{square_number[4]}|{square_number[5]}")
    print("-----")
    print(f"{square_number[6]}|{square_number[7]}|{square_number[8]}")


def players_turn(player):
    if player == '' or 'x':
        return 'o'
    elif player == 'o':
        return 'x'


    '''if one player just placed their symbol, move to next player'''


def player_move(player, square_number):
    if player == 'x':
        player_move = input(f'{player} please choose a slot (1-9).')
        square_number[player_move - 1] = player
        



def update_board():
    '''what players turn it is, add their symbol to selected box'''
    pass



def declare_winner():
    '''if there is 3 in a row, return true'''


main()
