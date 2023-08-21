from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topics')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'likes', LikeViewSet, basename='likes')
router.register(r'likeCount', LikeCountViewSet, basename='likeCount')
router.register(r'choices', ChoiceViewSet, basename='choices')
router.register(r'votes', VoteViewSet, basename='votes')

urlpatterns = []+router.urls
