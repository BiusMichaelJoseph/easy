
from django.urls import path
from .views import PostCreateView, LikeCreateView, CommentCreateView, ShareCreateView, BookmarkCreateView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='create-post'),
    path('like/create/', LikeCreateView.as_view(), name='create-like'),
    path('comment/create/', CommentCreateView.as_view(), name='create-comment'),
    path('share/create/', ShareCreateView.as_view(), name='create-share'),
    path('bookmark/create/', BookmarkCreateView.as_view(), name='create-bookmark'),
]
