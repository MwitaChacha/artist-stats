from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    spotify = models.CharField(max_length=2000,null=True)
    youtube = models.CharField(max_length=2000,null=True)
    tiktok = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.name 