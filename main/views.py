from django.shortcuts import render
from .models import Daily_thought
from datetime import datetime
from blog.models import Article

def home(request):
    loop_ls = [i for i in range(6)]
    context = {'loop_ls': loop_ls}
    today = datetime.today()
    try:
        today_thought = Daily_thought.objects.get(last_used= today)
    except:
        today_thought = Daily_thought.objects.all().order_by('last_used').first()
    context['today_thought'] =  today_thought
    blogs = Article.objects.all()
    context['blogs'] = blogs

    return render(request, "main/home.html", context)



def contactus(request):
    form = "form"
    context = {'form': form}
    return render(request, "main/contact.html", context)



def aboutus(request):
    return render(request, "main/about.html")