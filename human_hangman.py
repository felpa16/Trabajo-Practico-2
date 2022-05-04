from hangman_words import words, letters

import random

guessed_letters = []
result = []

c = 0

def choose_word(z):

    """This function will randomly choose
    a word for the player to guess."""

    computer_string = ""

    if z == 0:
        string = words[random.randint(0, len(words) - 1)]

    #if z == 1:
     #   if c == 0:
      #      string = input("""\nPick a word for the computer to guess:
       #     
#> """)
 #           computer_string += string
  #          c += 1
   #     
    #    elif c != 0:
     #       return computer_string

    return string

word1 = choose_word(0)

c = 0
if c > 0:
    word2 = input("""\nPick a word for the computer to guess:
           
> """)

c += 1

def guess_letter(k, n=None):

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

    if k == 0:

        for i in word1:
            if before == True:
                attempts = False
            if i == letter and letter in guessed_letters:
                attempts = False
            if i in guessed_letters:
                result.append(i)
            elif i not in guessed_letters:
                result.append("_")
    
    elif k == 1:

        for i in word2:
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
        if k == 0:
            print(f"\nYou win! The word was {word1}.")
            exit()
        if k == 1:
            print(f"\nYou win! The word was {word2}.")
            exit()

    if win == False:
        print("\nGuessed letters: " + ", ".join(guessed_letters))


def play():

    """Manages the amount of times that the user
     can guess in human hangman mode."""

    guesses = 5

    while guesses > 1:
        guess_letter(0)

        if attempts == True:
            guesses -= 1
        if guesses != 1:
            print(f"\nYou have {guesses} remaining guesses.")
        if guesses == 1:
            print("\nYou have 1 remaining guess.")

    while guesses == 1:
        guess_letter(0)

        if attempts == True:
            guesses -= 1
            print(f"\nYou lose. The word was {word1}.\n")
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

guessable_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
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

    for l in guessable_letters:
        letter_frequency.append(word_letters.count(l))


    chosen_letter = guessable_letters[letter_frequency.index(max(letter_frequency)) - 1]
    guessable_letters.remove(chosen_letter)
    letter_frequency.clear()
    chosen_letters.append(chosen_letter)


    return chosen_letter


def keep_playing():
    tries = 5

    while tries > 0:
        guess_letter(1, 1)
        tries -= 1

    if tries == 0:
        print(f"You lose. The word was {word2}.")