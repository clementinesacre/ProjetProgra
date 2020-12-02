# -*- coding: utf-8 -*-

from Classe.manche import *


class Utilisateur:
    def __init__(self, noms):
        self.__nom = noms

    @property
    def nom(self):
        """
        Permet d'accéder à l'attribut nom en dehors de l'objet Utilisateur.

        Post : retourne une string.
        """
        return self.__nom

    def init_resultats(self):
        """
        Initialise les thèmes de base pour le joueur.

        Post : renvoie les thèmes de base de l'application sous forme de dictionnaire
        (donc pas les thèmes que les utilisateurs auraient pu rajouter).
        """
        return {'geographie': [], 'math': []}

    def resultats(self, dico):
        """
        Affiche tout résultats confondus de l'utilisateur connecté.
        """
        print(dico[self.__nom])
        for theme_resultats in dico[self.__nom]:
            print(theme_resultats, " : ")
            for score in dico[self.__nom][theme_resultats]:
                print("    ", score[0], "% - ", score[1])
            print("")

    def creation_manche(self, theme_manche):
        """
        Crée un objet Manche et le lance.
        """
        manche = Manche(theme_manche)
        manche.lancer_manche()
