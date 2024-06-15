import datetime
from django.conf import settings
from django.shortcuts import render, redirect
import pytz
from users.forms import RegisterForm
from users.models import FAQ, CustomUser, OtpToken, Profile
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session



def index(request):
    return render(request, "index.html")


@csrf_exempt
def signup(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()  # Сохранение пользователя в базе данных
        Profile.objects.create(user=user, games_played=0, rating=0)  # Create a new Profile instance
        return JsonResponse({'status': 'uccess', 'essage': 'Регистрация прошла успешно'}, status=200)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'status': 'error', 'errors': errors}, status=400)


@csrf_exempt
def verify_email(request, username):
    user = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
        
    if user_otp.otp_code == request.POST['otp_code']:
        # checking for expired token
        if user_otp.otp_expires_at > timezone.now():
            user.is_active = True
            user.save()
            return JsonResponse({'status': 'success', 'message': 'Email verified successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'error': 'The OTP has expired, get a new OTP!'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'error': 'Invalid OTP entered, enter a valid OTP!'}, status=401)


@csrf_exempt
def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST["otp_email"]
        
        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            # email variables
            subject="Email Verification"
            message = f"""
                                Hi {user.username}, here is your OTP {otp.otp_code} 
                                it expires in 5 minute, use the url below to redirect back to the website
                                http://127.0.0.1:8000/verify-email/{user.username}
                                
                                """
            sender = "marat.shchur@gmail.com"
            receiver = [user.email, ]
        
        
            # send email
            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False,
                )
            
            return JsonResponse({'status': 'success', 'message': 'A new OTP has been sent to your email-address'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'error': 'This email doesn\'t exist in the database'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'error': 'Invalid request method'}, status=405)




@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['authenticated'] = True
            return JsonResponse({'status': 'success', 'session_id': request.session.session_key}, status=200)
        else:
            return JsonResponse({'status': 'error', 'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'error': 'Invalid request method'}, status=405)
    


@csrf_exempt
def check_session(request):
    """
    Проверяет, является ли сессия активной и валидной
    """
    session_id = request.session.session_key
    if not session_id:
        return JsonResponse({'error': 'No session ID provided'}, status=401)

    try:
        session = Session.objects.get(session_key=session_id)
    except Session.DoesNotExist:
        return JsonResponse({'error': 'Invalid session'}, status=401)

    # Проверяем, не истекла ли сессия
    session_expire_date = session.expire_date.astimezone(pytz.utc).replace(tzinfo=None)
    current_datetime = datetime.datetime.now()
    if session_expire_date < current_datetime:
        return JsonResponse({'error': 'Session has expired'}, status=401)

    # Проверяем, является ли сессия активной
    if not session.get_decoded().get('_auth_user_id'):
        return JsonResponse({'error': 'Session is not active'}, status=401)

    # Если сессия валидна, обновляем время жизни сессии
    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
    request.session.save()

    # Check if the user is an admin
    is_admin = request.user.is_staff

    # Возвращаем успешный ответ
    return JsonResponse({'message': 'Session is valid', 'username': request.user.username, 'is_admin': is_admin}, status=200)


@csrf_exempt
def get_profile_data(request):
    user = CustomUser.objects.get(username = request.GET.get('username'))
    profile = Profile.objects.get(user = user.id)
    
    return JsonResponse({'rating': profile.rating,'games_played': profile.games_played})


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        session_id = request.session.session_key
        if session_id:
            try:
                session = Session.objects.get(session_key=session_id)
                session.delete()
            except Session.DoesNotExist:
                pass
            logout(request)
            return JsonResponse({'status': 'success', 'message': 'Logged out successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'error': 'No session ID provided'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'error': 'Invalid request method'}, status=405)
    
    
    
def get_faq_answers(request):
    faq_items = FAQ.objects.all()
    answers = []
    for item in faq_items:
        answers.append({'question': item.question, 'answer': item.answer})
    return JsonResponse({'answers': answers})