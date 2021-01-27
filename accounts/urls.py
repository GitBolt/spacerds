from django.urls import include, path
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.forms import CreateUserForm

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_complete.html"), name="password_reset_complete"),
]
