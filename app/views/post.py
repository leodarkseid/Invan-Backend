from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Post
from app.serializer import PostSerializer

class CreatePost(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrievePost(generics.RetrieveAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePost(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"success":"True","message":"Update successful"})
        else:
            return Response({"success":"False","message":"error updating post"})
        
class DestroyPost(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            post = Post.objects.get(id=pk)
            if post.user.id == request.user.id:
                self.perform_destroy(post)
                return Response({"success":True, "message":"message deleted"})
            else:
                return Response({"success":False, "message":"delete operation failed"})
        except ObjectDoesNotExist:
            return Response({"success":False, "message":"user does not exist"})
        
class RetrieveUserPosts(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        user_posts = Post.objects.filter(user=request.user.id)
        serializer = self.serializer_class(user_posts, many=True)
        return Response({"success":"True","post":serializer.data})

class LikePost()