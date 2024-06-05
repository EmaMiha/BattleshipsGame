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

def check_guess(board, guess_row, guess_col, ship_row, ship_col):
    """
    Checks if the guess is correct, already guessed, or out of bounds and 
    updates the board.
    """
    if guess_row == ship_row and guess_col == ship_col:
        print("You sunk my ship, congratulations!")
        return True

    else:
        if guess_row not in range (len(board)) or guess_col not in range(len(board)):
             print("You even missed the sea!") 
        elif board [guess_row] [guess_col] == "X":
            print("You already guessed that one.") 
        else:
            print("You missed my ship!")
            board [guess_row] [guess_col]  = "X" 
        return False     

def play_game():
    """
    Manages the game, allows the player up to 4 turns to guess the ship's location 
    and provides feedback.
    """   
    board_size = 5
    board = create_board(board_size)
    ship_row,ship_col = set_ship(board, board_size)
    print("Let's having a battleships fun!")
    print_board(board)

    for turn in range(4):
        print(f"Turn{Turn + 1}")   
        guess_row, guess_col = make_guess()
        if check_guess(board, guess_row, guess_col, ship_row, ship_col):
            break