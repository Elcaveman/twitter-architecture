import requests
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser,FileUploadParser
from rest_framework.response import Response

MAX_RETRIES = 1  # number of times we want to try
def service_discovery(request):
    return {
        "tweet-service":"http://127.0.0.1:8000/api/v1/tweets/",
        "user-service":"http://127.0.0.1:8001/api/v1/users/",
        "token-provider":"",
        "media-api":"",
    }
def media_api_view(request):
    if request["method"] == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            r = requests.get("https://example.com/consumers", timeout=200)
            print("Waiting for Media-Service...")
            if r.status_code == 200:
                data = r.json()
                print("Media-Service: Data received")
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                print("Media-Service: request TimedOut")
        print("Media-Service: call failed")
        return Response({"error": "Request failed"}, status=r.status_code)
    elif request["method"] == "POST":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            r = requests.post("https://example.com/consumers", data={},timeout=200)
            print("Waiting for Media-Service...")
            if r.status_code == 200:
                data = r.json()
                print("Media-Service:Data uploaded successfully")
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                print("Media-Service: request TimedOut")
        print("Media-Service: call failed")
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

def tweet_api_view(request):
    TWITTER_SERVICES=service_discovery({})
    if request["method"] =="GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            r = requests.get(TWITTER_SERVICES["tweet-service"], timeout=200)
            print("Waiting for Tweet-Service...")
            if r.status_code == 200:
                data = r.json()
                print(data)
                print("Tweet-Service: Data received")
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                print("Tweet-Service: request TimedOut")
        print("Tweet-Service: call failed")
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

def jwt_api_view(request):
    if request["method"] == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            r = requests.get("https://example.com/consumers", timeout=200)
            print("Waiting for Token Provider...")
            if r.status_code == 200:
                data = r.json()
                print("Token Provider: Data received")
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                print("Token Provider: request TimedOut")
        print("Token Provider: call failed")
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


