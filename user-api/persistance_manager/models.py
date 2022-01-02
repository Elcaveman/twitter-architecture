from django.db import models
import uuid
from consistency_manager.views import media_api_view, tweet_api_view,jwt_api_view
# Create your models here.
r={"method":"GET"}
class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    bio = models.TextField()
    liked_tweets = models.ManyToManyField("persistance_manager.Tweet",blank=True,related_name="liked_tweets")
    following = models.ManyToManyField("self",blank=True,related_name="following")
    retweets = models.ManyToManyField("persistance_manager.Tweet",blank=True,related_name="retweets")
    blocked = models.ManyToManyField("self",blank=True,related_name="blocked")
    account_visibility = models.CharField(max_length=100,blank=True)
    disabled_interactions = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return str(self.username)
class Tweet(models.Model):
    direct_message_deep_link = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         unique= True,
         editable = False)
    text = models.TextField()
    user_id = models.ForeignKey("persistance_manager.User",on_delete=models.CASCADE,related_name="owner")
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
    
    def __str__(self):
        return "TweetLink:"+str(self.direct_message_deep_link)
    def save(self,*args,**kwargs):
        print("Fetching Tweet Service")
        tweet_api_view(r)
        print("Action: Saving Tweet to Cache"+str(self.direct_message_deep_link)+" User:"+str(self.user_id))
        super().save(*args,**kwargs) 

