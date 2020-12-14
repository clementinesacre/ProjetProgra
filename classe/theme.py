# -*- coding: utf-8 -*-

from classe.question_reponse import *
import csv


class Theme:
    def __init__(self, nom_fichier):
        self.__nom_theme = nom_fichier[:-4]
        self.__nom_fichier = "ressources/" + nom_fichier
        self.__question_theme = {}
        self.__liste_questions = []

    @property
    def nom_theme(self):
        """
        Permet de récupérer le nom du thème de l'objet Theme.

        PRE : -
        POST : Renvoie le nom sous forme de string.
        """
        return self.__nom_theme

    @property
    def nom_fichier(self):
        """
        Permet de récupérer le nom du fichier de l'objet Theme.

        PRE : -
        POST : Retourne le nom du fichier sous forme de string.
        """
        return self.__nom_fichier

    @property
    def question_theme(self):
        """
        Permet de récupérer les questions et réponses associées à l'objet Theme.

        PRE : -
        POST : Renvoie un dictionnaire avec la question comme clé et les réponses dans des listes comme valeur.
        """
        return self.__question_theme

    def recuperer_question(self, question_a_recuperer):
        """
        Permet de récupérer un objet Question sur base de son nom 'question_a_recuperer'.

        PRE : 'question_a_recuperer' est un string.
        POST : Retourne un objet Question.
        """
        return list(filter(lambda x: x.nom_question == question_a_recuperer, self.__liste_questions))[0]

    def initialisation_question(self, donnees):
        """
        Permet de créer un objet Question.

        PRE : 'donnees' est une liste avec la question comme premier élément, le deuxième élément est la bonne réponse,
        et les quatres éléments suivants sont les différentes propositions de réponses.
        POST : Crée l'objet Question, et l'ajoute au dictionnaire du thème lié. Initialise également les réponses qui
        sont liées à la question dans l'objet Question.
        """
        objet_q = Question(donnees[0])
        liste = list(map(lambda x: [x, x == donnees[1]], donnees[2:]))
        objet_q.creation_reponses(liste)
        self.__question_theme[objet_q.nom_question] = objet_q.reponses
        self.__liste_questions.append(objet_q)

    def creation_question(self, donnees):
        """
        Permet de créer un objet Question.

        PRE : 'donnees' est une liste avec la question comme premier élément, le deuxième élément est la bonne réponse,
        et les quatres éléments suivants sont les différentes propositions de réponses.
        POST : Crée la question, puis écrit ses différentes informations dans le fichier du thème associé.
        """
        self.initialisation_question(donnees)
        try:
            with open(self.__nom_fichier, "a", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',')
                nouveau_fichier.writerow(donnees)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def suppression_question(self, question_a_supprimer):
        """
        Permet de supprimer une question.

        PRE : 'question_a_supprimer' est une string et doit être une clé existante du dictionnaire du thème.
        POST : Supprime 'question_a_supprimer' et ses réponses associées du fichier du thème associé, ainsi qu'en la
        supprimant du dictionnaire des questions du thème.
        """
        del self.__question_theme[question_a_supprimer]
        try:
            with open(self.__nom_fichier, "w", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                nouveau_fichier.writerow(["questions", "bonneReponse", "reponseA", "reponseB", "reponseC", "reponseD"])
                for question in self.__question_theme:
                    reponses = self.__question_theme[question]
                    nouveau_fichier.writerow([question, list(filter(lambda x: x[1] is True, reponses))[0][0],
                                              reponses[0][0], reponses[1][0], reponses[2][0], reponses[3][0]])

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')



