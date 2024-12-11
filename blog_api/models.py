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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.IntegerField()  # The ID of the saved post from WordPress
    title = models.CharField(max_length=255)
    url = models.URLField()
    def __str__(self):
        return self.title
