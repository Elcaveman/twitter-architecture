from django.urls import path
from .views import *
urlpatterns = [
    path("users/create/",wizzardCreate),
    path("users/validate/<str:validationToken>/",wizzardValidate),
    path("users/activate/<int:user_id>/",wizzardUpgrade)
]
