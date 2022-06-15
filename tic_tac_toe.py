'''Logan Hitchcock, Tic Tac Toe'''

def main():
    player = players_turn('')
    square_number = make_gamesquare_number
    square_number = make_gamesquare_number()
    winner = declare_winner(square_number)
    while winner == False:
        show_game(square_number)
        player_move(player, square_number)
        player = players_turn(player)

    show_game(square_number)

def make_gamesquare_number():
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
    else:
        player == 'o'
        player_move = int(input(f'{player} please choose a slot (1-9).'))
        square_number[player_move - 1] = player   
    
def declare_winner(square_number):
    '''if there is 3 in a row, return true'''
    if(square_number[0] == square_number[1] == square_number[2] or
        square_number[3] == square_number[4] == square_number[5] or
        square_number[6] == square_number[7] == square_number[8] or
        square_number[0] == square_number[3] == square_number[6] or
        square_number[1] == square_number[4] == square_number[7] or
        square_number[2] == square_number[5] == square_number[8] or
        square_number[0] == square_number[4] == square_number[8] or
        square_number[2] == square_number[4] == square_number[6]):
        winner = True
    else:
        winner = False

    return winner



main()

