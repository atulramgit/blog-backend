from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import SavedPost
from .serializers import SavedPostSerializer

class SavePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['user'] = request.user.id  # Attach logged-in user

        serializer = SavedPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        saved_posts = SavedPost.objects.filter(user=request.user)
        serializer = SavedPostSerializer(saved_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
    