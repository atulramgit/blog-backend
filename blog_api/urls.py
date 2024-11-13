from django.urls import path
from .views import PostList, PostDetail, CommentListCreateView

app_name = "blog_api"

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("", PostList.as_view(), name="listcreate"),
    path('comments/', CommentListCreateView.as_view(), name='comments-list-create')
]
