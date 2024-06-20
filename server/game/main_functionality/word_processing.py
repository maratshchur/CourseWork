import random
from gensim.models import KeyedVectors
from math import ceil
import json
import functools
from pathlib import Path
from .paths import ALL_WORDS_FILE, MODEL_FILE, GAME_FILES


def retry_if_none(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            result = func(*args, **kwargs)
        return result
    return wrapper

@retry_if_none
def get_new_word():
    """
    Returns a random word from the dictionary file.

    """
    random_word = None
    with open(Path(__file__).parent.parent.parent / 'game' /  'data' / 'all_words.txt', "r", encoding="utf-8") as f:
        for line in f:
            if random.random() < 1e-3:  # Probability of selecting the line
                random_word = line.split()[0].strip()
                break  # Exit the loop after selecting a word
    return random_word

def check_word_selected(word):
    """
    Checks if a word has been selected.

    :param word: The word to check.
    :return: True if a word has been selected, False otherwise.
    """
    if word is None:
        return False
    return True

def load_close_words(word):
    """
    Loads and saves close words related to a given word.

    :param word: The word for which to load and save close words.
    """
    model = KeyedVectors.load_word2vec_format(Path(__file__).parent.parent.parent / 'game' /  'data' / 'model.txt', binary=False)
    with open(Path(__file__).parent.parent.parent / 'game_files' / f'close_words_{word}.json', "w", encoding="utf-8") as f:
        result = model.most_similar(positive=[word], topn=35519)
        result = {item[0]: index for index, item in enumerate(result)}
        json.dump(result, f, indent=4, ensure_ascii=False)        
        


def get_word_closeness(user_input, word_to_guess):
    """
    Retrieves the closeness value of a user's input word to the word to guess.

    :param user_input: The user's input word.
    :param word_to_guess: The word to guess.
    :return: The closeness value of the user's input word.
    """
    with open(Path(__file__).parent.parent.parent /  'game_files' / f'close_words_{word_to_guess}.json', "r", encoding="utf-8") as f:
        data = json.load(f)
        number = data[user_input]
        return number + 2


def get_hint(closest_word_guessed_number, word_to_guess):
    """
    Generates a hint for the user based on the closest word guessed.

    :param closest_word_guessed: The closest word guessed by the user.
    :param word_to_guess: The word to guess.
    :return: A hint word and the hint closeness.
    """
    with open(Path(__file__).parent.parent.parent /  'game_files' / f'close_words_{word_to_guess}.json', "r", encoding="utf-8") as f:
        data = json.load(f)
        print("Word guessed =", closest_word_guessed_number)
        hint_closeness = ceil(closest_word_guessed_number * 0.6)
        word = list(data.keys())[hint_closeness - 1]
        return word, hint_closeness+1
    
    

# word_to_guess = get_new_word()
# if word_to_guess != None:
#     load_close_words(word_to_guess)
#     print("Words loaded sucessfully")
#     print("Try to guess the word >.<")
# while True:
#     a=input()
#     if(a=="q"):
#         print("word:", word_to_guess)
#         break
#     elif (a==word_to_guess):
#         print("Congratulations, word guessed !!!!!!!!!")
#     try:
#         print(get_word_closeness(a, word_to_guess))   
#     except Exception as e:
#         print("Some exception")
#         continue
  
# model = KeyedVectors.load_word2vec_format("noun_only_model.txt", binary=False)
# result = model.most_similar(positive=["орех"], topn=500)
# print(result)

# load_close_words("чайник")