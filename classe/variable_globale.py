# -*- coding: utf-8 -*-

from classe import bibliotheque, utilisateur, theme

joueur = None
librairie = None
theme_courant = None


def initialisation_informations():
    """
    Permet d'initialiser l'objet Bibliotheque courant comprenant toutes les donnees de l'application.

    PRE : Nécessite l'existence de la classe Bibliotheque.
    POST : Instancie l'objet Bibliotheque dans la variale globale librairie.
    """
    global librairie
    librairie = bibliotheque.Bibliotheque("Application", "../ressources/themes.csv")


def initialisation_joueur():
    """
    Permet d'initialiser l'objet Utilisateur de l'utilisateur courant.

    PRE : Nécessite l'existence de la classe Utilisateur.
    POST : Instancie l'objet Utilisateur dans la variale globale joueur.
    """
    global joueur
    pseudo = input("Bonjour. Veuillez entrez votre pseudo : ")
    joueur = utilisateur.Utilisateur(pseudo)


def initialisation_theme(nom_du_theme):
    """
    Permet d'initialiser l'objet Theme courant.

    PRE : Nécessite l'existence de la classe Theme et une initialisation préalable de la classe Bibliotheque via la
    variable librairie.
    POST : Instancie l'objet Theme dans la variale globale theme_courant.
    """
    global theme_courant
    theme_courant = librairie.recuperer_theme(nom_du_theme)
