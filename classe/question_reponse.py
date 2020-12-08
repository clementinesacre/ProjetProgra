# -*- coding: utf-8 -*-


class Question:
    def __init__(self, nom_question):
        self.__nom_question = nom_question
        self.__reponses = []

    @property
    def nom_question(self):
        """
        Renvoie la question de l'objet Question.

        Post : renvoie une string.
        """
        return self.__nom_question

    @property
    def reponses(self):
        """
        Renvoie les reponses de l'objet Question.

        Post : renvoie une liste de liste.
        """
        return self.__reponses

    def creation_reponses(self, reponses):
        """
        Permet de créer un objet Réponse et de l'ajouter à la liste de l'objet Question.
        """
        for reponse_creation in reponses:
            objet_r = Reponse(reponse_creation[0], reponse_creation[1])
            self.__reponses.append(objet_r.nom_reponse)


class Reponse:
    def __init__(self, nom_reponse, type_bonne_reponse):
        self.__nom_reponse = nom_reponse
        self.__type_bonne_reponse = type_bonne_reponse

    @property
    def nom_reponse(self):
        """
        Renvoie le nom de la reponse de l'objet Reponse ainsi que son type (vraie ou fausse).

        Post : renvoie une liste contenant les deux informations.
        """
        return [self.__nom_reponse, self.__type_bonne_reponse]
