from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True )
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


class Forum_reply(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE )
    reply_text = RichTextField(blank = True, null=True)
    created_by = models.ForeignKey(CustomUser,on_delete=models.SET_NULL , null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey("self", blank=True, null=True, default=None, on_delete=models.SET_NULL)




