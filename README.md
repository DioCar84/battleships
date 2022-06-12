# Battleships

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can try to beat the computer by finding all of the computer's battleships before the computer can find theirs. Each battleship occupies one square on the board.

[Click here for the live version of this project](https://battleships-diogo.herokuapp.com/)

![Responsive Mock-up](/assets/images/responsive-project3.png)

## How to play

Battleships is a turn-based naval strategy game based on the classic pen-and-paper game. You read all about its history and evolution over the years on its [Wikipedia Page](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version of the game, the player is able to create a username and choose a board size between 5 and 8 rows and columns. The boards are then generated, and the ship positions randomly chosen.

The user is able to see their ships on the board, indicated by the `@` symbol. The computer's ships are hidden to provide the challenge. Spaces are indicated with a `-` symbol, incorrect guesses are marked with a `o` and direct hits will be marked with a `x`.

The player and the computer will take turns attempting to guess where their opponent's ship is to try and sink all of them. The winner is the first to sink their opponent's five ships.

## Features

### Implemented Features

- Intro with ASCII art and useful information

![Game Intro](/assets/images/Battleships%20intro.png)

- User defined board size
    - The player chooses between 5 to 8 rows and columns per board
- Randomly generated ship locations that can change each game

![Battle Boards](/assets/images/Battleships%20boards.png)

- Computer opponent that tries to defeat the user
- Accepts user input and returns feedback

![Input Feedback](/assets/images/Input%20feedback.png)

- Maintains score and displays the outcome of the previous guesses

![Updated Boards](/assets/images/Updated%20boards.png)

- Input validation and error-checking
    - Username cannot be blank or Computer
    - User cannot input coordinates outside of the board size
    - User cannot input characters, symbols or decimal numbers
    - User cannot enter the same coordinates twice

![Username Validation](/assets/images/Username%20validation.png)

![Guess Validation 1](/assets/images/Guess%20validation%201.png)

![Guess Validation 2](/assets/images/Guess%20validation%202.png)

- Data maintained in class instances(Player and Board)

### Future Features

- Allow the player to choose their ships' position
- Create ships that vary in size
- Allow for two users to play the game
- Change coordinates from 0 indexing for better user experience
- Allow the user to choose "Computer" as a username

## Data Model

For this project I have decided to create a Player class and a Board class as my models. 

The game creates two instances of the Player class, one for the user and one for the computer. This class stores the username, score, current guess and the guesses already made.

The Player class has methods such as the `new_player` method which stores the username chosen. The `get_player_answer` method which stores the players guess and checks if it's a valid response and the `check_answer` method that provides feedback to the player based on their guess.

The game then creates two instances of the Board class, one for each player. This class stores the player that owns the board, the board size, the location of the ships and the board's display.

The Board class has methods such as the `new_board` method which gets the user's desired board size. The `generate_ship_location` method which creates five random coordinates for the battleships and the `print_board` method which prints the board and the player's score to the terminal.

## Testing

I have manually tested this project by doing the following:
  - Passed the code through a PEP8 linter and confirmed there are no issues
  - Passed invalid inputs: decimal point numbers, chars, symbols and strings where only whole numbers are allowed.
  - Passed inputs that are outside of the board size and input the same coordinates more than once.
  - Passed inputs that are blank or "Computer" as a username.
  - Tested the game in both the Code Institute Heroku terminal and my local Gitpod terminal

### Bugs

#### Solved Bugs

  - The `display_result` function was returning feedback for a guess that the player had not entered. I fixed this by accessing the correct data structure, as I was originally accessing the ship position array instead of the guesses made array.

  - The `check_answer` function was creating an infinite guessing loop if the player had already entered the chosen coordinates. I fixed this by adding a return `True` or return `False` condition to stop looping if the new coordinates have not been previously guessed.

#### Remaining Bugs

  - No bugs remaining

#### Validator Testing

  - PEP8
    - No errors were returned from PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

  - Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to `Python` and `NodeJS` in that order
    - Link the Heroku app to the repository
    - Click on __Deploy__.

## Credits

- [Code Institute](https://codeinstitute.net/) for the deployment terminal, a big part of this Read Me file and the code for the `create_board` function
- [Ascii Art](https://www.asciiart.eu/vehicles/navy) for the Battleship ASCII art
- [Pator JK](https://patorjk.com/software/taag/#p=display&v=0&f=Slant&t=Battleships) for the ASCII title
- [Stack Overflow](https://stackoverflow.com/) for the countless doubts and questions I had
- [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for the rules and history of the Battleships game