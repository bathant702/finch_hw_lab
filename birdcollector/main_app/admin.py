from django.contrib import admin
from .models import Bird, Feeding #import Bird, Feeding so it knows to call the model

# Register your models here.
admin.site.register(Bird)
admin.site.register(Feeding)