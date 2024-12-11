from rest_framework import serializers
from blog.models import Post
from .models import Comment
from .models import SavedPost

class SavedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPost
        fields = ['post_id', 'title', 'url']  # Specify the fields you want to include in the serialized data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "author", "excerpt", "content", "status")
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'user_name', 'content', 'created_at']
