from rest_framework import serializers, exceptions
from Posts.models import *
from UserManagement.api.serializers import UserProfileSerializer
from django.db.models import Sum


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class LikeCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeCount
        fields = "__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    choice_details = ChoiceSerializer(source='choice', read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'


class VoteCountSerializer(serializers.ModelSerializer):
    votes_percentage = serializers.SerializerMethodField()

    class Meta:
        model = VoteCount
        fields = '__all__'

    def get_votes_percentage(self, obj):
        total_votes = VoteCount.objects.filter(post=obj.post).aggregate(Sum('count'))['count__sum'] or 0
        if total_votes > 0:
            percentage = (obj.count / total_votes) * 100
            return round(percentage, 2)
        return 0.00


class PostSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True)
    topic_details = TopicSerializer(source='topic', read_only=True)
    user_data = UserProfileSerializer(source='user_profile', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
