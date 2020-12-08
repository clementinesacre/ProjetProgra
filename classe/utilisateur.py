# -*- coding: utf-8 -*-


from datetime import date
from simplification import fonctions as fct
from classe import variable_globale as vb
import json


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

    def ajout_score(self, theme, point):
        """
        Permet d'ajouter un score à l'objet Utilisateur.
        """
        dico_python = fct.recup_donnees_fichier_json('ressources/scores.json')
        dico_python[vb.joueur.nom][theme.nom_theme[0]].append([round(point, 2), date.today().strftime('%d/%m/%Y')])
        try:
            with open('ressources/scores.json', 'w') as fichier:
                dico_json = json.dumps(dico_python)
                fichier.write(dico_json)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')
