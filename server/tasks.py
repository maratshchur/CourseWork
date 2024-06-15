import os
import schedule
import time
from datetime import datetime
import django
from django.http import HttpRequest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django.setup()

from game.main_functionality.word_processing import get_new_word
from game.models import DailyWord
from tournament.views import update_tournament_scores

def create_guess_word():
    print('genereting')
    now = datetime.now()
    if now.hour == 0 and now.minute == 0:
        date = now.date()
        word = get_new_word()
        game_number = DailyWord.objects.count() + 1
        guess_word = DailyWord(date=date, word=word, game_number=game_number)
        guess_word.save()
        print(guess_word)

schedule.every().day.at("00:00").do(create_guess_word)


dummy_request = HttpRequest()

schedule.every(1).minutes.do(update_tournament_scores, dummy_request)

# Бесконечный цикл для выполнения запланированных задач
while True:
    print("Working")
    schedule.run_pending()
    time.sleep(30)