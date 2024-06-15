from datetime import datetime, timedelta
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from game.main_functionality.word_processing import load_close_words
from game.models import DailyWord
from staff.additional_functions import create_word
from tournament.models import Tournament, TournamentWord
from users.models import Profile
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

@csrf_exempt
def users_list(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Only administrators can access this endpoint'}, status=403)

    top_users = Profile.objects.select_related('user').order_by('-rating')  # get top 10 users
    data = []
    for profile in top_users:
        data.append({
            'username': profile.user.username,
        })
    return JsonResponse({'users': data})

@csrf_exempt
@permission_required("is_admin")
def create_tournament(request):
    data = json.loads(request.body.decode("utf-8"))
    title = data["title"]
    description = data["description"]
    number_of_words = data["number_of_words"]
    start_date_time = datetime.fromisoformat(data["start_date_time"])
    start_date_time = timezone.make_aware(start_date_time, timezone.get_current_timezone())
    duration = timedelta(minutes=data["duration"]['minutes'])
    words = data["words"]

    end_date_time = start_date_time + duration
    tournament = Tournament(
        title=title,
        description=description,
        number_of_words=number_of_words,
        start=start_date_time,
        end=end_date_time,
        duration=duration
    )
    tournament.save()

    for round_number, word in words.items():
        tournament_word = TournamentWord(word=word, round_number=round_number, tournament=tournament)
        tournament_word.save()

    return JsonResponse({"message": "Tournament created successfully!"})


@csrf_exempt
def add_daily_word(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Only administrators can access this endpoint'}, status=403)

    word = request.POST.get("word")
    if create_word(word):
        game_number = DailyWord.objects.count() + 1
        date = datetime.now().date()
        guess_word = DailyWord(date=date, word=word, game_number=game_number)
        guess_word.save()
        return JsonResponse({'message': "success"}, status=200)
    
    else:
        return JsonResponse({'message': "Word doesn't exist"}, status=400)
                        
                        
@csrf_exempt
def download_word_files(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Only administrators can access this endpoint'}, status=403)

    word = request.POST.get("word")
    if create_word(word):
        return JsonResponse({'message': "success"}, status=200)
    
    else:
        return JsonResponse({'message': "Word doesn't exist"}, status=400)
                        
                   
@csrf_exempt
def get_all_tournaments(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Only administrators can access this endpoint'}, status=403)
    
    tournaments = Tournament.objects.all()
    response_data = [
        {
            "title": tournament.title,
            "number_of_rounds": tournament.number_of_words,
            "duration": int(tournament.duration.total_seconds() // 60)
        }
        for tournament in tournaments
    ]

    return JsonResponse({'data':response_data}, status = 200)