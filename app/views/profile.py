from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from app.models import Relation, Post


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):

        user_set = User.objects.filter(Q(Q(followed__follower=self.request.user) & Q(followed__status=1)) | Q(username=self.request.user.username))
        qs = Post.objects.filter(author__in=user_set)
        if Post.objects.filter(author=self.request.user).count() > 0:
            last = Post.objects.filter(author=self.request.user).order_by('-created_at').first()
            if last:
                qs = qs.exclude(id=last.id)
        return qs

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        if Post.objects.filter(author=self.request.user).count() > 0:
            last = Post.objects.filter(author=self.request.user).order_by('-created_at').first()
            context['last'] = last
        context['user'] = User.objects.get(username=self.request.user.username)
        context['follower_count'] = Relation.objects.filter(followed=self.request.user, status=1).count()
        context['following_count'] = Relation.objects.filter(follower=self.request.user, status=1).count()
        context['suggestions'] = User.objects.exclude(username=self.request.user.username)[:6]
        return context


class AuthPageView(View):
    def get(self, request):
        return render(request, template_name='auth/sign-in.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home-page'))

        return render(request, 'auth/sign-in.html', {'error': True})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('auth-page'))


class MyProfilePageView(LoginRequiredMixin, ListView):
    template_name = 'profile/my-profile-feed.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MyProfilePageView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(username=self.request.user.username)
        context['follower_count'] = Relation.objects.filter(followed=self.request.user, status=1).count()
        context['following_count'] = Relation.objects.filter(follower=self.request.user, status=1).count()
        context['followers'] = Relation.objects.filter(followed=self.request.user, status=1)[:6]
        context['followed'] = Relation.objects.filter(follower=self.request.user, status=1)[:6]
        return context


class GuestProfilePage(LoginRequiredMixin, ListView):
    template_name = 'profile/user-profile.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(GuestProfilePage, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])
        context['user'] = user
        context['follower_count'] = Relation.objects.filter(followed=user, status=1).count()
        context['following_count'] = Relation.objects.filter(follower=user, status=1).count()
        context['followers'] = Relation.objects.filter(followed=user, status=1)[:6]
        context['followed'] = Relation.objects.filter(follower=user, status=1)[:6]
        return context