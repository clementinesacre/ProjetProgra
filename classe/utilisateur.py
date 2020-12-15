# -*- coding: utf-8 -*-


from datetime import date
from simplification import fonctions as fct
from classe import variable_globale as vb
from classe import theme as t
import json
import logging
import datetime
logging.basicConfig(filename='../log/history.log', level=logging.DEBUG)


class Utilisateur:
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        """
        Permet d'accéder à l'attribut nom en dehors de l'objet Utilisateur.

        PRE : -
        POST : retourne le nom du joueur sous forme de string.
        """
        return self.__nom

    def init_resultats(self):
        """
        Permet d'initialiser les thèmes de base pour le joueur.

        PRE : -
        POST : renvoie les thèmes de base de l'application sous forme de dictionnaire (donc pas les thèmes que les
        utilisateurs auraient pu rajouter).
        """
        return {'geographie': [], 'math': []}

    def ajout_score(self, theme, point):
        """
        Permet d'ajouter un score à l'objet Utilisateur.

        PRE : 'theme' est un objet Theme. 'point' peut être un float ou un int.
        POST : Ecrit le score dans le fichier contenant l'historique des scores des différents joueurs.
        """
        dico_python = fct.recup_donnees_fichier_json('ressources/scores.json')
        dico_python[vb.joueur.nom][theme.nom_theme].append([round(point, 2), date.today().strftime('%d/%m/%Y')])
        try:
            with open('ressources/scores.json', 'w') as fichier:
                dico_json = json.dumps(dico_python)
                fichier.write(dico_json)

        except FileNotFoundError:
            logging.error(str(datetime.datetime.now())
                          + ' classe/utilisateur.py : ajout_score() : FileNotFoundError : ' + theme)
            raise FileNotFoundError('Fichier introuvable.')
        except IOError:
            logging.error(str(datetime.datetime.now())
                          + ' classe/utilisateur.py : ajout_score() : IOError : ' + theme)
            raise IOError('Erreur IO.')

