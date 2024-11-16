from django.db import models

# Create your models here.


class Daily_thought(models.Model):
    suvichar= models.CharField(max_length=300)
    author = models.CharField(max_length=300, default='Anonymous')
    used_count = models.IntegerField(default=0)
    last_used = models.DateField(null= True , blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
