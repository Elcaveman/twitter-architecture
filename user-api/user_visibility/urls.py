from django.urls import path
from .views import *
urlpatterns = [
    path("users/<int:user_id>/interactions/enable/<str:interaction>/",enableInteraction),
    path("users/<int:user_id>/interactions/disable/<str:interaction>/",disableInteraction),
    path("users/<int:user_id>/visibility/",changeAccountVisibility)
]
