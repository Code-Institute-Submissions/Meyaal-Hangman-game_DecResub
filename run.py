import random
from word import word_list

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

def get_word():
    """
    randomly chooses something from the list
    """
    word = random.choice(word_list)
    return word.upper()



