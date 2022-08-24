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

random_word = random.choice(words) # randomly chooses something from the list
print(
    "Hint: The word has", len(random_word), "letters")
print("================================")

correct_guess = ["_"] * len(random_word)
# below is a list collect wrong letters guessed by the user
incorrect_guess = []

def correct_guess_list():
    """
    it will print the correct letters in the
    correct_guess list
    """
    for letter in correct_guess:
        print(letter, end=" ")
    print()




