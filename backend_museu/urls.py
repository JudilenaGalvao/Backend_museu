from django.contrib import admin
from django.urls import path
from post.views import PostViewSet
from django.conf.urls import include
from user.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]