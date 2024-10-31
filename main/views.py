from django.shortcuts import render

# Create your views here.

def home(request):
    loop_ls = [i for i in range(6)]
    context = {'loop_ls': loop_ls}
    return render(request, "main/home.html", context)



def contactus(request):
    form = "form"
    context = {'form': form}
    return render(request, "main/contact.html", context)



def aboutus(request):
    return render(request, "main/about.html")