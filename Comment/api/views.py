from rest_framework import viewsets, permissions
from .serializers import *


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('id')


class CommentLikeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all().order_by('id')
