from django.urls import path

from .views import LoginView, RegisterView, LogoutView, ChangePasswordView, GetUserView


urlpatterns = [
    path('', GetUserView.as_view(), name='get-user'),
    path('login', LoginView.as_view(), name="user-login"),
    path('signup', RegisterView.as_view(), name="user-signup"),
    path('logout', LogoutView.as_view(), name="user-logout"),
    path('change/password', ChangePasswordView.as_view(), name="user-change-password")
]