from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

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

class Feeding(models.Model): 
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0], #sets default value to 'B'
    )

    #create a bird_id FK
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE) # this needs to be after Bird model in order for the variable to be defined

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
