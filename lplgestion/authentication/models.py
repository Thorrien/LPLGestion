from django.db import models
from django.contrib.auth.models import AbstractUser


class Joueur(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    wins= models.IntegerField(default=0)
    matchs= models.IntegerField(default=0)
    tournois= models.IntegerField(default=0)

    def __str__(self):
        return self.username