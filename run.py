import random
from words import word_list

# below is a function to make a random choice from the word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()
