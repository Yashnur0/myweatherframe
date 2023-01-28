
from django.urls import path
from . import djangoframe
  
urlpatterns = [
         path('', djangoframe.index),
]