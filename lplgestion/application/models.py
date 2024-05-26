from django.db import models
from authentication.models import Joueur


class Jeu(models.Model):
    class CATEGORIE(models.TextChoices):
        ACTION = 'ACT'
        SPORT = 'SPO'
        RPG = 'RPG'
        RTS = 'RTS'
        FPS = 'FPS'
        MOBA = 'MOB'
        PARTY = 'PAR'
        SIMULATION = 'SIM'
        ARCADE = 'ARC'
        COMBAT = 'COM'
        SANDBOX = 'SAN'
        AVENTURE = 'AVE'
        GESTION = 'GES'
        AUTRES = 'AUT'

    SOLO = 'solo'
    EQUIPE = 'equipe'
    TYPE_JEU_CHOICES = [
        (SOLO, 'Solo'),
        (EQUIPE, 'Equipe'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    game_image = models.ImageField(upload_to='game_images/', blank=True, null=True)
    categorie = models.CharField(choices=CATEGORIE.choices, max_length=3)
    type_jeu = models.CharField(max_length=10, choices=TYPE_JEU_CHOICES, default=EQUIPE)
    lien = models.URLField(blank=True, null=True)

class Tournoi(models.Model):
    class TYPE_TOURNOI(models.TextChoices):
        EN_LIGNE = 'online', 'En ligne'
        EN_PRESENTIEL = 'offline', 'En présentiel'

    nom = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    jeux = models.ManyToManyField(Jeu, related_name='tournois_jeux', blank=True)
    jeuxpool = models.ManyToManyField(Jeu, related_name='tournois_jeuxpool', blank=True)
    joueurs_inscrits = models.ManyToManyField(Joueur, related_name='tournois_inscrits', blank=True, null=True)
    joueurs_selectionnes = models.ManyToManyField(Joueur, related_name='tournois_selectionnes', blank=True, null=True)
    type_tournoi = models.CharField(max_length=7, choices=TYPE_TOURNOI.choices, default=TYPE_TOURNOI.EN_LIGNE)


class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    joueurs = models.ManyToManyField(Joueur)
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} - {self.tournoi.nom}'


class Vote(models.Model):
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Partie(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    joueur1 = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='parties_joueur1', blank=True, null=True)
    joueur2 = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='parties_joueur2', blank=True, null=True)
    equipe1 = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='parties_equipe1', blank=True, null=True)
    equipe2 = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='parties_equipe2', blank=True, null=True)
    score_joueur1 = models.IntegerField(blank=True, null=True)
    score_joueur2 = models.IntegerField(blank=True, null=True)
    score_equipe1 = models.IntegerField(blank=True, null=True)
    score_equipe2 = models.IntegerField(blank=True, null=True)
    vainqueur_joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='parties_gagnees_joueur', blank=True, null=True)
    vainqueur_equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='parties_gagnees_equipe', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.jeu.type_jeu == Jeu.SOLO:
            return f'{self.joueur1.username} vs {self.joueur2.username} - {self.jeu.nom}'
        else:
            return f'{self.equipe1.nom} vs {self.equipe2.nom} - {self.jeu.nom}'


class HautFait(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    xp = models.IntegerField()

