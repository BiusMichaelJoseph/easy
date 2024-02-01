
from django.urls import path
from .views import (
    PostListCreateView, LikeListCreateView, CommentListCreateView,
    ShareListCreateView, BookmarkListCreateView,
    PostDetailView, LikeDetailView, CommentDetailView,
    ShareDetailView, BookmarkDetailView,
)

urlpatterns = [
    # Create and List URLs
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('shares/', ShareListCreateView.as_view(), name='share-list-create'),
    path('bookmarks/', BookmarkListCreateView.as_view(), name='bookmark-list-create'),

    # Retrieve, Update, and Destroy URLs
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('shares/<int:pk>/', ShareDetailView.as_view(), name='share-detail'),
    path('bookmarks/<int:pk>/', BookmarkDetailView.as_view(), name='bookmark-detail'),
]

