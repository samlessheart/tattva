from django.urls import path, include
from .views import *


urlpatterns = [
    path('blogs/', blogs, name = "blogs"),
    path('blogdetail/<int:pk>', blogdetail, name = "blogdetail"),
    
]
