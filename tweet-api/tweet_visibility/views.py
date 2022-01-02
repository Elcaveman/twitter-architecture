import requests
import time
from django.shortcuts import render
#from rest_framework.renderers import TemplateHTMLRenderer
from persistance_manager.models import *
from django.http import Http404
from consistency_manager.views import media_api_view,user_api_view,jwt_api_view
from django.http import JsonResponse
# Create your views here.
r = {"method":"GET"}

def hideTweet(request,t_id):
    print("calling Token Provider")
    jwt_api_view(r)
    print("calling User Service")
    user_api_view(r)
    try:
        q = Tweet.objects.get(id=t_id)
        q.hidden = not q.hidden
        print("Hidding the tweet...")
        q.save()
    except Tweet.DoesNotExist:
        raise Http404("Tweet does not exist")
    
    return JsonResponse({"hidden":q.hidden})
