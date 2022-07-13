import random
from words import word_list

# below is a function to make a random choice from the word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

# create a play function for users and a while loop

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    
    
    