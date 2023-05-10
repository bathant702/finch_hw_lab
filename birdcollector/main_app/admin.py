from django.contrib import admin
from .models import Bird #import Bird so it knows to call the model

# Register your models here.
admin.site.register(Bird)