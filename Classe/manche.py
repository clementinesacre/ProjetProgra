# -*- coding: utf-8 -*-

from datetime import date

from options.menu import *
import options.menu as om
from Simplification import fonctions as fct
from Classe import variable_globale as vb


class Manche:
    def __init__(self, theme_manche):
        self.__theme = theme_manche
        self.__nbr_questions = 0
        self.__pourcentage = 0
        self.__date = date.today().strftime('%d/%m/%Y')

    def lancer_manche(self):
        """
        Permet de lancer une manche, c'est à dire de répondre à des questions,
        puis de noter le score de cette manche de l'Utilisateur qui a lancé la manche.
        """
        questions_liste = vb.librairie.retourne_total()[self.__theme.nom_theme[0]]

        self.__nbr_questions = fct.validation_question("Combien de questions pour la partie ?", len(questions_liste))
        fct.separation()

        liste_questions_aleatoires = fct.aleatoire(questions_liste, self.__nbr_questions)
        points_joueur = 0
        for question_manche in liste_questions_aleatoires:
            print(question_manche)
            reponses = self.__theme.recuperer_question(question_manche).retourne_reponses_question()
            for i in range(len(reponses)):
                print("    " + str(i + 1) + ". " + reponses[i][0])

            reponse_joueur = fct.validation_question("Quelle réponse choisissez-vous ?", len(reponses))

            if reponses[reponse_joueur - 1][1]:
                print("\nCorrect !")
                points_joueur += 1
            else:
                print("\nFaux !")

            fct.separation()

        print("Vous avez", points_joueur, "bonne(s) réponse(s) sur " + str(len(liste_questions_aleatoires)) + ".")
        self.__pourcentage = points_joueur / len(liste_questions_aleatoires) * 100

        self.ajout_score()

        fct.separation()
        om.menu_principal()

    def ajout_score(self):
        """
        Permet d'ajouter un score à l'objet Utilisateur.
        """
        try:
            with open('fichier/scores.json', 'r') as file:
                dico_python = json.load(file)
                dico_python[vb.joueur.nom][self.__theme.nom_theme[0]].append(
                    [round(self.__pourcentage, 2), self.__date])
            with open('fichier/scores.json', 'w') as fichier:
                dico_json = json.dumps(dico_python)
                fichier.write(dico_json)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')
