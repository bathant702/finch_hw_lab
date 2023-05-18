from django.contrib import admin
from .models import Bird, Feeding, Toy #import models so app knows to call

# Register your models here.
admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(Toy)