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
    Runs at the beggining of every new game. Prints the title, ascii battleship art and 
    gives the player a welcome message. Executes the new player function. 
    """
    print(INTRO)
    new_player()


def new_player():
    """
    Prompts the player to enter a username and returns it.
    """
    username = input("Please enter your username:\n")
    
    return username


new_game()
