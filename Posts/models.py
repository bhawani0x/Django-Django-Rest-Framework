from django.db import models
from django.contrib.auth.models import User
from UserManagement.models import UserProfile


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # content_text = models.TextField(blank=True, null=True)  # text poll
    question = models.TextField(blank=True, null=True)
    content_image_url = models.URLField(blank=True, null=True)  # image poll
    content_video_url = models.URLField(blank=True, null=True)  # video poll
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def user_can_vote(self, user_profile):
        user_votes = user_profile.vote_set.all()
        vote_qs = user_votes.filter(poll=self)
        if vote_qs.exists():
            return False
        return True


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)


class LikeCount(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.post}  ==>  {self.count}"


class Choice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    # @property
    # def get_vote_count(self):
    #     return Vote.objects.filter(choice=self.choice_id).count()
    #
    # def get_vote_percentage(self):
    #     total_votes = self.get_vote_count
    #     total_votes_in_post = self.post.vote_set.count()
    #     if total_votes_in_post > 0:
    #         percentage = (total_votes / total_votes_in_post) * 100
    #         return round(percentage, 2)
    #     return 0

    def __str__(self):
        return self.choice.choice_text


class VoteCount(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.post}  ==>  {self.count}"
