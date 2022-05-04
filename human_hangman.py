from hangman_words import words, letters

import random

guessed_letters = []
result = []

def choose_word():

    """This function will randomly choose
    a word for the player to guess."""

    string = str(words[random.randint(1, len(words))])

    return string
    

word = choose_word()

def guess_letter(n=None):

    """In human hangman mode, it lets the user guess a letter.
    In computer hangman mode, it lets the computer guess a letter."""

    win = False
    before = False

    if n == None:
        
        letter = input("""\nGuess a letter:

> """)

    else:
        letter = best_letter()

    letter = letter.lower()

    while letter not in letters:
        letter = input("""\nPlease make sure to choose a valid letter.
        

> """)

    result.clear()

    global attempts
    attempts = True
    
    if letter in guessed_letters:
        before = True

    if letter not in guessed_letters:
        guessed_letters.append(letter)

    for i in word:
        if before == True:
            attempts = False
        if i == letter and letter in guessed_letters:
            attempts = False
        if i in guessed_letters:
            result.append(i)
        elif i not in guessed_letters:
            result.append("_")


    print("\n" + "".join(result))
    
    if "_" not in result:
        win = True
        print(f"\nYou win! The word was {word}.")
        exit()

    if win == False:
        print("\nGuessed letters: " + ", ".join(guessed_letters))


def play():

    """Manages the amount of times that the user
     can guess in human hangman mode."""

    guesses = 5
    
    while guesses > 1:
        guess_letter()

        if attempts == True:
            guesses -= 1
        if guesses != 1:
            print(f"\nYou have {guesses} remaining guesses.")
        if guesses == 1:
            print("\nYou have 1 remaining guess.")

    while guesses == 1:
        guess_letter()

        if attempts == True:
            guesses -= 1
            print(f"\nYou lose. The word was {word}.\n")
            exit()
        else:
            print("\nYou have 1 remaining guess.")

chosen_letters = []

def pick_word():

    chosen_words = []
    
    if len(chosen_letters) < 1:
        chosen_word = input("""\nPick a word for the computer to guess:
    
> """)
        chosen_words.append(chosen_word)

    return "".join(chosen_words)

guessable_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split()
letter_frequency = []

def best_letter():

    word_list = []
    
    word2 = pick_word()

    for e in words:
        if len(e) == len(word2):
            word_list.append(e)

    word_letters = []

    for w in word_list:
        for c in w:
            word_letters.append(c)
    
    ordered_letters = sorted(word_letters)

    for l in ordered_letters:
        letter_frequency.append(word_letters.count(l))
    
    for b in letter_frequency:
        if b in letter_frequency:
            letter_frequency.remove(b)


    chosen_letter = guessable_letters[letter_frequency.index(max(letter_frequency))]
    guessable_letters.remove(chosen_letter)
    letter_frequency.remove(max(letter_frequency))
    chosen_letters.append(chosen_letter)

    return chosen_letter


def keep_playing():
    tries = 5

    while tries > 0:
        guess_letter(1)
        tries -= 1