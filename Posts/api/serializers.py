from rest_framework import serializers, exceptions
from Posts.models import Topic, Post, Like, Choice, Vote, LikeCount
from UserManagement.api.serializers import UserProfileSerializer


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
    votes_percentage = serializers.SerializerMethodField()
    choice_details = ChoiceSerializer(source='choice', read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'

    def get_votes_percentage(self, obj):
        return obj.get_vote_percentage()


class PostSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True)
    topic_details = TopicSerializer(source='topic', read_only=True)
    user_data = UserProfileSerializer(source='user_profile', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
