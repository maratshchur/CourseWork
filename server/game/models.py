import pathlib
from django.db import models
import sys
from django.core.serializers.json import DjangoJSONEncoder
#sys.path.append(r'D:\4_SEM\CourseWork\server')
from users.models import CustomUser


class DailyWord(models.Model):
    date = models.DateField()
    word = models.CharField(max_length=100)
    game_number = models.IntegerField(unique=True, primary_key=True)  

    def __str__(self):
        return f"Game #{self.game_number}: {self.word}"

class GameStatistic(models.Model):
    word_number = models.ForeignKey(DailyWord, on_delete=models.CASCADE)  # Создать внешний ключ на модель DailyWord
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attempts = models.PositiveIntegerField()
    entered_words = models.JSONField(encoder=DjangoJSONEncoder, default=dict)
    hints = models.PositiveIntegerField()
    guessed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Game #{self.word_number.game_number} for User {self.user.username}"
    
        
