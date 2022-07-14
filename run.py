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


def play(word):
    """
    function to collect letters guessed by the user
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

# below is a main loop for the game with if/else block 

while not guessed and tries > 0: 
    guess = input("please guess a letter or a word: ").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letter:
            print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word. ")
                tries -= 1
                guessed_letters.append(guess)
                else
                print("Good job" guess "is in the word! ")
                guessed_letters.append(guess)
                word_as_list = list(word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True


    elif len(guess) == len(word) and guess.isalpha(): #another block to check if the word already guessed, correct or wrong
        if guess in guessed_words:
            print("You already guessed the word" guess)
            elif guess != word:
                print(guess, "is not inte word!")
                tries -= 1
                guessed_words.append(guess)
                else: 
                    guessed = True
                    word_completion = word
        else :
        print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

        if guessed = True #check if the user guessed correctly 
        print("Yay, you guessed the word! You win!")
        else: 
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


