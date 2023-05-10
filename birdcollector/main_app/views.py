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

#dummy data for birds
# birds = [
#     {'name': 'Finchie', 'breed': 'finch', 'description': 'small, with white underbelly and gray wings. finished off with a black trim.', 'age': 2},
#     {'name': 'Tweetie', 'breed': 'canary', 'description': 'yellow witha huge head', 'age': 1},
#     {'name': 'Murica', 'breed': 'eagle', 'description': 'with the color of freedom on its great wings of freedom', 'age': 200},
# ]
