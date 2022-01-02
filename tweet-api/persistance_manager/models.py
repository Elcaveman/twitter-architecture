from django.db import models
import uuid
from consistency_manager.views import media_api_view,user_api_view,jwt_api_view
# Create your models here.
class Tweet(models.Model):
    direct_message_deep_link = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         unique= True,
         editable = False)
    geo = models.ForeignKey("persistance_manager.Geo", on_delete=models.CASCADE)
    reply_settings = models.CharField(max_length=30)
    hidden = models.BooleanField(default=False)
    text = models.TextField()
    user_id = models.ForeignKey("persistance_manager.User",on_delete=models.CASCADE,related_name="owner")
    retweeted_by = models.ManyToManyField("persistance_manager.User",related_name="retweeted_by")
    liking_users = models.ManyToManyField("persistance_manager.User",related_name="liking_users")
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
    
    def __str__(self):
        return self.direct_message_deep_link
    def save(self,*args,**kwargs):
        print("Tweet Service")
        print("Calling: Tweet Visibility")
        #call hide tweet
        print("Action: Saving Tweet:"+str(self.direct_message_deep_link)+" User:"+str(self.user_id))
        super().save(*args,**kwargs) 

class Geo(models.Model):
    place_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    country = models.CharField(max_length=40)
    lon = models.FloatField()
    lat = models.FloatField()
    class Meta:
        verbose_name = "Geo"
        verbose_name_plural = "Geo"
    def __str__(self):
        return self.country+"{"+str(self.lat)+","+str(self.lon)+"}" 

class Media(models.Model):
    """Model definition for Media."""
    media_deep_link = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         unique= True,
         editable = False)
    tweet = models.ForeignKey("persistance_manager.Tweet", on_delete = models.CASCADE)
    file_path = models.FileField(verbose_name='File',upload_to="uploads/")
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return self.media_deep_link
    @property
    def size(self):
        x = self.file_path.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
        
    @property
    def type(self):
        extension = self.file_path.path.split('.')[-1]
        return extension
        
    def save(self,*args,**kwargs):
        print("Calling: Media-Service")
        print("Action: Saving Media:"+self.media_deep_link+"\n\tTweet: "+self.tweet.pk)
        media_api_view({"method":"POST","data":self})
        super().save(self,*args,**kwargs)

class User(models.Model):
    username = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.username



    