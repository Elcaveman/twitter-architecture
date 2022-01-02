from django.urls import path , include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets',views.TweetView)
router.register('media',views.MediaView)
router.register('geo',views.GeoView)
router.register('users',views.UserView)

urlpatterns = [
    path('',include(router.urls)),
]
