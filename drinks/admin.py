from .models import *
from django.contrib import admin
class DrinkAdmin(admin.ModelAdmin):
    list_display=['id','name','description',"created_at","updated_at"]


admin.site.register(Drink,DrinkAdmin)
