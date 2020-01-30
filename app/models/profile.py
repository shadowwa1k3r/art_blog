from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

STATUS = (
    (0, _('BLOCKED')),
    (1, _('FRIEND')),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile/photos/', blank=True, null=True)
    background = models.ImageField(upload_to='profile/background/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        p.save()


class Relation(models.Model):
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    status = models.IntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'relations'

    def __str__(self):
        if self.status == 1:
            return self.follower.username + '->following->' +self.followed.username
        return self.follower.username + '<-block->' + self.followed.username
