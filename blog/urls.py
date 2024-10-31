from django.urls import path, include
from .views import *


urlpatterns = [
    path('blog/', PostListView.as_view(), name = "blog_home"),
    
    
    
]