from django.contrib.admin import ModelAdmin
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True)
    avatar = models.ImageField(upload_to='profile/', default='default.png')
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    raiting = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass

class UserRaiting(ModelAdmin):
    readonly_fields = ['raiting']
