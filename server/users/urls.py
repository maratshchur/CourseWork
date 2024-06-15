from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.signup, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login", views.signin, name="signin"),
    path("check_session", views.check_session, name="check_session"),
    path("profile", views.get_profile_data, name="get_profile_data"),
    path("logout", views.logout_view, name = "logout"),
    path("faq", views.get_faq_answers, name = "faq")


]