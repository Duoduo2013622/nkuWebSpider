from django.db import models

# Create your models here.

class NewsInfoManager(models.Manager):
    pass

class NewsInfo(models.Model):
    title = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    pub_date=models.CharField(max_length=13)

    news = NewsInfoManager()

