import random
from hangman_words import words, letters





#funcion que elige la palabra para el human

def pick_human_word():

    return words[random.randrange(0, len(words) - 1)]







#funcion que elige la palabra para el computer

def pick_computer_word():

    word = input("\nPick a word for the computer to guess:\n\n> ")
    while word not in words:
        word = input("\nPlease pick a valid word:\n\n> ")
    
    return word









#funcion que te pregunta si queres volver a jugar

def play_again():

    k = input("\nWould you like to play again? [yes/no]\n\n> ")

    while k != "yes" and k != "no":
        k = input('\nPlease type "yes" or "no".\n\n> ')
    
    if k == "yes":
        return True

    elif k == "no":
        return False










#funcion que elige la letra para el human

def get_human_letter():
    
    return input("\nGuess a letter or word:\n\n> ")












#funcion que elige la letra para el computer

picked_letters = []

def get_computer_letter(string):

    letter_frequency = []
    guessable_letters = letters.copy()

    for i in picked_letters:
        guessable_letters.remove(i)

    possible_words = [i for i in words if len(i) == len(string)]

    possible_letters = []

    for w in possible_words:
        for l in w:
            possible_letters.append(l)

    for i in letters:
        if i not in picked_letters:
            letter_frequency.append(possible_letters.count(i))

    
    letter = guessable_letters[letter_frequency.index(max(letter_frequency))]
    picked_letters.append(letter)

    return letter












#funcion que juega al hangman

def hangman(word, mode):

    guesses = 5
    guessed_letters = []
    result = []

    print("_" * len(word))

    while guesses > 0:

        if mode == "h":
            letter = get_human_letter()

        elif mode == "c":
        
            letter = get_computer_letter(word)

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
            return play_again()


        while len(letter) != len(word) and letter not in letters and letter != word:
            letter = input("\nPlease pick a valid letter:\n\n> ")

        if letter == word:
            print(f"You win! The word was {word}.")
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
            return play_again()
            
        elif letter in word:
            print(f"You win! The word was {word}.")
            return play_again()

