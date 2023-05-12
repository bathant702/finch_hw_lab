from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #think of this as the controller.
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'), # route to details page
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'), # route to creat page
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'), #route to update
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'), #route to delete

]