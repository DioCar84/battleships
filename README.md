# Battleships

Battleships is a Python terminal game, which runs in the Code Institue mock terminal on Heroku.

Users can try to beat the computer by finding all of the computer's battleships before the computer can find theirs. Each battleship occupies one square on the board.

[Click here for the live version of this project]()

## How to play

Battleships is a turn-based naval strategy game based on the classic pen-and-paper game. You read all about it's history and evolution over the years on it's [Wikipedia Page](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version of the game, the player is able to create a username and choose a board size between 5 and 8 rows and columns. The boards are then generated and the ship positions randomly chosen.

The user is able to see their ships on the board, indicated by the "@" symbol. The computer's ships are hidden to provide the challenge. Spaces are indicated with a "-" symbol, incorrect guesses are marked with a "o" and direct hits will be marked with a "x".

The player and the computer will take turns attempting to guess where their opponent's ship is to try and sink all of them. The winner is the first to sink their opponent's five ships.

## Features

### Implemented Features

- User defined board size
    - The player chooses between 5 to 8 rows and columns per board
- Randomly generated ship locations that can change each game
- Computer opponent that tries to defeat the user
- Accepts user input
- Maintains score and displays the outcome of the previous guesses
- Input validation and error-checking
    - Username cannot be blank
    - User cannot input coordinates outside of the board size
    - User cannot input characters, symbols or decimal numbers
    - User cannot enter the same coordinates twice
- Data maintained in class instances

### Future Features

- Allow the player to choose their ships' position
- Create ships that vary in size
- Allow for two users to play the game

## Data Model

For this project I have decided to create a Player class and a Board class as my models. The game creates two instances of the Player class, one for the user and one for the computer. This class stores the username, score, current guess and the guesses already made.

The Player class has methods such as the `new_player` method which stores the username chosen. The `get_player_answer` method which stores the players guess and checks if it's a valid response and the `check_answer` method that provides feedback to the player based on their guess.

The game then creates two instances of the Board class, one for each player. This class stores the player that owns the board, the board size, the location of the ships and the board's display.

The Board class has methods such as the `new_board` method which gets the user's desired board size. The `generate_ship_location` method which creates five random coordinates for the battleships and the `print_board` method which prints the board and the player's score to the terminal.

## Testing

I have manually tested this project by doing the following:
  - Passed the code through a PEP8 linter and confirmed there are no issues
  - Passed invalid inputs: decimal point numbers, chars, symbols and strings where only whole numbers are allowed.
  - Passed inputs that are outside of the board size and input the same coordinates more than once.
  - Tested the game in both the Code Institue Heroku terminal and my local Gitpod terminal

### Bugs

#### Solved Bugs

#### Remaining Bugs

#### Validator Testing

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

  - Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to `Python` and `NodeJS` in that order
    - Link the Heroku app to the repository
    - Click on __Deploy__.

## Credits

- [Code Institute](https://codeinstitute.net/) for the deployment terminal and also a big part of this Read Me file
- [Ascii Art](https://www.asciiart.eu/vehicles/navy) for the Battleship ascii art
- [Pator JK](https://patorjk.com/software/taag/#p=display&v=0&f=Slant&t=Battleships) for the ascii title
- [Stack Overflow](https://stackoverflow.com/) for countless doubts and questions I had
- [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for the rules and history of the Battleships game