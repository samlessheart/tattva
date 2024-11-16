from django.shortcuts import render
from .forms import ForumForm, ReplyForm
from .models import *
# Create your views here.


def forum_home(request):
    forum_list = Forum.objects.all()
    context = {"forum_list":forum_list}
    return render(request, "forum/forum_home.html", context)


def forum_detail(request, pk):
    forum = Forum.objects.get(id=pk)  
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply= form.save(commit= False)
            reply.created_by = request.user
            reply.forum = forum
            reply.save()

    reply_list = Forum_reply.objects.filter(forum = forum)  
    context = {"forum":forum, "reply_list":reply_list, 'form': ReplyForm()}
   
    return render(request, "forum/forum_detail.html", context)


def add_forum(request):
    form = ForumForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, "forum/add_forum.html", context)