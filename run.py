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
    number_mistakes = 0 
    letters_guessed = [] 
    number_mistakes_allowed = len(hangman_graphics) 

    word = random.choice(words) 
    letters_word = list(word) 
    wrong_letters = [] 

    print('Welcome to Hangman')
    welcome_user()

    print() # För att kunna testa -> visa ordet
    print('The word has {} letters'.format(len(letters_word))) 

    while number_mistakes < number_mistakes_allowed:   
        print() 
        print('Wrong letters: ', end='')
        for letter in wrong_letters: 
            print('{}, '.format(letter), end='') 
        
        print() 
        print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes)) 
        
        