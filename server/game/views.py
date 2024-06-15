from datetime import datetime
import json
import os
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import DailyWord, GameStatistic
from .main_functionality.word_processing import get_word_closeness, get_hint
from users.models import Profile
from django.db.models import F


def get_daily_word(request):
    today = datetime.date.today() 

    try:
        daily_word = DailyWord.objects.latest('pk')
        response_data = {
            "game_number": daily_word.game_number,
            "word": daily_word.word,
            "date": daily_word.date.strftime("%Y-%m-%d")
        }

        return JsonResponse(response_data, status=200)

    except DailyWord.DoesNotExist:
        return JsonResponse({"error": "No word found for today"}, status=404)
    
@csrf_exempt   
def get_daily_word_by_number(request):

    game_number = request.GET.get('game_number')

    if game_number:
        try:
            game_number = int(game_number)
            daily_word = DailyWord.objects.get(game_number=game_number)

            response_data = {
                "game_number": daily_word.game_number,
                "word": daily_word.word,
                "date": daily_word.date.strftime("%Y-%m-%d") 
            }

            return JsonResponse(response_data)

        except ValueError:
            return JsonResponse({"error": "Invalid game number. Please provide a valid integer."}, status=400)

        except DailyWord.DoesNotExist:
            return JsonResponse({"error": "No word found for this game number."}, status=404)

    else:
        return JsonResponse({"error": "Please provide a game number."}, status=400)
    
    
@csrf_exempt
def get_all_daily_words(request):

    daily_words = DailyWord.objects.all()
    response_data = [
        {
            "game_number": word.game_number,
            "word": word.word,
            "date": word.date.strftime("%Y-%m-%d")
        }
        for word in daily_words
    ]

    return JsonResponse({'data':response_data}, status = 200)


@csrf_exempt
def get_game_statistics(request):
    user = request.user
    game_number = request.GET.get('game_number')
    game_statistic = GameStatistic.objects.filter(user=user, word_number=game_number)
    response_data = [
        {
            'attempts': stat.attempts,
            'entered_words': stat.entered_words,
            'hints': stat.hints,
            'guessed' : stat.guessed
        }
        for stat in game_statistic
        ]
    
    return JsonResponse(response_data, safe=False)



@csrf_exempt
def guess_word(request):
    user_word = request.GET.get("user_word")
    game_word = request.GET.get("game_word")
    game_number = request.GET.get("game_number")
    guessed = False
    guessed_earlier = False

    try:
        if user_word==game_word:
            if not GameStatistic.objects.get(word_number_id = game_number, user_id=request.user.id).guessed:
                guessed =True
            else:
                guessed_earlier = True
            closeness = 1
        else:
            if GameStatistic.objects.get(word_number_id = game_number, user_id=request.user.id).guessed:
                guessed_earlier = True
            closeness = get_word_closeness(user_word, game_word)
        return JsonResponse ({"closeness": closeness, "guessed": guessed, "guessed_earlier": guessed_earlier}, status=200)
    except:
        return JsonResponse ({"message": "error" }, status=400)
    
@csrf_exempt
def guess_training_word(request):
    user_word = request.GET.get("user_word")
    game_word = request.GET.get("game_word")
    guessed = False
    try:
        if user_word==game_word:
            guessed =True
            closeness = 1
        else:
            closeness = get_word_closeness(user_word, game_word)
        return JsonResponse ({"closeness": closeness, "guessed": guessed}, status=200)
    except:
        return JsonResponse ({"message": "error" }, status=400)
    
@csrf_exempt
def save_statistic(request):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        game_number = data.get('game_number')
        attempts = data.get('attempts')
        hints = data.get('hints')
        words = data.get('words')
        guessed = data.get('guessed')
        
        game_statistic, created = GameStatistic.objects.get_or_create(
            word_number_id=game_number,
            user_id=request.user.id,
            defaults={
                'attempts': attempts,
                'hints': hints,
                'entered_words': words,
                'guessed': guessed
            }
        )

        if not created:
            game_statistic.attempts = attempts
            game_statistic.hints = hints
            game_statistic.entered_words = words
            game_statistic.guessed = guessed
            game_statistic.save()

        return JsonResponse({"message": "success"}, status=200)
    else:
        return JsonResponse({"message": "error"}, status=400)
    
csrf_exempt  
def get_hint_view(request):
    most_close_word_number = int(request.GET.get("most_close_word_number"))
    word_to_guess = request.GET.get("current_word")
    word, closeness = get_hint(most_close_word_number, word_to_guess)
    
    return JsonResponse({"closeness": closeness, "word": word}, status=200)
    
@csrf_exempt
def update_user_rating(request):
    quantity = request.GET.get("rating_quantity")
    profile = Profile.objects.get(user=request.user)
    profile.rating = F('rating') + quantity
    profile.save()
    
    return JsonResponse({"message": "success"}, status=200)
    
@csrf_exempt    
def add_games_quantity(request):
    profile = Profile.objects.get(user=request.user)
    profile.games_played = F('games_played') + 1
    profile.save()
    return JsonResponse({"message": "success"}, status=200)

@csrf_exempt    
def get_top_list(request):
    top_users = Profile.objects.select_related('user').order_by('-rating')[:10]  # get top 10 users
    data = []
    for profile in top_users:
        data.append({
            'username': profile.user.username,
            'rating': profile.rating,
            'games_played': profile.games_played
        })
    return JsonResponse({'top_users': data})
    

@csrf_exempt    
def get_random_training_word(request):
    folder_path = r'D:\4_SEM\CourseWork\server\game\game_files'  # replace with the actual path to your folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    random_file = random.choice(files)
    word = random_file.split('_')[-1].split('.')[0]
    return JsonResponse({'word': word})
    