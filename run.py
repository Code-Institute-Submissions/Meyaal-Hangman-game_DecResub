import random
from word import words
from hangman_structure import hangman_graphics

def welcome_user():
    """
    This function allows user to type
    their name.
    user cannot use numbers
    username must have characters only
    """
    username = None

    while True:
        username = input('Enter your name\n')

        if not username.isalpha():
            print('Username must be alphabets only')
            continue
        else:
            print('welcome '+username)
            break


print('Welcome to Hangman')
welcome_user()

# create some variables for the game
# number of misstakes
# number af letters guessed
# use the structure to show how many tries left
# let the user knows how many letters
# choose random word from list
# let the user knows how many letters


number_mistakes = 0
letters_guessed = []
number_mistakes_allowed = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word) 
wrong_letters = []

print()
print('The word has {} letters'.format(len(letters_word)))


