from django.urls import path
from . import views 

urlpatterns = [
    path("daily_word", views.get_daily_word, name="get_daily_word"),
    path("words", views.get_all_daily_words, name="get_all_words"),
    path("game/data", views.get_game_statistics, name="get_game_statistics"),
    path("guess_word", views.guess_word, name="guess_word"),
    path("save_statistic", views.save_statistic, name="save_statistic"),
    path("get_hint", views.get_hint_view, name="get_hint"),
    path("add_rating", views.update_user_rating, name="update_user_rating"),
    path("add_games_quantity", views.add_games_quantity, name="add_games_quantity"),
    path("top_list", views.get_top_list, name="top_list"),
    path("training_word", views.get_random_training_word, name="get_training_word"),
    path("guess_training_word", views.guess_training_word, name="guess_training_word")
]