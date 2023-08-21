from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
urlpatterns = [
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('Posts.api.urls')),
    path('comments/', include('Comment.api.urls')),
    # path(r'^relationship/', include('Relationship.urls')),
    # path(r'^rewards/', include('Rewards.urls')),
    path(r'usermanagement/', include('UserManagement.api.urls')),

]

# admin.site.index_title = 'PollWork'
# admin.site.site_header = 'PollWork Dashboard'
# admin.site.site_title = 'PollWork'
