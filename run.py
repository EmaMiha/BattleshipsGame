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

