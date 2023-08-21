from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from Posts.models import *
from .serializers import *
from UserManagement.models import UserProfile
from rest_framework.decorators import action


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Topic.objects.all().order_by('id')
    serializer_class = TopicSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = LikeSerializer
    queryset = Like.objects.all().order_by('id')

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        user_profile_id = self.request.data.get('user_profile')

        try:
            post = Post.objects.get(pk=post_id)
            user_profile = UserProfile.objects.get(pk=user_profile_id)

            existing_like = Like.objects.filter(post=post, user_profile=user_profile).first()
            like_count_instance, created = LikeCount.objects.get_or_create(post=post)

            if existing_like:
                if existing_like.is_liked:
                    existing_like.is_liked = False
                    like_count_instance.count -= 1
                    like_count_instance.save()
                    existing_like.save()
                    return Response({"detail": "Existing like removed."}, status=status.HTTP_200_OK)
                else:
                    existing_like.is_liked = True
                    like_count_instance.count += 1
                    like_count_instance.save()
                    existing_like.save()
                    return Response({"detail": "Existing like added."}, status=status.HTTP_200_OK)
            else:
                new_like = serializer.save(user_profile=user_profile)
                like_count_instance.count += 1
                like_count_instance.save()
                print("New like added.")
                return Response({"detail": "New like added."}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({"detail": "The specified post does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class LikeCountViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = LikeCountSerializer
    queryset = LikeCount.objects.all().order_by('post_id')


class ChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class VoteViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Vote.objects.all().order_by('id')
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        user_profile_id = self.request.data.get('user_profile')

        try:
            post = Post.objects.get(pk=post_id)
            user_profile = UserProfile.objects.get(pk=user_profile_id)
            existing_vote = Vote.objects.filter(post=post, user_profile=user_profile).first()
            vote_count_instance, created = VoteCount.objects.get_or_create(post=post)

            if not existing_vote:
                vote_count_instance.count += 1
                vote_count_instance.save()

        except Post.DoesNotExist:
            return Response({"detail": "The specified post does not exist."}, status=status.HTTP_400_BAD_REQUEST)
