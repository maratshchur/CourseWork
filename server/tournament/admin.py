from django.contrib import admin

from tournament.models import Message, Tournament, TournamentResult, TournamentWord, TournamentWordStatistic, TournmentParticipant

admin.site.register(TournmentParticipant)
admin.site.register(TournamentWord)
admin.site.register(Tournament)
admin.site.register(TournamentWordStatistic)
admin.site.register(TournamentResult)
admin.site.register(Message)