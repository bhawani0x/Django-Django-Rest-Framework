from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CommentLikeViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'comment_likes', CommentLikeViewSet)

urlpatterns = []+router.urls
