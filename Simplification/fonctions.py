import random
import csv


def aleatoire(questions, nbr_questions):
    """
    Renvoie x questions aléatoirement provenant de préférence d'un dictionnaire ou d'une
    liste, où x est précisé à l'appel de la fonction.

    Post : les questions sont renvoyées dans une liste.
    """
    liste = []
    compteur = 0
    liste_questions = list(questions)
    while compteur < nbr_questions:
        x = random.randint(0, len(liste_questions) - 1)
        if liste_questions[x] not in liste:
            liste.append(liste_questions[x])
            compteur += 1

    return liste


def recup_donnees_fichier(fichier_a_ouvrir):
    """
    Récupère les informations d'un fichier pour pouvoir les utiliser.

    Pré : fichier csv.

    Post : retourne les informations sour forme de liste.
    """
    try:
        with open(fichier_a_ouvrir) as file:
            lecture = csv.reader(file)
            liste = list(map(lambda x: x, lecture))
            del liste[0]
            return liste

    except FileNotFoundError:
        raise FileNotFoundError('Fichier introuvable.')
    except IOError:
        raise IOError('Erreur IO.')


def separation():
    """
    Crée une ligne de séparation afin d'avoir un écran plus clair, avec un retour
    chariot au dessus et en dessous.
    """
    print("                                         ")
    print("-----------------------------------------")
    print("                                         ")


def validation_question(question, longueur):
    """
    Vérifie que le paramètre entré est un objet de type int se trouvant entre 1 et la longueur précisée.
    Boucle tant que ces conditions ne sont pas respectées.

    Pre : question doit être une chaine de caractère, longueur doit être un entier.

    Post : Retourne le chiffre respectant les conditions sous forme d'int.
    """
    while True:
        try:
            nombre = int(input(question + " (entrez un chiffre entre 1 et " + str(longueur) + ") : "))
            if 0 < nombre <= longueur:
                break
            else:
                print("Veuillez entrez un chiffre entre 1 et " + str(longueur) + ".")
        except:
            print('Veuillez entrer un nombre naturel.')

    return nombre


def validation_oui_non(question):
    """
    Vérifie que le paramètre entré est une string valant "oui" ou "non".
    Boucle tant que ces conditions ne sont pas respectées.

    Pre : question doit être une chaine de caractère.

    Post : Retourne la string respectant les conditions.
    """
    while True:
        reponse = input(question + " (oui ou non) : ")
        try:
            if reponse == "oui" or reponse == "non":
                break
            else:
                print("Les seules réponses acceptées sont 'oui' et 'non'.")
        except:
            print("Les seules réponses acceptées sont 'oui' et 'non'.")
    return reponse
