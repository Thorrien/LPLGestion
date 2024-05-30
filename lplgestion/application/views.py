from django.shortcuts import render
from authentication.models import Joueur
from application.models import Jeu


# Create your views here.
def home(request):
    return render(request, 'home.html')


def games(request):
    games = Jeu.objects.all()
    return render(request, 'games.html', {'games': games})