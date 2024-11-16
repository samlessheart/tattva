from django.urls import path, include
from .views import *


urlpatterns = [
    
    path('subsribe/', subsribe, name = "subsribe"),
    path('unsubscribe/', unsubscribe, name = "unsubscribe"),
    
    
]