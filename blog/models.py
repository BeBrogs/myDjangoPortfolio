from django.db import models
from datetime import date
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=25)
    myDate = models.DateTimeField()
    myPost = models.TextField(max_length = 300)
    mySnapshot = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def mySummary(self):
        return self.myPost[:80]


    def myTimeStamp(self):
        return self.myDate.strftime('%b %e %Y')
