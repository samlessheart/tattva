from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views.generic.edit import FormMixin
from django.urls import reverse


class PostListView(ListView):
	model = Article
	template_name = 'blog/blog_home.html'
	context_object_name = 'posts'
	ordering = ['created_on']
	paginate_by = 4




class PostDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentForm
	
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post= self.object,  ).order_by('-date_posted')
		
        return context
	
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()		
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.save()
        return super(PostDetailView, self).form_valid(form)
	
    def get_success_url(self):
        return reverse('article-Detail', kwargs={'pk': self.object.id})