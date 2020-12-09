# -*- coding: utf-8 -*-


class Question:
    def __init__(self, nom_question):
        self.__nom_question = nom_question
        self.__reponses = []

    @property
    def nom_question(self):
        """
        Permet de récupérer la question de l'objet Question.

        PRE : -
        POST : Renvoie la questions sous forme de string.
        """
        return self.__nom_question

    @property
    def reponses(self):
        """
        Permet de récupérer les réponses de l'objet Question.

        PRE : -
        POST : renvoie les réponses dans une liste de liste.
        """
        return self.__reponses

    def creation_reponses(self, reponses):
        """
        Permet de créer un objet Réponse.

        PRE : 'reponses' est une liste de liste, avec en première position le nom de la réponse et en deuxième position, son
        type.
        POST : Instancie 4 objets Reponse, sur base de leur nom et de leur type, et les ajoute à la liste de
        l'objet Question.
        """
        for reponse_creation in reponses:
            objet_r = Reponse(reponse_creation[0], reponse_creation[1])
            self.__reponses.append([objet_r.nom_reponse, objet_r.type_reponse])


class Reponse:
    def __init__(self, nom_reponse, type_bonne_reponse):
        self.__nom_reponse = nom_reponse
        self.__type_reponse = type_bonne_reponse

    @property
    def nom_reponse(self):
        """
        Permet de récupérer le nom de la réponse de l'objet.

        PRE : -
        POST : Renvoie le nom de la réponse sous forme de string.
        """
        return self.__nom_reponse

    @property
    def type_reponse(self):
        """
        Permet de récupérer le type de la réponse (vraie ou fausse).

        PRE : -
        POST : Renvoie True ou False.
        """
        return self.__type_reponse
