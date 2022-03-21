from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_home, name='index_home'),
    path('exibe', views.exibe_home, name='exibe_home'),
]