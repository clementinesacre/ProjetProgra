# -*- coding: utf-8 -*-

import options.menu as om
from simplification import fonctions as fct
from classe.theme import *
import os


class Bibliotheque:
    def __init__(self, nom_bibliotheque, nom_fichier_bibliotheque):
        self.__nom_bibliotheque = nom_bibliotheque
        self.__nom_fichier_bibliotheque = nom_fichier_bibliotheque
        self.__liste_themes = []
        self.__dictionnaire_themes = {}

    @property
    def nom_bibliotheque(self):
        """
                Renvoie le fichier de l'objet Bibliotheque

                PRE : -
                POST : Retourne le nom de la bibliotheque de l'objet sous forme de string.
                """
        return self.__nom_bibliotheque
    @property
    def nom_fichier_bibliotheque(self):
        """
        Renvoie le fichier de l'objet Bibliotheque

        PRE : -
        POST : Retourne le nom du fichier de l'objet sous forme de string.
        """
        return fct.recup_donnees_fichier(self.__nom_fichier_bibliotheque)

    def initialisation_theme(self, nom_theme):
        """
        Crée un objet Theme.

        PRE : 'nom_theme' est une string.
        POST : Instancie un objet Theme et l'ajoute à la liste de l'objet Bibliotheque.
        """
        objet_t = Theme(nom_theme)
        self.__liste_themes.append(objet_t)

    def retourne_themes(self):
        """
        Renvoie les noms de tous les objets Theme que l'objet Bibliotheque contient.

        PRE : -
        POST : Renvoie les noms des objets Theme sous forme de string dans une liste.
        """
        return list(map(lambda x: x.nom_theme, self.__liste_themes))

    @property
    def liste_themes(self):
        """
        Retourne tous les objets Theme instanciés dans l'objet Bibliotheque.

        PRE : -
        POST : Renvoie les objets Theme dans une liste.
        """
        return self.__liste_themes

    def recuperer_theme(self, nom_theme):
        """
        Récupère l'objet d'un Theme.

        PRE : 'nom_theme' est une string.
        POST : Retourne l'objet Theme sur base de son nom ou du nom de son fichier.
        """
        for theme_recuperer in self.__liste_themes:
            if theme_recuperer.nom_theme == nom_theme or theme_recuperer.nom_fichier == nom_theme:
                return theme_recuperer

    @property
    def dictionnaire_themes(self):
        """
        Permet de récupérer toutes les données liées à l'objet Bibliotheque, tels que les thèmes avec leurs questions
        et leurs réponses.

        PRE : -
        POST : Renvoie un dictionnaire, avec comme clé le nom des thèmes, et un dictionnaire comme valeur, contenant
        les questions et réponses du thème.
        """
        for theme_total in self.__liste_themes:
            self.__dictionnaire_themes[theme_total.nom_theme] = theme_total.question_theme
        return self.__dictionnaire_themes

    def creation_theme(self, nom_nouveau_fichier):
        """
        Permet de créer un nouveau thème.

        PRE : 'nom_nouveau_fichier' est une string.
        POST : Instancie un objet Theme, crée son fichie, l'ajoute dans le fichier thèmes et dans la liste des objets
        Theme.
        """
        nouveau_theme = Theme(nom_nouveau_fichier + ".csv")
        nom_fichier = nouveau_theme.nom_fichier

        try:
            with open(nom_fichier, 'w', newline='') as csvfile:
                write = csv.writer(csvfile)
                write.writerow(["questions", "bonneReponse", "reponseA", "reponseB", "reponseC", "reponseD"])

            with open("ressources/themes.csv", 'a', newline='') as doss21:
                write = csv.writer(doss21)
                write.writerow([nom_fichier[11:]])

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

        self.__liste_themes.append(nouveau_theme)
        self.__dictionnaire_themes[nouveau_theme.nom_theme] = ""

        om.ajouter_question_console()

    def suppression_theme(self, theme):
        """
        Permet de supprimer un thème existant.

        PRE : 'theme' est un objet Theme.
        POST : Supprime le fichier du thème et le retire du fichier des thèmes et de la liste des objets Themes.
        """
        os.remove(theme.nom_fichier)
        del self.__liste_themes[self.__liste_themes.index(theme)]

        liste_fichiers = []
        with open("ressources/themes.csv", "r") as fichier_lecture:
            lire = csv.reader(fichier_lecture)
            for ligne in lire:
                if theme.nom_fichier[11:] != (','.join(ligne).rstrip()):
                    liste_fichiers.append(','.join(ligne))

        with open("ressources/themes.csv", 'w', newline='') as fichier_ecriture:
            write = csv.writer(fichier_ecriture)
            for i in liste_fichiers:
                write.writerow([i])
