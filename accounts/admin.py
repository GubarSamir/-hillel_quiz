from django.contrib import admin

from .models import CustomUser, UserRaiting

admin.site.register(CustomUser, UserRaiting)
