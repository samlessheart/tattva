from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()



class Blog(models.Model):
    name = models.CharField(max_length=100, )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog')
    video_link = models.CharField(max_length=100, blank= True , null=True)

    def __str__(self):
        return self.name