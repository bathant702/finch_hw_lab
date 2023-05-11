from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bird

# Create your views here.
# class based requests
class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age'] # what fields are displayed from the model and in what order
    success_url = '/birds/{bird_id}' # <--- must specify an exact ID
    # Or..more fitting... you want to just redirect to the index page
    # success_url = '/birds'


# function based requests
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
