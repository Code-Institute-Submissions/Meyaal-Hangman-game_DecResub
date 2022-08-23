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
alphabet = ('abcdefghijklmnopqrstuvwxyz')

print()
print('The word has {} letters'.format(len(letters_word)))


while number_mistakes < number_mistakes_allowed:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    letter_user = input('Enter a letter --> ')

    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print('You have already entered this letter, enter another one')
        letter_user = input('Enter a letter --> ')
    if letter_user not in alphabet:
        print(' Make sure you enter an alphabet not a number')
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
    print()
    print('-------------------------------------------')

    if len(letters_guessed) == len(letters_word):
        print()
        print('YOU WOOOON!!!')
        break

if number_mistakes == number_mistakes_allowed:
    print()
    print('YOU LOST! TRY AGAIN!')
