from rest_framework import generics

from app.models import Post
from app.serializer import PostSerializer

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer