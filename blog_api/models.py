
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post_id = models.IntegerField()  # ID of the associated WordPress post
    user_name = models.CharField(max_length=100)  # Commenter's name
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the comment

    def __str__(self):
        return f"Comment by {self.user_name} on post {self.post_id}"



class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_posts")
    post_id = models.CharField(max_length=100)  # WordPress post ID
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # Optional
    link = models.URLField()  # WordPress post link
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} saved by {self.user.username}"
