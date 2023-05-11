from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #think of this as the controller.
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='details'), # route to details page
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'), # route to creat page

]