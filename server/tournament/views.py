from datetime import datetime, timedelta
import json
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from game.main_functionality.word_processing import get_word_closeness
from tournament.models import Message, Tournament, TournamentResult, TournamentWord, TournamentWordStatistic, TournmentParticipant

from users.models import CustomUser

@csrf_exempt
def upcoming_tournaments(request):
    upcoming_tournaments = Tournament.objects.filter(end__gt=datetime.now())
    data = []
    for tournament in upcoming_tournaments:
        data.append({
            'id': tournament.id,
            "title": tournament.title,
            "number_of_rounds": tournament.number_of_words,
            "duration": int(tournament.duration.total_seconds() // 60)
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def get_tournament_data(request, pk):
    tournament = Tournament.objects.get(pk=pk)
    data = {
        'title': tournament.title,
        'description': tournament.description,
        'number_of_words': tournament.number_of_words,
        'start': tournament.start,
        'duration': int(tournament.duration.total_seconds() // 60),
        'end': tournament.end,
        'words': [{'word': word.word, 'round_number': word.round_number, "word_id": word.id} for word in tournament.words.all()],
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def get_user_tournament_statistic(request, tournament_id):
    user_id = request.user.id
    tournament = Tournament.objects.get(id=tournament_id)
    user = TournmentParticipant.objects.get(user_id=user_id)
    statistic = TournamentWordStatistic.objects.filter(participant_id=user, tournament_id=tournament)
    data = [
        {
            'round_number': stat.tournament_word_id.round_number,
            'attempts': stat.attempts,
            'guessed': stat.guessed,
            'entered_words': stat.entered_words
        }
        for stat in statistic
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def save_statistic(request):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        tournament_id = data.get('tournament_id')
        round_number = data.get('round_number')
        word = data.get('word')
        attempts = data.get('attempts')
        entered_words = data.get('words')
        guessed = data.get('guessed')
        
        tournament = Tournament.objects.get(id=tournament_id)
        tournament_word = TournamentWord.objects.get(tournament=tournament, round_number=round_number, word=word)
        participant = TournmentParticipant.objects.get(user_id=request.user.id)
        
        statistic, created = TournamentWordStatistic.objects.get_or_create(
            tournament_id = tournament,
            tournament_word_id=tournament_word,
            participant_id=participant,
            defaults={
                'attempts': attempts,
                'entered_words': entered_words,
                'guessed': guessed
            }
        )

        if not created:
            statistic.attempts = attempts
            statistic.entered_words = entered_words
            statistic.guessed = guessed
            statistic.save()

        return JsonResponse({"message": "success"}, status=200)
    else:
        return JsonResponse({"message": "error"}, status=400)
    
@csrf_exempt
def guess_word(request):
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
def tournament_participant_stats(request, tournament_id):
    stats = TournamentWordStatistic.objects.filter(tournament_id=tournament_id)
    data = {}
    for stat in stats:
        if stat.guessed:
            username = stat.participant_id.user_id.username
            if username in data:
                data[username] += 1
            else:
                data[username] = 1
    return JsonResponse(list(data.items()), safe=False)


@csrf_exempt
def user_participate_in_tournament(request, tournament_id):
    try:
        participant = TournmentParticipant.objects.get(user_id=request.user.id, tournaments=tournament_id)
        has_statistic = True
    except TournmentParticipant.DoesNotExist:
        has_statistic = False
    return JsonResponse({"has_statistic": has_statistic})

@csrf_exempt
@require_http_methods(['POST'])
def participate_in_tournament(request, tournament_id):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)
    tournament = Tournament.objects.get(id=tournament_id)
    participant, created = TournmentParticipant.objects.get_or_create(user_id=user)
    if created:
        tournament.participants.add(participant)
        return JsonResponse({'message': 'Participation successful!'}, status=201)
    else:
        if participant in tournament.participants.all():
            return JsonResponse({'message': 'You are already participating in this tournament.'}, status=400)
        else:
            tournament.participants.add(participant)
            return JsonResponse({'message': 'Participation successful!'}, status=201)
    
    
@csrf_exempt
def save_completion_time(request, tournament_id):
    data = json.loads(request.body)
    completion_time = data.get('completion_time')
    if completion_time:
        participant = TournmentParticipant.objects.get(user_id=request.user.id)
        tournament = Tournament.objects.get(id=tournament_id)
        result, created = TournamentResult.objects.get_or_create(tournament=tournament, participant=participant)
        result.completion_time = completion_time
        result.save()
        return JsonResponse({'message': 'Completion time saved successfully'}, status=200)
    return JsonResponse({'message': 'Invalid request'}, status=400)


@csrf_exempt
def get_completion_time(request, tournament_id):
    participant = TournmentParticipant.objects.get(user_id=request.user.id)
    tournament = Tournament.objects.get(id=tournament_id)
    result = TournamentResult.objects.filter(tournament=tournament, participant=participant).first()
    if result:
        return JsonResponse({'completion_time': result.completion_time.isoformat() if result.completion_time else None}, status=200)
    return JsonResponse({'completion_time': None}, status=200)

@csrf_exempt
def update_tournament_scores(request):
    tournaments = Tournament.objects.filter(
        end__lte=timezone.now() + timedelta(hours=3),
        end__gt=timezone.now() - timedelta(minutes=1) + timedelta(hours=3)
    )    
    for tournament in tournaments:
        stats = TournamentWordStatistic.objects.filter(tournament_id=tournament.id)
        data = {}
        for stat in stats:
            username = stat.participant_id.user_id.username
            if stat.guessed:
                if username in data:
                    data[username] += 1
                else:
                    data[username] = 1
            else:
                if username not in data:
                    data[username] = 0
        
        participants = TournmentParticipant.objects.filter(tournaments=tournament)
        for participant in participants:
            username = participant.user_id.username
            score = data.get(username, 0)
            result, created = TournamentResult.objects.get_or_create(tournament=tournament, participant=participant)
            result.score = score
            if not result.completion_time:
                result.completion_time = timezone.now()
            result.save()
    
    for tournament in tournaments:
        TournamentResult.recalculate_places(tournament)
        
        for result in TournamentResult.objects.filter(tournament=tournament):
            user_email = result.participant.user_id.email
            message = Message(
                user=result.participant.user_id,
                title=f"Результаты турнира {tournament.title}",
                message=f"Вы заняли {result.place} место в турнире {tournament.title} с результатом {result.score}! Инструкции по получению награды будут высланы на ваш email: {user_email}",
                readed=False
            )
            message.save()
            
    return JsonResponse({"message": True})

@csrf_exempt
def new_messages(request):
    user = request.user.id
    unread_messages = Message.objects.filter(user=user, readed=False).exists()
    return JsonResponse({'new_messages': unread_messages})

@csrf_exempt
def get_all_messages(request):
    user_id = request.user.id
    messages = Message.objects.filter(user_id=user_id)
    message_list = []
    for message in messages:
        message_list.append({
            "id": message.pk,
            "title": message.title,
            "message": message.message,
            "readed": message.readed,
            "created_at": message.created_at.isoformat()
        })
    return JsonResponse({"messages": message_list})

@csrf_exempt
def mark_message_as_read(request, message_id):
    message = Message.objects.filter(id=message_id).first()
    if message:
        message.readed = True
        message.save()
        return JsonResponse({"success": True})        
