import random
from word import words
from hangman_structure import hangman_graphics

# chosen word
word = random.choice(words)

# remove from this list until there are no more left
letters_word = list(word)

# mistakes
number_mistakes = 0
number_mistakes_allowed = len(hangman_graphics)

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


def start_game_loop():

    # while the user has guesses left
    while number_mistakes < number_mistakes_allowed:
        print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    letter_user = input('Enter a letter --> ')

    letter_user = None

    while True:
            #ask for user input
            letter_user = input('Enter a letter --> ')

            # check if only alphabet character
            if not letter_user.isalpha():
                print(' Make sure you enter an alphabet not a number\n\n')
                continue

            # check that only a single character has been added
            if len(letter_user) != 1:
                print("Please enter only a sinlgle character \n\n")
                continue

            # check for correct guess
            # if the letter is in the "letter_word" list
                # remove the letter from the list
                # add letter to the list of correctly guessed letters
                # break out of the while True loop


            # break from loop after all checks and logic are done
            print("New Round About to begin \n\n")
            break



# start the game and call needed functions
if __name__ == "__main__":
    welcome_user()
    start_game_loop()