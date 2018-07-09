from django.contrib import admin

# Register your models here.
from hackday_project.models import Family, Grocery

admin.site.register(Family)
admin.site.register(Grocery)