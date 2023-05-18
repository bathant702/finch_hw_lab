from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #think of this as the controller.
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    #bird path
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'), # route to details page
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'), # route to creat page
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='birds_update'), #route to update
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='birds_delete'), #route to delete
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'), #route to add new feeding to feeding model
    #toy path
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

]