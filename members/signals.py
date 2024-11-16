from django.db.models. signals import post_save
from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# CustomUser = get_user_model()
from .models import Subscriber, CustomUser

@receiver(post_save, sender=CustomUser)
def add_user_subscriber(sender, instance, created, **kwargs) :
    if created:
        email = instance.email

        Subscriber.objects.get_or_create(email = email)
        

