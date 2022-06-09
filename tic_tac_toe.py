'''Logan Hitchcock, Tic Tac Toe'''

def main():
    square_number = number_of_squares()
    show_game(square_number)


def number_of_squares():
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


def players_turn():
    '''if one player just placed their symbol, move to next player'''
    pass 


def update_board():
    '''what platers turn it is, add their symbol to selected box'''
    pass



def declare_winner():
    '''if there is 3 in a row, return true'''


main()
