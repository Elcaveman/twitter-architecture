from django.http.response import JsonResponse
from django.shortcuts import render
from random import choice
# Create your views here.

def wizzardCreate(request):
    print('creating user...')
    print('Awaiting Validation, the account will be deleted after 48hrs')

def wizzardValidate(request,validationToken):
    if request.method =="POST":
        print('checking if the user is Valid...')
        c=choice([True,False])
        if c:
            print('Token is Valid!')
            return JsonResponse({"valid":True})
        else:
            print('Invalid Token Try again!')
            return JsonResponse({"valid":False})

def wizzardUpgrade(request,user_id):
    if request.method =="POST":
        print('Upgrading the user model...')
        c=choice([True,False])
        if c:
            print('Congrats you\'re VIP now')
            return JsonResponse({"vip":True,"user_id":user_id})
        else:
            print('Something went wrong')
            return JsonResponse({"vip":False})