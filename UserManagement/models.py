from django.db import models
from django.contrib.auth.models import User
from util.choices import GENDER_CHOICES


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    selected_topics = models.ManyToManyField("Posts.Topic")
    objects = models.Manager()

    def __str__(self):
        return self.username

    def follow(self, user):
        self.followers.add(user)

    def unfollow(self, user):
        self.followers.remove(user)
