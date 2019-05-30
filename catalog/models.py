from django.db import models

# Create your models here.

class Genre(models.Model):
    """
    Model representing a game genre.
    """
    name = models.CharField(max_length=200, help_text="Enter a game genre")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
		
		
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Game(models.Model):
    """
    Model representing a game.
    """
    title = models.CharField(max_length=200)
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because game can only have one studio, but studios can have multiple games
    # Studio as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the game")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this game")
    # ManyToManyField used because genre can contain many games. Games can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular game instance.
        """
        return reverse('game-detail', args=[str(self.id)])
		

		
		
class Studio(models.Model):
    """
    Model representing a studio.
    """
    first_name = models.CharField(max_length=100)
   
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular studio instance.
        """
        return reverse('studio-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.first_name
		

		


	
