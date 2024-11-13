from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from .models import Comment
from .serializers import CommentSerializer

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
    