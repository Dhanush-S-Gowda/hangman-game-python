# Hangman Game

## Overview

This Hangman game is a text-based Python implementation where players can guess words and try to complete them before running out of lives. The game provides a visual representation of the hangman figure and gives players the option to exit or start a new game.

## Features

- **Word Selection**: Randomly selects a word from a list of over 100 words stored in the `words.json` file.
- **Visual Feedback**: Displays a series of ASCII art hangman figures for each incorrect guess stored in the `hangmanPics.json` file.
- **User Interaction**: Allows users to input characters to guess the word.
- **Game Outcome**: Declares whether the player has won or lost the game, revealing the correct word if lost.
- **New Game Option**: After completing a game, users have the option to start a new game.

## Files

- **words.json**: Contains a list of words used for the game. Over 100 words are stored in this file.
- **hangmanPics.json**: Contains a list of ASCII art representations of the hangman figure corresponding to each incorrect guess.

## Usage

1. Run the Python script in your terminal or preferred Python environment.
2. Choose to either exit the game (`"e"`) or play (`"p"`).
3. If playing, input characters to guess the word.
4. The game will provide visual feedback and inform you of the outcome.
5. After completing a game, choose to start a new game.

## Dependencies

- Python 3.x

## How to Run

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Open a terminal in the project directory.
4. Run the command: `python hangman_game.py`

## Example

```
$ python hangman_game.py
 Enter "e" to exit or "p" to play
->>p

['_', '_', '_', '_', '_']
Enter character: e
Your guess e is in the word , completed words 1
['_', '_', 'e', '_', '_']
Enter character: x
   +---+
   |   |
       |
       |
       |
       |
   =========
Your guess x is not in the word, you lose one life. Remaining: 6
['_', '_', 'e', '_', '_']
...
You lost!! Never give up... The word was example

 ------------------New Game-----------------
 Enter "e" to exit or "p" to play
->>e
```

## License

This Hangman game is licensed under the MIT License.
