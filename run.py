import random
from word import words
from hangman_structure import hangman_graphics
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
    while ok is not True:
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
    print()
    print('The word has {} letters'.format(len(letters_word)))
    while number_mistakes < number_mistakes_allowed:
        print()
        print('Wrong letters: ', end='')
        for letter in wrong_letters:
            print('{}, '.format(letter), end='')
        print()
        print(
            'Guesses left: {}'.format(
                number_mistakes_allowed - number_mistakes))
        letter_user = get_input()
        while letter_user in letters_guessed or letter_user in wrong_letters:
            print()
            print('You have already entered this letter, enter another one')
            letter_user = get_input()  # New input
        if letter_user not in letters_word:
            number_mistakes += 1
            wrong_letters.append(letter_user)
        print()
        print('Word: ', end='')
        for letter in letters_word:
            if letter_user == letter:
                letters_guessed.append(letter_user)

        for letter in letters_word:
            if letter in letters_guessed:
                print(letter + ' ', end='')
            else:
                print('_ ', end='')
        print()
        if number_mistakes:
            print(hangman_graphics[number_mistakes - 1])
# when we have the right word, break
        if len(letters_word) == len(letters_guessed):
            break
    print()
    print('-------------------------------------------')
    print()
    if len(letters_guessed) == len(letters_word):
        print('YOU WOOOON!!!')
    if number_mistakes == number_mistakes_allowed:
        print('YOU LOST! TRY AGAIN!')
# Program starting here


if __name__ == "__main__":
    HangmanClient()