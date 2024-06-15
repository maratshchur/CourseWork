from django.urls import path
from . import views 

urlpatterns = [
    path("upcoming_tournaments", views.upcoming_tournaments, name="upcoming_tournaments"),
    path('tournament/<int:pk>/data/', views.get_tournament_data, name='get_tournament_data'),
    path('tournaments/<int:tournament_id>/statistic/', views.get_user_tournament_statistic, name='get_user_word_statistic'),
    path('tournaments/save_statistic/', views.save_statistic, name='save_statistic'),
    path('tournament/guess_word/', views.guess_word, name='guess_word'),
    path('tournament/<int:tournament_id>/stats/', views.tournament_participant_stats, name='tournament_participant_stats'),
    path('tournament/<int:tournament_id>/participation/', views.user_participate_in_tournament, name='tournament_participant_stats'),
    path('tournament/<int:tournament_id>/participate/', views.participate_in_tournament, name='participate_in_tournament'),
    path('tournament/<int:tournament_id>/save_completion_time/', views.save_completion_time, name='save_completion_time'),
    path('tournament/<int:tournament_id>/get_completion_time/', views.get_completion_time, name='get_completion_time'),
    path('new_messages/', views.new_messages, name='new_messages'),
    path('messages/<int:message_id>/read/', views.mark_message_as_read, name='mark_message_as_read'),

    path('messages/', views.get_all_messages, name='get_all_messages'),
    path('test/', views.update_tournament_scores, name='get_all_messages'),



]
