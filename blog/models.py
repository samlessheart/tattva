from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank = True, null=True)
    author =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)



    @property
    def small_content(self):
        return self.content[0:100] + " ..."
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
