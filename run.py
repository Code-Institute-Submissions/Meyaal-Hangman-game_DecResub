import random
from word import words
from hangman_structure import get_hangman


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
graphics = x

def correct_guess_list():
    """
    the function will print the correct letters in the
    correct_guess list
    """
    for letter in correct_guess:
        print(letter, end=" ")
    print()

def letters_only():
    """
    this function will validate input from users
    only letters and no character or numbers
    """
    while True:
        user_input_letter = input("type a letter: \n").lower()
        if not user_input_letter.isalpha():
            print('Error, please select a letter')
        else:
            return user_input_letter 

correct_guess_list()
get_hangman(len(incorrect_guess))

while True:
    user_input = letters_only()
    if user_input in random_word:
        INDEX = 0
        for i in random_word:
            if i == user_input:
                correct_guess[INDEX] = user_input
            INDEX += 1
        correct_guess_list()

    else:
        if user_input not in incorrect_guess:
            incorrect_guess.append(user_input)
            get_hangman(len(incorrect_guess))
            print(f'sorry, letter {user_input} is not in the word')

        else:
            print("You already guessed it, please try again...")
        print(incorrect_guess)

    if len(incorrect_guess) > 5:
        print("You lose, please try again")
        print("correct word is ", random_word)
        break

    if "_" not in correct_guess:
        print("Congratulations!!!, you have guessed the correct letter")
        break