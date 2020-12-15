# -*- coding: utf-8 -*-
# Auteur : Cécile Bonnet - Clémentine Sacré


import json
from classe import variable_globale as vb
from classe.bibliotheque import *
from simplification import fonctions as fct

"""import argparse"""
import sys
from graphique import console_graphique as cg

import datetime
import logging
# logging.basicConfig(filename='./log/history.log', level=logging.DEBUG)

logger = logging.getLogger("cultureg")

def introduction():
    """
    Permet de lancer l'application en accueillant le joueur.

    PRE : L'objet Utilisateur utilisé via 'joueur' doit avoir été initialisé auparavant.
    POST : Si le joueur est déjà encodé dans la base, on affiche ses scores précédents. Si il n'est pas encore encodé,
    son pseudo est enregistré dans l'application.
    """
    dictionnaire = fct.recup_donnees_fichier_json('ressources/scores.json')
    if vb.joueur.nom not in dictionnaire:
        dictionnaire[vb.joueur.nom] = vb.joueur.init_resultats()
        try:
            with open(fct.chemin_absolu('ressources/scores.json', 'w')) as fichier:
                nouveau_dictionnaire = json.dumps(dictionnaire)
                fichier.write(nouveau_dictionnaire)

        except FileNotFoundError:
            logger.error(str(datetime.datetime.now()) + ' options/menu.py : introduction() : FileNotFoundError : '
                                                         'ressources/scores.json')
            raise FileNotFoundError('Fichier introuvable.')
        except IOError:
            logger.error(str(datetime.datetime.now()) + ' options/menu.py : introduction() : IOError : '
                                                         'ressources/scores.json')
            raise IOError('Erreur IO.')

        print("Bienvenue dans le jeu.")
    else:
        print("Vos scores précédents :\n")

        for theme_resultats in dictionnaire[vb.joueur.nom]:
            print(theme_resultats, " : ")
            for score in dictionnaire[vb.joueur.nom][theme_resultats]:
                print("    ", score[0], "% - ", score[1])

        fct.separation()
    return dictionnaire


def jouer_console():
    """
    Permet à l'utilisateur de lancer une manche, selon le thème choisi qu'il a choisi.

    PRE : 'joueur' et 'librairie' doivent avoir été initialisés auparavant en global, via leur objet respectif.
    POST : Ajoute les points du joueur selon les réponses auxquelles il a répondu correctement.
    """
    themes_jeu = vb.librairie.retourne_themes()
    print("Thèmes : ")
    [print("    {0}. {1}".format(themes_jeu.index(theme_nom) + 1, theme_nom)) for theme_nom in themes_jeu]
    print("    {0}. Revenir en arrière\n".format(len(vb.librairie.retourne_themes()) + 1))

    choix_theme = fct.validation_question("Choisissez un thème.", len(themes_jeu) + 1)
    if choix_theme == len(themes_jeu) + 1:
        fct.separation()
        return menu_principal()

    vb.initialisation_theme(themes_jeu[choix_theme - 1])
    fct.separation()

    if len(themes_jeu) == 0:
        print("Il n'y a pas de question dans ce thème.")
        fct.separation()
        return jouer_console()

    questions_liste = vb.theme_courant.question_theme

    # Lancement de la partie
    nbr_questions = fct.validation_question("Combien de questions pour la partie ?", len(questions_liste))
    fct.separation()

    liste_questions_aleatoires = fct.aleatoire(questions_liste, nbr_questions)
    points_joueur = 0
    for question_manche in liste_questions_aleatoires:
        print(question_manche)
        reponses = vb.theme_courant.recuperer_question(question_manche).reponses
        [print("    {0}. {1}".format(reponses.index(reponse) + 1, reponse[0])) for reponse in reponses]

        reponse_joueur = fct.validation_question("Quelle réponse choisissez-vous ?", len(reponses))

        if reponses[reponse_joueur - 1][1]:
            print("\nCorrect !")
            points_joueur += 1
        else:
            print("\nFaux !")

        fct.separation()

    pluriel = ("", "s")[points_joueur > 1]
    print("Vous avez {0} bonne{1} réponse{1} sur {2}.".format(points_joueur, pluriel, nbr_questions))
    pourcentage = points_joueur / nbr_questions * 100

    vb.joueur.ajout_score(vb.theme_courant, pourcentage)

    fct.separation()
    om.menu_principal()


def ajouter_question_console():
    """
    Permet à l'utilisateur de créer une question.

    PRE : 'librairie' doit avoir été initialisée auparavant en global, via son objet respectif.
    POST : Ajoute la question et ses réponses dans le thème précisé (dans l'objet Bibliothèque
    et dans le fichier du thème).
    """
    themes_modif = vb.librairie.retourne_themes()
    print("Thèmes : ")
    [print("    {0}. {1}".format(themes_modif.index(theme_nom) + 1, theme_nom)) for theme_nom in themes_modif]

    choix_theme = fct.validation_question("\nChoisissez un thème dans lequel rajouter une question.", len(themes_modif))
    vb.initialisation_theme(themes_modif[choix_theme - 1])
    fct.separation()

    question_ajouter = input("Entrez la question : ")
    print("\nVous allez maintenant devoir entrer des réponses. Une seule réponse peut être bonne, "
          "les 3 autres doivent être fausses.\nL'ordre n'a pas d'importance.\n")

    reponses_liste = [input("Entrez la réponse {0} : ".format(reponse + 1)) for reponse in range(4)]
    bonne_reponse = fct.validation_question("\nQuelle réponse est la bonne ? Entrez le numéro de la réponse.", 4) - 1

    ligne_donnees = [question_ajouter] + [reponses_liste[bonne_reponse]] + reponses_liste
    vb.theme_courant.creation_question(ligne_donnees)
    fct.separation()

    print("La question '{0}' a été ajoutée dans le thème '{1}', avec '{2}' comme bonne réponse."
          .format(question_ajouter, vb.theme_courant.nom_theme, reponses_liste[bonne_reponse]))
    fct.separation()

    refaire = fct.validation_oui_non("Voulez-vous rajouter une nouvelle question ?")
    fct.separation()
    if refaire == "oui":
        return ajouter_question_console()
    else:
        return modifier()


def supprimer_question_console():
    """
    Permet à l'utilisateur de supprimer une question dans un thème précis.

    PRE : 'librairie' doit avoir été initialisée auparavant en global, via son objet respectif.
    POST : Soit appelle la fonction permettant de supprimer la question (en la supprimant de l'objet Bibliothèque
    et du le fichier du thème), soit annule l'opération.
    """
    themes_modif = vb.librairie.retourne_themes()
    print("Thèmes : ")
    [print("    {0}. {1}".format(themes_modif.index(theme_nom) + 1, theme_nom)) for theme_nom in themes_modif]
    print("    {0}. Revenir en arrière\n".format(len(themes_modif) + 1))

    numero_theme = fct.validation_question("Choisissez le thème dans lequel supprimer une question",
                                           len(themes_modif) + 1)

    if numero_theme == len(themes_modif) + 1:
        return modifier()

    vb.initialisation_theme(themes_modif[numero_theme - 1])
    fct.separation()

    if len(vb.theme_courant.question_theme) == 0:
        print("Il n'y a pas de question dans ce thème.")
        fct.separation()
        return supprimer_question_console()

    questions_theme = list(vb.theme_courant.question_theme.keys())
    print("Questions du thème '{0}' : ".format(vb.theme_courant.nom_theme))
    [print("    {0}. {1}".format(questions_theme.index(question_supprimer) + 1, question_supprimer)) for
     question_supprimer in questions_theme]

    choix_question = fct.validation_question("\nChoisissez la question à supprimer.", len(questions_theme))
    fct.separation()

    valider_question = fct.validation_oui_non("Etes-vous sur de vouloir supprimer la question '" +
                                              questions_theme[choix_question - 1] + "' ?")
    if valider_question == "oui":
        vb.theme_courant.suppression_question(questions_theme[choix_question - 1])
        print("\nLa question '{0}' a été supprimée.".format(questions_theme[choix_question - 1]))

    else:
        print("\nAnnulation. Aucune question n'a été supprimée.")

    fct.separation()
    modifier()


def ajouter_theme_console():
    """
    Permet à l'utilisateur de créer un thème.

    PRE : 'librairie' doit avoir été initialisée auparavant en global, via son objet respectif.
    POST : Ajoute le thème créé à l'application, en lui créant un fichier, en notant son nom dans le
    fichier thèmes, et en le rajoutant à la liste de thèmes.
    """
    nouveau_theme = input("Quel est le nom du thème que vous voulez ajouter : ")
    vb.librairie.creation_theme(nouveau_theme)

    print("\nLe thème '{0}' a été ajouté.\n".format(nouveau_theme))
    print("Vous allez maintenant devoir rajouter des questions dans le nouveau thème.")
    fct.separation()
    ajouter_question_console()


def supprimer_theme_console():
    """
    Permet à l'utilisateur de supprimer un thème.

    PRE : 'librairie' doit avoir été initialisée auparavant en global, via son objet respectif.
    POST : Soit appelle la fonction  permettant de supprimer le thème (en supprimant son fichier, et en le retirant
    du fichier des thèmes et de la liste des thèmes), soit annule l'opération.
    """
    themes_supp = vb.librairie.retourne_themes()
    print("Thèmes : ")
    [print("    {0}. {1}".format(themes_supp.index(theme_nom) + 1, theme_nom)) for theme_nom in themes_supp]

    numero_theme = fct.validation_question("\nQuel thème voulez-vous supprimer ? ", len(themes_supp))
    fct.separation()

    vb.initialisation_theme(themes_supp[numero_theme - 1])
    validation_theme = fct.validation_oui_non("Etes-vous sur de vouloir supprimer le thème '{0}' ?"
                                              .format(vb.theme_courant.nom_theme))
    if validation_theme == "oui":
        vb.librairie.suppression_theme(vb.theme_courant)
        print("\nLe thème '{0}' a été supprimé.".format(vb.theme_courant.nom_theme))

    else:
        print("\nAnnulation. Aucun thème n'a été supprimé.")

    fct.separation()
    modifier()


def modifier():
    """
    Permet au joueur de modifier l'application en ajoutant/supprimant des thèmes/questions.

    PRE : -
    POST : Redirige l'utilisateur selon son choix en appelant la fonction adéquate.
    """
    print("Menu > Modifier :")
    print("    1. Ajouter un thème")
    print("    2. Ajouter une question")
    print("    3. Supprimer un thème")
    print("    4. Supprimer une question")
    print("    5. Revenir en arrière")
    print("")
    mode = fct.validation_question("Choisissez une option.", 5)
    fct.separation()

    if mode == 1:
        ajouter_theme_console()
    elif mode == 2:
        ajouter_question_console()
    elif mode == 3:
        supprimer_theme_console()
    elif mode == 4:
        supprimer_question_console()
    else:
        menu_principal()


def quitter():
    """
    Permet de fermer le programme. Si on veut le relancer, il faudra exécuter le fichier à nouveau.

    PRE : 'joueur' doit avoir été initialisé auparavant en global, via son objet respectif.
    POST : Affiche un message de fermeture.
    """
    print("Au revoir {0}.\n\nApplication fermée.".format(vb.joueur.nom))


def menu_principal():
    """
    Permet au joueur de choisir si il souhaite jouer ou apporter des modifications à l'application.

    PRE : -
    POST : Redirige l'utilisateur selon son choix en appelant la fonction adéquate.
    """
    print("Menu :")
    print("    1. Jouer")
    print("    2. Modifier")
    print("    3. Quitter")
    print("")
    mode = fct.validation_question("Choisissez une option.", 3)
    fct.separation()

    if mode == 1:
        jouer_console()
    elif mode == 2:
        modifier()
    elif mode == 3:
        quitter()


def initialisation_bibliotheque():
    """
    Initalise les informations de l'application, telles que les thèmes, les questions et les réponses.

    PRE : Nécessite l'existance de l'objet Bibliotheque, instancié à librairie.
    POST : Crée les thèmes, les questions, les réponses en tant qu'objet.
    """
    themes = vb.librairie.nom_fichier_bibliotheque
    for theme in themes:
        for nom in theme:
            vb.librairie.initialisation_theme(nom)

    for theme_fichier in vb.librairie.liste_themes:
        vb.initialisation_theme(theme_fichier.nom_theme)
        liste_questions = fct.recup_donnees_fichier(vb.theme_courant.nom_fichier)
        for question in liste_questions:
            vb.theme_courant.initialisation_question(question)


def lancement_application():
    """
    Démarre l'application.

    PRE : -
    POST : Si console : Initialise l'objet librairie avec ses informations, et l'objet joueur. Lance ensuite l'initialisation du jeu,
    puis l'accès au menu.
    Si graphique : lance l'interface graphique permettant de voir les scores des joueurs par thème.
    """
    commande = sys.argv

    if len(commande) != 2:
        print("Commandes attendues :")
        print("    pour lancer l'interface console : python main.py console ")
        print("    pour lancer l'interface graphique : python main.py graphique")
    elif commande[1] == "console":
        vb.initialisation_informations()
        initialisation_bibliotheque()
        vb.initialisation_joueur()
        fct.separation()
        introduction()
        menu_principal()

    elif commande[1] == "graphique":
        dico_scores = fct.recup_donnees_fichier_json('ressources/scores.json')
        cg.Graphique(dico_scores)

    else:
        print("Commandes attendues :")
        print("    pour lancer l'interface console : python main.py console ")
        print("    pour lancer l'interface graphique : python main.py graphique")
