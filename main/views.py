from django.shortcuts import render
from .forms import *
# Create your views here.


def home(request):
    return render(request, "main/home.html")



def contactus(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, "main/contact.html", context)



def aboutus(request):
    return render(request, "main/about.html")