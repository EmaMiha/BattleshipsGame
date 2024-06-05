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
