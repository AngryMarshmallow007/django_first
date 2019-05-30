from django.contrib import admin

# Register your models here.

from .models import Studio, Genre, Game

#admin.site.register(Game)
#admin.site.register(Studio)
admin.site.register(Genre)

# Define the admin class
class StudioAdmin(admin.ModelAdmin):
  display = ('first_name')
  fields = ['first_name']
  

# Register the admin class with the associated model
admin.site.register(Studio, StudioAdmin)


# Register the Admin classes for Game using the decorator

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass