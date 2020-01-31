from django.contrib.auth.models import User
from django.db import models

from app.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.content


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='parent_comment')
    reply = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comment')

    class Meta:
        db_table = 'comment_replies'

    def __str__(self):
        return self.reply.content