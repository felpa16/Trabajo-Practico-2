import random
from hangman_words import words, letters

def pick_human_word():

    "This function will pick a random word for the user to guess."

    return words[random.randrange(0, len(words) - 1)]


def pick_computer_word():

    "This function will ask the user for a word for the computer to guess it."

    word = input("\nPick a word for the computer to guess:\n\n> ")
    while word not in words:
        word = input("\nPlease pick a valid word:\n\n> ")
    
    return word



def play_again():

    """This function will ask the player whether or not they want to play again.
    
    Returns True if the user wants to keep playing or False if they don't want to play anymore."""


    k = input("\nWould you like to play again? [yes/no]\n\n> ")

    while k != "yes" and k != "no":
        k = input('\nPlease type "yes" or "no".\n\n> ')
    
    if k == "yes":
        return True

    elif k == "no":
        return False


def get_human_letter():

    """This function will ask the user to guess a letter or word
    and return the guessed letter/word."""
    
    return input("\nGuess a letter or word:\n\n> ")


def hangman(word: str, mode: str):

    guesses = 5
    guessed_letters = []
    result = []
    picked_letters = []

    print("_" * len(word))

    while guesses > 0:

        if mode == "h":
            letter = get_human_letter()

        elif mode == "c":
        
            letter_frequency = []
            guessable_letters = letters.copy()

            for i in picked_letters:
                guessable_letters.remove(i)

            possible_words = [i for i in words if len(i) == len(word)]

            possible_letters = []

            for w in possible_words:
                for l in w:
                    possible_letters.append(l)

            for i in letters:
                if i not in picked_letters:
                    letter_frequency.append(possible_letters.count(i))


            letter = guessable_letters[letter_frequency.index(max(letter_frequency))]
            picked_letters.append(letter)

            confirm = input(f"\nIs the letter '{letter}' in your word?  [yes/no]\n\n> ")
            while confirm != "yes" and confirm != "no":
                confirm = input('\nPlease type "yes" or "no".\n\n> ')
            
            if confirm == "yes":
                if letter in word:
                    pass
                elif letter not in word:
                    print("\nHey! Don't lie to me!")

            elif confirm == "no":
                if letter in word:
                    print("\nHey! Don't lie to me!")
                elif letter not in word:
                    pass
            


        if len(letter) == len(word) and letter != word:
            print(f"\nYou lose. The word was {word}.")
            picked_letters.clear()
            return play_again()


        while len(letter) != len(word) and letter not in letters and letter != word:
            letter = input("\nPlease pick a valid letter:\n\n> ")

        if letter == word:
            print(f"You win! The word was {word}.")
            picked_letters.clear()
            return play_again()

        if (letter not in word) and (letter not in guessed_letters):
            guesses -= 1

        if letter not in guessed_letters:
            guessed_letters.append(letter)

        for i in word:

            if i in guessed_letters:
                result.append(i)
            elif i not in guessed_letters:
                result.append("_")

        if "_" not in result:
            print(f"You win! The word was {word}.")
            picked_letters.clear()
            return play_again()

        print("\n" + "".join(result)) 
        print("\nGuessed letters: " + ", ".join(guessed_letters))

        if guesses > 1:
            print(f"\nYou have {guesses} remaining guesses.")
        elif guesses == 1:
            print(f"\nYou have {guesses} remaining guess")

        result.clear()

    if guesses == 0:
        if letter not in word:
            print(f"\nYou lose. The word was {word}.")
            picked_letters.clear()
            return play_again()
            
        elif letter in word:
            print(f"You win! The word was {word}.")
            picked_letters.clear()
            return play_again()