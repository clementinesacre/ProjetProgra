# -*- coding: utf-8 -*-

from datetime import date
from simplification import fonctions as fct
from classe import variable_globale as vb
import json

import logging
logger = logging.getLogger("cultureg")


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
        dico_python = fct.recup_donnees_fichier_json(fct.chemin_absolu('ressources/scores.json'))
        dico_python[vb.joueur.nom][theme.nom_theme].append([round(point, 2), date.today().strftime('%d/%m/%Y')])
        try:
            with open(fct.chemin_absolu('ressources/scores.json'), 'w') as fichier:
                dico_json = json.dumps(dico_python)
                fichier.write(dico_json)

        except FileNotFoundError:
            logger.error('classe/utilisateur.py : ajout_score() : FileNotFoundError : ressources/scores.json')
            raise FileNotFoundError('Fichier introuvable.')
        except IOError:
            logger.error('classe/utilisateur.py : ajout_score() : IOError : ressources/scores.json')
            raise IOError('Erreur IO.')

        logger.info('classe/utilisateur.py : ajout_score() : ajout de points : ' + str(point) + ", theme : "
                    + theme.nom_theme + ", joueur : " + self.__nom)
