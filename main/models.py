from django.db import models

# Create your models here.


class Daily_thought(models.Model):
    suvichar= models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    