from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView
from .forms import CommentForm, ArticleForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json



class PostListView(ListView):
	model = Article
	template_name = 'blog/blog_home.html'
	context_object_name = 'posts'
	ordering = ['created_on']
	paginate_by = 4




def blogdetail(request, pk):

    post = Article.objects.get(pk=pk)
    context = {'post':post}
    context['comments']= Comment.objects.filter(post= post ).order_by('-date_posted')
    return render(request, 'blog/blog_detail.html', context)


@login_required
def submitcomment(request):    
    data = json.load(request)
    
    if request.method == "POST" :
        post = Article.objects.get(pk=data.get("post_id"))
        content = data.get("content")
        comment = Comment.objects.create(post=post, author=request.user, content=content)

        response_data = {
            "id": comment.id,
            "content": comment.content,
            "date_posted":comment.date_posted            
        }
        return JsonResponse(response_data)
    
    return JsonResponse({"error": "Invalid request"}, status=400)



def add_blog(request):
     form = ArticleForm()
     context = {'form' : form}
     if request.method == "POST" :
          form = ArticleForm(request.POST)
          if form.is_valid():
               form.save()

               return redirect('blog_home' )

     return render(request, 'blog/add_blog.html', context)