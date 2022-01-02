from django.urls import path
from .views import *
urlpatterns = [
    path('tweets/<int:t_id>/hidden/',hideTweet)
]
