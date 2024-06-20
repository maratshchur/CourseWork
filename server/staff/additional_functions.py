from datetime import datetime
import os
from game.main_functionality.word_processing import load_close_words
from game.models import DailyWord
from pathlib import Path


def is_word_in_file(word, file_path=Path(__file__).parent.parent / 'game' /  'data' / 'all_words.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return word in words
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False

def create_word(word):
    if not is_word_in_file(word):
        return 0
    
    try:
        if not find_file_with_word(Path(__file__).parent.parent /  'game_files', word):
            load_close_words(word)
        return 1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
        
        
def find_file_with_word(directory, word):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if word.lower() in file.lower():
                return True
    return False