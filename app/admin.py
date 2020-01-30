from django.contrib import admin
from app import models

admin.site.register(models.Comment)
admin.site.register(models.CommentReply)
admin.site.register(models.PostLike)
admin.site.register(models.Post)
admin.site.register(models.Profile)
admin.site.register(models.Relation)
admin.site.register(models.PostView)
admin.site.register(models.PostImage)

