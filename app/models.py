from django.db import models

# Create your models here.

class Topic(models.Model):
        topic_name=models.CharField(max_length=40,primary_key=True)


class Webpage(models.Model):
        topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
        name=models.CharField(max_length=30)
        url=models.URLField()
        email=models.EmailField()
        
class Accessrecord(models.Model):
        name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
        author=models.CharField(max_length=30)
        date=models.DateField()
 