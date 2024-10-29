from django.shortcuts import render
from post.models import Post
from rest_framework import viewsets
from post.serializers import PostSerializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
        
        
