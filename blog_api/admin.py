
from django.contrib import admin
from .models import Comment, SavedPost

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post_id', 'created_at')
    search_fields = ('user_name', 'post_id')

@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'post_id', 'saved_at')
    search_fields = ('user__username', 'post_id', 'title')
