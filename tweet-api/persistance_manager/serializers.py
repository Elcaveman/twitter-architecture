from .models import Geo, Media, Tweet , User
from rest_framework import serializers

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['url','place_id','country','lon','lat']

class MediaSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()#in octet
    type = serializers.SerializerMethodField()
    class Meta:
        model = Media
        fields = ['url','file_path','media_deep_link','tweet','size','type']
    def get_size(self,obj):
        return obj.size
    def get_type(self,obj):
        return obj.type

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','name']

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'url','geo','reply_settings','text','user_id','hidden','retweeted_by','liking_users']
        read_only_fields = ['direct_message_deep_link']
