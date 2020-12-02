# -*- coding: utf-8 -*-
from classe import bibliotheque, utilisateur

joueur = None
librairie = None


def initialisation_informations():
    global librairie
    librairie = bibliotheque.Bibliotheque("Application", "fichier/themes.csv")


def initialisation_joueur():
    global joueur
    pseudo = input("Bonjour. Veuillez entrez votre pseudo : ")
    joueur = utilisateur.Utilisateur(pseudo)
