from django.db.models. signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
from members.models import Subscriber
from .models import Article

from task.errands import new_blog_update

@receiver(post_save, sender=Article)
def new_blog_signal(sender, instance, created, **kwargs) :
    if created:
        new_blog_update.delay()
        pass
        



