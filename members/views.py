from django.shortcuts import render, redirect
from .models import Subscriber
# Create your views here.
from django.contrib import messages
from django.core.mail import send_mail
from task.errands import test_func, hello_test






def subsribe(request):
    email = 'cyrilekta@gmail.com'

    if Subscriber.objects.filter(email=email).exists():
        subs = Subscriber.objects.get(email=email)
        subs.is_active = True
        subs.save()
    else:
        subs = Subscriber.objects.create(email=email)
        
    return redirect('home')


def unsubscribe(request):
    if request.method == 'POST':
        email = (request.POST['email'])
        if Subscriber.objects.filter(email=email).exists():
            subs = Subscriber.objects.get(email=email)
            subs.is_active = False
            subs.save()
        else:
            subs = Subscriber.objects.create(email=email, is_active = False)
        
        messages.success(request, f'{email} is successfully unsubscribed...')

    return render(request, 'members/unsubscribe.html')



