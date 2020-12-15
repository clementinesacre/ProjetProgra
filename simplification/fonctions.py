# -*- coding: utf-8 -*-

import random
import csv
import json
import os
import sys

import logging
logger = logging.getLogger("cultureg")


def aleatoire(questions, nbr_questions):
    """
    Permet d'avoir nbr_questions questions aléatoires.

    PRE : 'questions' est un dictionnaire ou une liste comprenant des strings comme valeur, et 'nbr_questions' est un
    entier compris entre 1 et len(questions).
    POST : Les questions sont renvoyées dans une liste.
    """
    liste = list(questions)
    chiffres_aleatoires = random.sample(range(1, len(questions) + 1), nbr_questions)
    return [liste[chiffre - 1] for chiffre in chiffres_aleatoires]


def recup_donnees_fichier(fichier_a_ouvrir):
    """
    Permet de récuperer les informations d'un fichier.

    PRE : 'fichier_a_ouvrir' est un fichier csv.
    POST : Retourne les informations du fichier sour forme de liste.
    """
    try:
        with open(chemin_absolu(fichier_a_ouvrir)) as file:
            lecture = csv.reader(file)
            liste = list(map(lambda x: x, lecture))[1:]
            return liste

    except FileNotFoundError:
        logger.error('simplification/fonctions.py : recup_donnees_fichier() : FileNotFoundError : ' + fichier_a_ouvrir)
        raise FileNotFoundError('Fichier introuvable.')
    except IOError:
        logger.error('simplification/fonctions.py : recup_donnees_fichier() : IOError : ' + fichier_a_ouvrir)
        raise IOError('Erreur IO.')


def separation():
    """
    Permet de créer une ligne de séparation afin d'avoir un écran plus clair, avec un retour chariot au dessus et en
    dessous.

    PRE : -
    POST : affiche une séparation.
    """
    print("                                         ")
    print("-----------------------------------------")
    print("                                         ")


def validation_question(question, longueur):
    """
    Permet de vérifier que le paramètre entré est un objet de type int se trouvant entre 1 et 'longueur'. Boucle tant
    que ces conditions ne sont pas respectées.

    PRE : 'question' doit être une chaine de caractère, 'longueur' doit être un entier.
    POST : Retourne le chiffre respectant les conditions, sous forme d'entier.
    """
    nombre = ""
    while True:
        try:
            nombre = int(input("{0} (entrez un chiffre entre 1 et {1}) : ".format(question, longueur)))
            if 0 < nombre <= longueur:
                break
            else:
                print("Veuillez entrez un chiffre entre 1 et {0}.".format(longueur))

        except ValueError:
            logger.error('simplification/fonctions.py : validation_question() : ValueError : ' + str(nombre))
            print("Veuillez entrer un nombre.")

    return nombre


def validation_oui_non(question):
    """
    Permet de vérifier que le paramètre entré est une string valant "oui" ou "non". Boucle tant que ces conditions ne
    sont pas respectées.

    PRE : 'question' doit être une chaine de caractère.
    POST : Retourne la string "oui" ou "non".
    """
    while True:
        reponse = input("{0} (oui ou non) : ".format(question))
        try:
            if reponse == "oui" or reponse == "non":
                break
            else:
                print("Les seules réponses acceptées sont 'oui' et 'non'.")
        except TypeError:
            logger.error('simplification/fonctions.py : validation_oui_non() : TypeError : ' + reponse)
            print("Erreur.")

    return reponse


def recup_donnees_fichier_json(fichier):
    """
    Permet de récuperer les informations d'un fichier.

    PRE : 'fichier' est un fichier json.
    POST : Retourne le dictionnaire contenu dans le fichier json.
    """
    try:
        with open(chemin_absolu(fichier), 'r') as file:
            donnees = json.load(file)
    except FileNotFoundError:
        logger.error('simplification/fonctions.py : recup_donnees_fichier_json() : FileNotFoundError : ' + fichier)
        raise FileNotFoundError('Fichier introuvable.')
    except IOError:
        logger.error('simplification/fonctions.py : recup_donnees_fichier_json() : IOError : ' + fichier)
        raise IOError('Erreur IO.')
    return donnees


def chemin_absolu(relative_path):
    """
    Donne le chemin absolu d'un fichier.

    PRE : -
    POST : Retourne ''C:\\Users\\sacre\\PycharmProjects\\ProjetProgra\\' + 'relative_path'.
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path[:-15], relative_path)


