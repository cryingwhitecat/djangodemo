from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    Title = models.CharField(default="Cool Title",max_length=100)
    Abstract = models.CharField(default="Some Abstract",max_length=200)
    FullText = models.CharField("FullText",default='',max_length=1000)
    ImageUrl = models.CharField(default="#",max_length=100)
    PublishDate = models.DateTimeField('PublishDate',default=timezone.now())
    #endpoint to refer to the specific post, defaults to lowercase Title
    UrlTitle=models.CharField(max_length=100,primary_key=True,default = '')
    def __str__(self):
        return self.Title + ', was published at ' + str(self.PublishDate) + \
            ' API url: ' + self.UrlTitle
    def save(self, *args, **kwargs):
        self.UrlTitle ='_'.join(self.Title.lower().split(' '))
        print(self.UrlTitle)
        super().save(*args, **kwargs) 
