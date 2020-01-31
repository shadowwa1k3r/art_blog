from django.urls import path
from app import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('auth/', views.AuthPageView.as_view(), name='auth-page'),
    path('message/', views.MessagePageView.as_view(), name='message-page'),
    path('profile/my', views.MyProfilePageView.as_view(), name='my-profile-page'),
    path('profile/<str:username>', views.GuestProfilePage.as_view(), name='guest-profile-page'),
]
