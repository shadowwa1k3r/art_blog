from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Profile, Relation


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


class FollowBlockApiView(APIView):
    def post(self, request):
        t = User.objects.get(id=request.data['target'])
        status = request.data['status']
        if Relation.objects.filter(follower=request.user, followed=t).count() == 0:
            Relation.objects.create(status=status, follower=request.user, followed=t)
            return Response(status=200, data={'following': Relation.objects.filter(follower=request.user).count()})
        return Response(status=400)
