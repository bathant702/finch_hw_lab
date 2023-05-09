from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #think of this as the controller.
    path('about/', views.about, name='about'),

]