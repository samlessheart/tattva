from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True,)
    is_active = models.BooleanField(default=True)




class CustomUser(AbstractUser):
    pass





