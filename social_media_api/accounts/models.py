from django.db import models
from django.contrib.auth.models import AbstractUser
#configuring user authenthication
# create a custom user model

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return self.username
