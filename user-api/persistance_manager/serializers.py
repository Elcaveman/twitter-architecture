from .models import *
from rest_framework import serializers

      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','name','birthday','bio',
        'liked_tweets','following','retweets','blocked',
        'account_visibility','disabled_interactions']

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'url','text','user_id']
        read_only_fields = ['direct_message_deep_link']
