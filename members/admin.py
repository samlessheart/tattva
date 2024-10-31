from django.contrib import admin
from django.contrib.auth import get_user_model
CustomUser = get_user_model()

from .models import Subscriber
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Subscriber)