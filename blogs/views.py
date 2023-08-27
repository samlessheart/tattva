from django.shortcuts import render
from blogs.models import Blog

# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, "blogs/home.html", context)


def blogdetail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {"blog":blog}   
    return render(request, "blogs/blogdetail.html", context)
