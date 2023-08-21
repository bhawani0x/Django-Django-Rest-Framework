from rest_framework import serializers
from Comment.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    comment_like_count = serializers.SerializerMethodField()
    class Meta:
        model = CommentLike
        fields = '__all__'

    def get_comment_like_count(self, obj):
        return obj.comment.commentlike_set.count()
