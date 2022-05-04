from hangman_words import words
from human_hangman import choose_word, guess_letter, play
import sys
from human_hangman import keep_playing


def welcome():

    "Greets the user"

    print("\nWelcome to the hangman simulator!")


def word_list():

    "Prints the list of available words."

    print(words)


def start():

    """Asks the user whether they want to play, 
    read the word list, or exit the program."""
    
    answer = input("""\nWhat would you like to do?

1. Play
2. Word list
3. Quit

> """)

    while answer != "1" and answer != "2" and answer != "3":

        answer = input("""\nInvalid action. Please choose from one of the options above (type 1, 2 or 3).
    
> """)
    
    if answer == "1":
        game_mode()
    
    elif answer == "2":
        word_list()
        exit()
    
    elif answer == "3":
        print("\nGoodbye!")
        exit()


def game_mode():

    """Asks the user what game mode they want to play and
    then executes the chosen game mode."""

    response = input("""\nGreat! What game mode would you like to play?
    
1. Human Hangman
2. Computer Hangman
3. Go back

> """)

    while response != "1" and response != "2" and response != "3":

        response = input("""\nInvalid action. Please choose from one of the options above (type 1, 2 or 3).

> """)

    if response == "1":
        play()

    elif response == "2":
        keep_playing()

    elif response == "3":
        start()
    
    