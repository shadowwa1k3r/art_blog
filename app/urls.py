from django.urls import path
from app import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home-page'),
    path('auth/', views.AuthPageView.as_view(), name='auth-page'),
]
