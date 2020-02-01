from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Post, PostImage, PostLike, Comment


class PostCreateApiView(APIView):
    def post(self, request):
        p = Post(author=request.user)

        if(request.data['title']):
            title = request.data.get('title')
            p.title = title
            p.save()
        if (request.data['content']):
            content = request.data.get('content')
            p.content = content
            p.save()
        if (request.data['image']):
            p.save()
            images = request.data.getlist('image')
            for img in images:
                pi = PostImage.objects.create(post=p)
                pi.image.save(img.name, img, save=True)
                pi.save()
        return Response(status=200)


class PostLikeApiView(APIView):
    def post(self, request):
        if PostLike.objects.filter(post_id=request.data['post_id'], author=request.user).count() == 0:
            pl = PostLike.objects.create(post_id=request.data['post_id'], author=request.user)
            pl.save()
            return Response(status=200, data={'count': PostLike.objects.all().filter(post_id=request.data['post_id']).count()})
        return Response(status=400)


class PostCommentApiView(APIView):
    def post(self, request):
        if len(request.data['comment']) > 0:
            c = Comment.objects.create(post_id=request.data['post_id'], author=request.user, content=request.data['comment'])
            return Response(status=200, data={'comment': c.content, 'date': c.created_at, 'author': c.author.get_full_name(), 'photo': c.author.profile.photo.url, 'count': Comment.objects.all().filter(post_id=request.data['post_id']).count()})
        return Response(status=400)
