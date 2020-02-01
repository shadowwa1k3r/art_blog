from django.urls import path

from app.api.profile.views import BackgroundImageUpdateView, ProfilePhotoUpdateView, FollowBlockApiView

urlpatterns =[
    path('background/', BackgroundImageUpdateView.as_view(), name='background-image-upload-api'),
    path('photo/', ProfilePhotoUpdateView.as_view(), name='profile-photo-upload-api'),
    path('follow/', FollowBlockApiView.as_view(), name='follow-block-api'),
]
