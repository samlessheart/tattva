from django.urls import path, include
from .views import *


urlpatterns = [
    path('forum/', forum_home, name = "forum_home"),
    path('add_forum/', add_forum, name = "add_forum"),
    path('forum_detail/<int:pk>/', forum_detail, name = "forum_detail"),
    
    
]