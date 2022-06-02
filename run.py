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

def new_game():
    """
    Runs at the beggining of every new game. Prints the title, ascii battleship art 
    and gives the player a welcome message. Executes the new player function. 
    """
    print(INTRO)
    new_player()


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
            raise ValueError(f"Please enter a number between 5 and 8")
    except ValueError as e:
        print(f"Invalid entry: {e} Please try again!\n")
        return False

    return True

def create_board(board_size):
    """
    Generates the battleships board based on size provided.
    Creates a 2D matrix with equal size columns and rows.
    """
    for x in range(board_size):
        print("*  " * board_size)

board_size = new_board()
create_board(board_size)
