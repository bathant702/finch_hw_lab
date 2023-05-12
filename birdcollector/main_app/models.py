from django.db import models
from django.urls import reverse

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): #this takes advantage of implementing an Update route
        return reverse('detail', kwargs={'bird_id': self.id})