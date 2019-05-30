from django.shortcuts import render

# Create your views here.

from .models import Game, Studio, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_games=Game.objects.all().count()    
    num_studios=Studio.objects.count()  # The 'all()' is implied by default.
	
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
 # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_games':num_games,'num_studios':num_studios,'num_visits':num_visits}, # num_visits appended
    )
	
from django.views import generic

class GameListView(generic.ListView):
    model = Game

	
class GameDetailView(generic.DetailView):
    model = Game