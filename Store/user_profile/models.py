from django.db import models
from mainpage.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='prfile')
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.username = self.user.username
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username