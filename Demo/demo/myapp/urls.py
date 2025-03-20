from django.urls import path 
from .migrations import views

from myapp import views

urlpatterns = [
    path("", views.home,name="home")
]
