from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name = "home"),
    path('contactus/', contactus, name = "contactus"),
    path('aboutus/', aboutus, name = "aboutus"),
    
]