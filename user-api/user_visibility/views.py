from django.http.response import JsonResponse
from django.shortcuts import render
from persistance_manager.models import User
from django.http import JsonResponse
from consistency_manager.views import jwt_api_view
# Create your views here.
r = {"method":"GET"}
def enableInteraction(request,user_id,interaction):
    jwt_api_view(r)
    print("User Service :" + interaction)
    print("Enabeling Interaction :" + interaction)
    u = User.objects.get(id=user_id)
    lis = u.disabled_interactions.split(",")
    for i in range(len(lis)):
        if lis[i] == interaction:
            print("Interaction Already Enabled")
            return JsonResponse({"interaction":interaction,"user":user_id})
    u.disabled_interactions += ","+interaction
    print("Interaction Enabled successfully")
    return JsonResponse({"interaction":interaction,"user":user_id})

def disableInteraction(request,user_id,interaction):
    jwt_api_view(r)
    print("User Service :" + interaction)
    print("Enabeling Interaction :" + interaction)
    u = User.objects.get(id=user_id)
    lis = u.disabled_interaction.split(",")
    for i in range(len(lis)):
        if lis[i] == interaction:
            lis.pop(i)
    u.disabled_interaction = ','.join(lis)
    print("Interaction Disabled successfully")
    return JsonResponse({"interaction":interaction,"user":user_id})

def changeAccountVisibility(request,user_id,config):
    jwt_api_view(r)
    u = User.objects.get(id=user_id)
    print("updating visibility settings")
    u.account_visibility = config
    print("visibility updated!")
    return JsonResponse({"account_visibility":config})