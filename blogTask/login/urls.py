
from django.urls import path, include
from login.views import login_user

urlpatterns = [
    path('login_user', login_user, name='login_user'),
]
