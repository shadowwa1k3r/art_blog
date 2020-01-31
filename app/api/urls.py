from django.urls import include, path

urlpatterns = [
    path('profile/', include('app.api.profile.urls')),
]