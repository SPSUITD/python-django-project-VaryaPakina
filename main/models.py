from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Channel(models.Model):
  title = models.CharField(max_length=50)


class Message(models.Model):
  text = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
  user_to = models.ForeignKey(User, on_delete=models.CASCADE)
  publication_time = models.DateTimeField(auto_now_add=True)


class ChannelMessage(models.Model):
  text = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
  publication_time = models.DateTimeField(auto_now_add=True)
