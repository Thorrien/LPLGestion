from django.contrib import admin
from .models import Jeu, Tournoi, Equipe, Vote, Partie, HautFait


admin.site.register(Jeu)
admin.site.register(Tournoi)
admin.site.register(Equipe)
admin.site.register(Vote)
admin.site.register(Partie)
admin.site.register(HautFait)
