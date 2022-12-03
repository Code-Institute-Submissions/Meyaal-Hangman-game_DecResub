import random
from word import words
from structure import hangman_graphics
from validateinput import *

validate = ValidateInput()

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
def get_input() -> str:

    result = ""
    ok = False
    while ok != True:
        result = input('Enter a letter --> ') 
        ok = validate.validate(result)
        if ok: 
            break
    return result

# Client program
def HangmanClient() -> None:
