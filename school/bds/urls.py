from django.urls import path,include
from . import views
urlpatterns = [

    path('index.html', views.index, name='index.html'),
]