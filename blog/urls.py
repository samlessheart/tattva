from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', PostListView.as_view(), name = "blog_home"),
    path('blog_detail/<int:pk>', blogdetail, name = "blog_detail"), 
    path('submit_comment/', submitcomment, name = "submit_comment"),    
    path('add_blog/', add_blog, name = "add_blog"),
    
    
]