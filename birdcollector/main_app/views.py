from django.shortcuts import render
from .models import Bird

# Create your views here.
def home(request): #is this like the controllers, with the functions telling the urls (routers) what to do?
    return render(request, 'home.html')

def about(request): #is this like the controllers, with the functions telling the urls (routers) what to do?
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()# retrieves all birds from model
    return render(request, 'birds/index.html', {
        'birds': birds #calling back the model using the value of birds in the function
    })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)# retrieves bird detail via id
    return render(request, 'birds/detail.html', { #function calling page
        'bird': bird #calling back the model using the value of birds in the function
    })
