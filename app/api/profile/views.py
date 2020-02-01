from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Profile


class BackgroundImageUpdateView(APIView):
    def post(self, request):
        f = request.data.get('background')
        p = Profile.objects.get(user=self.request.user)
        p.background.save(f.name, f, save=True)
        return Response(status=200)


class ProfilePhotoUpdateView(APIView):
    def post(self, request):
        f = request.data.get('profile')
        p = Profile.objects.get(user=self.request.user)
        p.photo.save(f.name, f, save=True)
        return Response(status=200)

