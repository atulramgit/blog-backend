from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from .models import Comment, SavedPost
from .serializers import CommentSerializer, SavedPostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SavePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        post_id = request.data.get('post_id')
        title = request.data.get('title')
        url = request.data.get('url')

        # Check if the post is already saved
        if SavedPost.objects.filter(user=user, post_id=post_id).exists():
            return Response({"message": "Post already saved"}, status=400)

        saved_post = SavedPost(user=user, post_id=post_id, title=title, url=url)
        saved_post.save()

        # Serialize the saved post to return its details
        serializer = SavedPostSerializer(saved_post)

        return Response({"message": "Post saved successfully", "post": serializer.data}, status=201)
    
    def get(self, request):
        user = request.user
        saved_posts = SavedPost.objects.filter(user=user)
        
        # Serialize all saved posts for the user
        serializer = SavedPostSerializer(saved_posts, many=True)

        return Response(serializer.data)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save()
        
        
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    