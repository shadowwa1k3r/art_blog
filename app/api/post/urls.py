from django.urls import path

from app.api.post.views import PostCreateApiView, PostLikeApiView, PostCommentApiView

urlpatterns = [
    path('create/', PostCreateApiView.as_view(), name='post-create-api'),
    path('like/', PostLikeApiView.as_view(), name='post-like-api'),
    path('comment/', PostCommentApiView.as_view(), name='post-comment-api'),
]
