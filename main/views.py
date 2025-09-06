from django.shortcuts import render, redirect
from .models import Daily_thought
from datetime import datetime
from blog.models import Article
from .errands import get_daily_thought

def home(request):
    loop_ls = [i for i in range(6)]
    context = {'loop_ls': loop_ls}
    today = datetime.today()

    
    today_thought = get_daily_thought()

    print(today_thought)
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


def test_suvichar(request):
    get_daily_thought()
    return redirect('home')
