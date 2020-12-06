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

    def retourne_fichier_bibliotheque(self):
        """
        Renvoie le ressources de l'objet Bibliotheque

        Post : retourne le nom du ressources de l'objet Bibliotheque sous forme de string.
        """
        return fct.recup_donnees_fichier(self.__nom_fichier_bibliotheque)

    def initialisation_theme(self, nom_theme):
        """
        Crée un objet Theme et l'ajoute à la liste de l'objet Bibliotheque.
        """
        objet_t = Theme(nom_theme)
        self.__liste_themes.append(objet_t)

    def retourne_themes(self):
        """
        Renvoie tous les objets Theme que l'objet Bibliotheque contient dans une liste.

        Post : renvoie les thèmes dans une liste.
        """
        return list(map(lambda x: x.nom_theme, self.__liste_themes))

    def recuperer_theme(self, nom_theme):
        """
        Retourne l'objet Theme sur base de son nom ou du nom de son ressources.
        """
        for theme_recuperer in self.__liste_themes:
            if theme_recuperer.nom_theme[0] == nom_theme or theme_recuperer.nom_theme[1] == nom_theme:
                return theme_recuperer

    def retourne_total(self):
        """
        Renvoie les questions et réponses de tous les objet Theme de l'objet Bibliotheque.

        Post : renvoie un dictionnaire, avec comme clé le nom du thème (pas le nom du ressources).
        """
        for theme_total in self.__liste_themes:
            self.__dictionnaire_themes[theme_total.nom_theme[0]] = theme_total.retourne_question_theme()
        return self.__dictionnaire_themes

    def creation_theme(self, nom_nouveau_fichier):
        """
        Crée un nouveau thème, en créant son ressources, en ajoutant le thème dans le fichier thèmes et dans la liste de
        thème.
        """
        nouveau_theme = Theme(nom_nouveau_fichier + ".csv")
        nom_fichier = nouveau_theme.nom_theme[1]

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
        self.__dictionnaire_themes[nouveau_theme.nom_theme[0]] = ""

        om.ajouter_question_console()

    def suppression_theme(self,   nom_du_fichier, indice):
        """
        Supprime un thème existant, en supprimant son ressources et en le retirant du fichier et de la liste de thèmes.
        """
        os.remove("ressources/" + nom_du_fichier)
        del self.__liste_themes[indice]

        liste_fichiers = []
        with open("ressources/themes.csv", "r") as doss1:
            lire = csv.reader(doss1)
            for ligne in lire:
                if nom_du_fichier != (','.join(ligne).rstrip()):
                    liste_fichiers.append(','.join(ligne))

        with open("ressources/themes.csv", 'w', newline='') as doss2:
            write = csv.writer(doss2)
            for i in liste_fichiers:
                write.writerow([i])


"""#+-factory où get_bibliotheque est une méthode statique
  #où test = objet biblio global
  def get_bibliotheque(cls):
      if test != none :
          return test
      test = cls()
      return test

biblio = Bibliotheque.get_bibliotheque()"""