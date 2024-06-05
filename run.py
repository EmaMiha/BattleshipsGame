import random

def print_board(board):
    """ 
    Creating the board.
    Prints the board in a readable format.
    """
    for row in board: 
        print(" ".join(row))

def create_board(board):
    """
    Creates a size x size board filled with "O", which represent the sea.
    """
    board = [["O"] * size for _ in range(size)]
    return board

def set_ship(board, size):
    """
    Randomly places a single ship "S" on the board and returns its cordinates.
    """
    ship_row = random.randint(0, size -1)
    ship_col = random.randint(0, size -1)
    return (ship_row, ship_col)

def make_guess ():
    """
    Prompts the player to input their guess for the row and column.
    """
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    return(guess_row, guess_col)

    