from random import randint
from pprint import pprint

# https://www.asciiart.eu/vehicles/navy - ascii battleship
#https://patorjk.com/software/taag/#p=display&v=0&f=Slant&t=Battleships - ascii title

INTRO = """

             ____        __  __  __          __    _           
            / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___  _____
           / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __ \/ ___/
          / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ (__  ) 
         /_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/____/  
                                                /_/    
                                       
                                               
                                        |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/  _
 __..._____--==/___]_|__|_____________________________[___\==--___,-----' 7
|                                                                   BB-61/
 \_______________________________________________________________________|


Welcome to Battleships, the naval strategy game!

        """
class Player:
    """
    Player class. Stores the username and score for each Player object.
    Has a methods for incrementing the Player's score.
    """

    def __init__(self, username, score):
        self.username = username
        self.score = score

    def increment_score(self):
        """
        Increments the Player's score by 1.
        """
        self.score += 1

def new_game():
    """
    Runs at the beggining of every new game. 
    Prints the title, ascii battleship
    art and gives the player a welcome message. 
    Executes the new player function. 
    """
    print(INTRO)

def new_player():
        """
        Prompts the player to enter a username and returns it.
        """
        username = input("Please enter your username:\n")
        
        return username

def new_board():
    """
    Prompts the user to enter the size of the board and then
    generates the board based on the user response. 
    Board size must be between 5-8 spaces per row/column.
    """
    while True:
        board_size = input("Please enter the number of rows/columns " +  
                           "for the boards(Must be between 5 and 8): \n")
        if validate_board_size(board_size):
            print(f"You have chosen a board size of {board_size}")
            break

    return int(board_size)

def validate_board_size(size):
    """
    Checks user input to make sure it is a number between 5 and 8.
    Returns feedback to the user if they enter something that is not a number
    or if the number is not between 5 and 8.
    """
    try:
        row_size = int(size)
        if row_size < 5 or row_size > 8:
            print("Please enter a number between 5 and 8")
            return False
    except:
        print("Invalid entry: You must enter a whole number. Please try again!")
        return False

    return True

def create_board(size):
    """
    Generates the battleships board based on size provided.
    Creates a 2D matrix with equal size columns and rows.
    Stores the board elements in a list of lists.
    """
    board = [["*" for x in range(size)] for y in range(size)]

    return board

def generate_ship_location(size):
    """
    Randomly generates location for 5 ships based on the size of the board.
    Stores the ship locations in a Set to ensure there are 
    no duplicate locations. Finally, converts to set into a list 
    for easier access to the elements.
    """
    ship_pos = set()
    while len(ship_pos) < 5:
        nums = (randint(0, size - 1), randint(0, size - 1))
        ship_pos.add(nums)
    
    ship_pos_list = list(ship_pos)

    return ship_pos_list

def place_ships_on_board(board, ships):
    """
    Places the ships on the board based on the ship positions.
    Replaces the '*' with a '@' to represent a ship.
    """
    for ship in ships:
        board[ship[0]][ship[1]] = "@"

    return board

def get_user_answer(player, size):
    """
    Prompts user to input a row/column pair and stores the response
    """
    while True:
        row = input("Please choose a Row:\n")
        if validate_user_answer(size, row):
            column = input("Please choose a Column:\n")
            if validate_user_answer(size, column):
                print(f"{player} guessed: ({row}, {column})")
                break

    response = [int(row), int(column)]

    return response
    
def validate_user_answer(size, response):
    """
    Checks user input to make sure it is a valid number within the board size .
    Returns feedback to the user if they enter something that is not a number
    or if the number is not a valid row or column within the board.
    """
    
    try:
        response = int(response)
        if response < 0 or response > size - 1:
            print(f"Please enter a number between 0 and {size - 1}!")
            return False
    except:
        print("Invalid entry: You must enter a whole number. Please try again!")
        return False

    return True

def generate_pc_answer(size):
    """
    Creates a random set of coordinates as the computer's guess
    """
    random_guess = [randint(0, size - 1), randint(0, size - 1)]

    return random_guess


def check_answer(row, column, board):
    """
    Checks the board to see if the row and column provided correspond
    to a ship location or an empty position(water). Returns feedback to
    the player to advise if the input provided is a hit or a miss.
    """

new_player = Player(new_player(), 0)
print(f"Your username is: {new_player.username}")
