from django.db import models
from title.models import Title
from django.contrib.auth.models import User


class Post(models.Model):

    postUser = models.ForeignKey(User)
    postTitle = models.ForeignKey(Title)

    postText = models.TextField(max_length=2000)

    postCreatedAt = models.DateTimeField(auto_now_add=True)
    postUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.postText

class PostText(models.Model):

    postTextPost = models.ForeignKey(Post)

    postTextText = models.TextField(max_length=2000)

    postTextCreatedAt = models.DateTimeField(auto_now_add=True)
    postTextUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.postTextText