from django.db import models
from django.urls import reverse #to redirect back to initial page
from datetime import date #using a date check to figure out business logic

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS) #using sql logic to figure out if the meals are >= what they should be
    
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
    
    class Meta: #arranging the dates for feeding
        ordering = ['-date']
