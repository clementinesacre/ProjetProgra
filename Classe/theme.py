# -*- coding: utf-8 -*-

import csv

from options.menu import *
from Classe.question_reponse import *


class Theme:
    def __init__(self, nom_fichier):
        self.__nom_theme = nom_fichier[:-4]
        self.__nom_fichier = "fichier/" + nom_fichier
        self.__dictionnaire = {}
        self.__liste_questions = []

    @property
    def nom_theme(self):
        """
        Renvoie le nom de l'objet Theme et le nom du fichier qui contient les questions
        de l'objet Theme.

        Post : renvoie les deux informations dans une liste.
        """
        return [self.__nom_theme, self.__nom_fichier]

    def retourne_question_theme(self):
        """
        Renvoie les questions et réponses de tous les objet Theme de l'objet Bibliotheque.

        Post : renvoie un dictionnaire.
        """
        return self.__dictionnaire

    def recuperer_question(self, question_a_recuperer):
        """
        Retourne l'objet Theme sur base de son nom ou du nom de son fichier.
        """
        for question_recuperer in range(len(self.__liste_questions)):
            if self.__liste_questions[question_recuperer].nom_question == question_a_recuperer:
                return self.__liste_questions[question_recuperer]

    def creation_question(self, nom_question, reponses):
        """
        Permet de créer un objet Question et de l'ajouter au dictionnaire de l'objet Theme.
        Ces informations sont rajoutées avec la question comme clé du dictionnaire et
        les réponses comme valeurs du dictionnaire.
        Crée également les objet Réponse pour pouvoir les rajouter dans le dictionnaire.
        """
        objet_q = Question(nom_question)
        objet_q.creation_reponses(reponses)
        self.__dictionnaire[objet_q.nom_question] = objet_q.retourne_reponses_question()
        self.__liste_questions.append(objet_q)

    def ecriture_question(self, liste):
        """
        Ecrit une nouvelle question et les réponses associées dans le fichier d'un thème précis.
        """
        try:
            with open(self.__nom_fichier, "a", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',')
                nouveau_fichier.writerow(liste)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def suppression_question(self, questions):
        """
        Supprime une question précise en la supprimant du dictionnaire de questions ainsi que du fichier de thème dans
        lequel elle se trouvait.
        """
        del self.__dictionnaire[questions]
        try:
            with open(self.__nom_fichier, "w", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                nouveau_fichier.writerow(["questions", "bonneReponse", "reponseA", "reponseB", "reponseC", "reponseD"])
                for question_supprimer in self.__dictionnaire:
                    reponses = self.__dictionnaire[question_supprimer]
                    nouveau_fichier.writerow([question_supprimer, list(filter(lambda x: x[1] is True, reponses))[0][0],
                                              reponses[0][0], reponses[1][0], reponses[2][0], reponses[3][0]])

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')
