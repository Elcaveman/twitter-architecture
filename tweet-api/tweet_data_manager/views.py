import requests
from django.shortcuts import render
#from rest_framework.renderers import TemplateHTMLRenderer
from persistance_manager.models import *
# from django.contrib import messages
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser,FileUploadParser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from persistance_manager import models
from consistency_manager.views import media_api_view,user_api_view,jwt_api_view

from persistance_manager.serializers import *
# Create your views here.
r = {"method":"GET"}

class TweetView(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication,]
    serializer_class = TweetSerializer
    http_method_names = ['get','post','put','delete','head']
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    queryset = Tweet.objects.all()
    #we would normally use full text search with Postgres (@) 
    search_fields = ['^text',]
    filter_fields = ('id','direct_message_deep_link','user_id','hidden')
    #permission_classes = (Perm,)
    def get_queryset(self):
        queryset = self.queryset
        print("Tweet Service..")
        print("Calling Token Provider...")
        jwt_api_view(r)
        print("Calling Media Service...")
        media_api_view(r)
        print("Calling User Service...")
        user_api_view(r)
        return queryset

class GeoView(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication,]
    serializer_class = GeoSerializer
    #permission_classes = (Perm,)
    queryset = Geo.objects.all()
    filter_fields = ('place_id','lon','lat','country')
    http_method_names = ['get','post','put', 'head']
    def get_queryset(self):
        print("Tweet Service")
        print("Calling Token Provider...")
        jwt_api_view(r)
        queryset = self.queryset
        return queryset

class MediaView(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication,]
    parser_classes = (MultiPartParser,FormParser,JSONParser,FileUploadParser)
    serializer_class = MediaSerializer
    #permission_classes = (Perm,)
    queryset = Media.objects.all()
    filter_fields = ('tweet','media_deep_link')
    http_method_names = ['get','post','put', 'head']
    def get_queryset(self):
        print("Calling Token Provider Service...")
        jwt_api_view(r)
        print("Calling Media Service...")
        media_api_view(r)
        return super().get_queryset()

class UserView(viewsets.ModelViewSet):
    #authentication_classes = [SessionAuthentication,]
    serializer_class = UserSerializer
    #permission_classes = (Perm,)
    queryset = User.objects.all()
    filter_fields = ('id','username','name')
    #http_method_names = ['get','post', 'head']
    http_method_names = ['get', 'head']
    def get_queryset(self):
        print("Tweet Service")
        print("Calling Token Provider...")
        jwt_api_view(r)
        print("Calling User Service...")
        queryset = self.queryset
        return queryset

