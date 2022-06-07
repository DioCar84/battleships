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
The top left corner’s coordinates are (0, 0).
        """
class Player:
    """
    Player class. Stores the username and score for each Player object.
    Has methods for incrementing the Player's score and creating new usernames.
    """

    def __init__(self, username, score, guess, guesses_made):
        self.username = username
        self.score = score
        self.guess = guess
        self.guesses_made = guesses_made

    def increment_score(self):
        """
        Increments the Player's score by 1.
        """
        self.score += 1

    def new_player(self):
        """
        Prompts the player to enter a username and returns it.
        """
        username = input("Please enter your username:\n")
        
        self.username = username

    def get_player_answer(self, size):
        """
        Checks to see if it's the user or the PC guessing.
        Creates a random set of coordinates as the computer's guess.
        Prompts user to input a row/column pair and stores the response. 
        """

        if self.username == "Computer":
            row = randint(0, size - 1)
            column = randint(0, size - 1)
            response = [row, column]
            self.guess = response
        else:
            while True:
                row = input("Please choose a Row:\n")
                if self.validate_player_answer(size, row):
                    column = input("Please choose a Column:\n")
                    if self.validate_player_answer(size, column):
                        break
            response = [int(row), int(column)]
            self.guess = response

        return response

    def validate_player_answer(self, size, response):
        """
        Checks user input to make sure it's a valid number within the 
        board size. Returns feedback to the user if they enter something 
        that's not a number or if the number is not a valid row or 
        column within the board.
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

    def check_answer(self, size, guess, ships, display):
        """
        Checks to see if the guess enterred has already been made before,
        if so calls the get_player_answer function again until a new guess
        has been enterred. Checks the board to see if the row and column
        provided correspond to a ship location or an empty position(water).
        Returns feedback to the player to advise if the input provided is a
        hit or a miss. Alters the opponent's display to reflect the result.
        """

        if guess in self.guesses_made:
            if self.username != "Computer":
                print("You have already tried those coordinates, please choose new ones!")
            new_guess = self.get_player_answer(size)
            self.check_answer(size, new_guess, ships, display)
        else:
            self.guesses_made.append(guess)
            for x, y in ships:
                if guess == [x, y]:
                    print(f"{self.username} guessed: ({x}, {y})")
                    print(f"{self.username} scores a direct hit!!!")
                    display[x][y] = "x  "
                    self.increment_score()
                    return True

            display[guess[0]][guess[1]] = "o  "
            print(f"{self.username} guessed: ({x}, {y})")
            print(f"{self.username} hits the water...")

class Board:
    """
    """

    def __init__(self, player, size, ships, display):
        self.player = player
        self.size = size
        self.ships = ships
        self.display = display

    def new_board(self):
        """
        Prompts the user to enter the size of the board and then
        generates the board based on the user response. 
        Board size must be between 5-8 spaces per row/column.
        """
        while True:
            board_size = input("Please enter the number of rows/columns " +  
                            "for the boards(Must be between 5 and 8): \n")
            if self.validate_board_size(board_size):
                print(f"You have chosen a board size of {board_size}")
                break

        self.size = int(board_size)
        return int(board_size)

    def validate_board_size(self, size):
        """
        Checks user input to make sure it is a number between 5 and 8.
        Returns feedback to the user if they enter something that's not
        a number or if the number is not between 5 and 8.
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

    def generate_ship_location(self):
        """
        Randomly generates location for 5 ships based on the size of the board.
        Stores the ship locations in a Set to ensure there are 
        no duplicate locations. Finally, converts to set into a list 
        for easier access to the elements.
        """
        ship_pos = set()
        while len(ship_pos) < 5:
            nums = (randint(0, self.size - 1), randint(0, self.size - 1))
            ship_pos.add(nums)
        
        ship_pos_list = list(ship_pos)

        self.ships = ship_pos_list

    def create_board(self):
        """
        Generates the battleships board based on size provided.
        Creates a 2D matrix with equal size columns and rows.
        Stores the board elements in a list of lists.
        """
        board = [["-  " for x in range(self.size)] for y in range(self.size)]

        self.display = board

    def place_ships_on_board(self):
        """
        Places the ships on the board based on the ship positions.
        Replaces the '*' with a '@' to represent a ship.
        """
        for ship in self.ships:
            self.display[ship[0]][ship[1]] = "@  "

    def print_board(self, score):
        """
        Prints the board owner's name and score.
        Will also print the game board to the terminal.
        """
        print(f"{self.player}'s Board. Score: {score}")
        print("********************")
        for row in self.display:
            print(*row)
        print("********************")    

def new_game():
    """
    Runs at the beggining of every new game. 
    Prints the title, ascii battleship
    art and gives the player a welcome message. 
    Executes the new player function. 
    """
    print(INTRO)

def continue_game(score1, score2):
    """
    Checks both player's score to see if any has scored 5 hits.
    Prompts the user to decide wether they wish to continue the game.
    """
    if score1 < 5 and score2 < 5:
        keep_playing = input("Do you want to keep playing?\n" + 
        "Enter q to quit or any other key to continue: ")
        if keep_playing.lower() == "n":
            return False
        return True

    return False

def main():
    """
    The main function, used to execute the program.
    """
    new_game()
    player1 = Player("", 0, [], [])
    player1.new_player()
    player2 = Player("Computer", 0, [], [])
    board1 = Board(player1.username, 0, [], [])
    board_size = board1.new_board()
    board2 = Board(player2.username, board_size, [], [])
    board1.generate_ship_location()
    board1.place_ships_on_board()
    board2.generate_ship_location()

    while continue_game(player1.score, player2.score):
        board1.print_board(player1.score)
        board2.print_board(player2.score)
        player1.get_player_answer(board_size)
        player1.check_answer(board_size, player1.guess, board2.ships, board2.display)
        player2.get_player_answer(board_size)
        player2.check_answer(board_size, player2.guess, board1.ships, board1.display)
    
main()