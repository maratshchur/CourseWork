from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from users.models import CustomUser

class TournmentParticipant(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Participant {self.user_id.username}"

class Tournament(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    number_of_words = models.PositiveIntegerField()
    start = models.DateTimeField()
    duration = models.DurationField()
    end = models.DateTimeField()
    participants = models.ManyToManyField(TournmentParticipant, related_name='tournaments')
    
    
    def __str__(self):
        return self.title

class TournamentWord(models.Model):
    word = models.CharField(max_length=100)
    round_number = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='words')
    
    def __str__(self):
        return f"Word {self.word} (Round {self.round_number}) in {self.tournament.title}"

class TournamentWordStatistic(models.Model):
    tournament_word_id = models.ForeignKey(TournamentWord, on_delete=models.CASCADE)  
    participant_id = models.ForeignKey(TournmentParticipant, on_delete=models.CASCADE)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    
    attempts = models.PositiveIntegerField()
    entered_words = models.JSONField(encoder=DjangoJSONEncoder, default=dict)
    guessed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Stats for {self.participant_id.user_id.username} on {self.tournament_word_id.word} in {self.tournament_id.title}"

class TournamentResult(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participant = models.ForeignKey(TournmentParticipant, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completion_time = models.DateTimeField(null=True, blank=True)
    place = models.PositiveIntegerField(default=0)  # Add this field back

    def __str__(self):
        return f"{self.participant.user_id.username} - {self.place} place in {self.tournament.title} with score {self.score}"

    @classmethod
    def recalculate_places(cls, tournament):
        results = cls.objects.filter(tournament=tournament).order_by('-score', 'completion_time')
        place = 1
        for result in results:
            result.place = place
            place += 1
            result.save()
        
class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    message = models.TextField()
    readed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
