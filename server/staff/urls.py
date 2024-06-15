from django.urls import path
from . import views 

urlpatterns = [
    path("users_list", views.users_list, name="users_list"),
    path('create_word', views.add_daily_word, name='add_word'),
    path('create_tournament', views.create_tournament, name='create_tournament_view'),
    path('download_word_files', views.download_word_files, name='download_word_files'),
    path('tournaments_list', views.get_all_tournaments, name='get_all_tournaments'),

]
