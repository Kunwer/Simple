from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peer_id = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.user.username}'
