from gensim.models import KeyedVectors
from navec import Navec
import logging
from tqdm import tqdm
import re


# logging.basicConfig(level=logging.INFO)

# path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
# navec = Navec.load(path)

# print('пес' in navec)
# model = KeyedVectors.load_word2vec_format("model.txt", binary=False)
# model.most_similar(positive=["король_NOUN", "женщина_NOUN"], topn=1)
# nouns = []
# ''' удаление странных слов а также оставляем только существительные'''
# with open("model.txt", "r", encoding="utf-8") as  f:
#     for line in tqdm(f, total=249334):
#         if "_NOUN" not in line or "::" in line:
#             continue

#         clear_line = line.replace("_NOUN", "")
#         clear_word = line.split('_')[0].strip()

#         if "-" in clear_word:
#              continue
#         has_english_letter = re.search(r'[A-Za-z0-9]', clear_word)
#         if(has_english_letter):
#             continue
#         if clear_word not in navec:
#             print(f"Strange word: {clear_word}")
#             continue

#         nouns.append(clear_line)

#     with open("noun_only_model.txt", "w", encoding="utf-8") as f:
#         f.write(f"{len(nouns)} 300\n")
#         for line in nouns:
#             f.write(line)

""" Создание текстового файла только из слов"""
nouns = []
with open("noun_only_model.txt", "r", encoding="utf-8") as f:
    next(f)  # Пропускаем первую строку
    for line in tqdm(f, total=249334):
        clear_word = line.split(' ')[0].strip()
        nouns.append(clear_word)

    with open("dict.txt", "w", encoding="utf-8") as f:
        for line in nouns:
            f.write(line+'\n')

# logging.info("Loading model...")
# model = KeyedVectors.load_word2vec_format("noun_only_model.txt", binary=False)
# model.
# print(model.most_similar(positive=["электростанция"], topn=100))