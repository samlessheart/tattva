from django.contrib.auth import get_user_model
CustomUser = get_user_model()
from members.models import Subscriber
from django.core.mail import send_mail
from time import sleep

from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    
    print('task running')
    sleep(10)
    
    subject = 'testing sent from django localhost'
    message = 'testing sent from django localhose'
    
    send_mail (
        subject, message,  'cyrilekta@gmail.com', ['samlessheart@gmail.com', 'cyrilekta@gmail.com']
    )
    print('email sent')


@shared_task(bind=True)
def hello_test(self):
    sleep(0.1)
    print("hello task has been executed")



@shared_task(bind=True)
def new_blog_update(self):
    subject = 'New Blog has Been posted'
    message = """Hi subscriber, 
        We have just uploaded a new blog to  our site we would really appreciate if you would give it a read.
        Please click here if you do not want to recieve further updates
        """
    from_email = 'cyrilekta@gmail.com'
    send_to_list =  ['samlessheart@gmail.com', 'cyrilekta@gmail.com']

    send_mail(subject, message, from_email, send_to_list)

