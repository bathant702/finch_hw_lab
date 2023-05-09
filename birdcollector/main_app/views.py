from django.shortcuts import render

# Create your views here.
def home(request): #is this like the controllers, with the functions telling the urls (routers) what to do?
    return render(request, 'home.html')
