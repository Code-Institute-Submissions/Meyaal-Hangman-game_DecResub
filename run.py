import random
from words import word_list


def get_word():
    """
    function to make a random choice from the word_list
    """
    word = random.choice(word_list)
    return word.upper()

# create a play function for users and a while loop

def play(word):
    """
   create a play function for users and a while loop inside it
    """

    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # a loop with three possible conditional branches for different user inputs
    # if/else block to guess a letter or a word