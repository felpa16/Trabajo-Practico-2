from menu import start, game_mode
from hangman import hangman, pick_human_word, pick_computer_word


def main():

    if start() == 1:

        play()

def play():

    mode = game_mode()

    if mode == 1:

        word = pick_human_word()

        while hangman(word, "h") == True:
            play()

        else:
            print("\nGoodbye!")
            exit()

    elif mode == 2:

        word = pick_computer_word()

        while hangman(word, "c") == True:
            play()
        
        else:
            print("\nGoodbye!")
            exit()

    elif mode == 3:
        main()

if __name__ == '__main__':
    main()