from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Channel(models.Model):
    name = models.CharField(unique=True, max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(null=True, blank=True)
    channel_date = models.DateField(default=date.today)
    members = models.ManyToManyField(User, blank=True, related_name='members')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['channel_date']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} said {self.message}'

    class Meta:
        ordering = ['timestamp']

# class JoindChannel(models.Model):

#      members=models.ForeignKey(User, on_delete=models.CASCADE)
#      channel= models.ForeignKey(Channel, on_delete=models.CASCADE)
#       joind=models.BooleanField(default=False)