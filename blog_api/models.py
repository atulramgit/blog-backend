
from django.db import models

class Comment(models.Model):
    post_id = models.IntegerField()  # ID of the associated WordPress post
    user_name = models.CharField(max_length=255)  # Commenter's name
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the comment

    def __str__(self):
        return f"Comment by {self.user_name} on post {self.post_id}"
