# -*- coding: utf-8 -*-

import json
from classe import variable_globale as vb
from classe.bibliotheque import *


def introduction():
    """
    Lance l'application en demandant le pseudo du joueur.
    Si le joueur est déjà encodé dans la base, on affiche ses scores précédents.
    Si il n'est pas encore encodé, son pseudo est enregistré dans l'application.
    """
    try:
        with open('fichier/scores.json') as file:
            dictionnaire = json.load(file)

            if vb.joueur.nom not in dictionnaire:
                dictionnaire[vb.joueur.nom] = vb.joueur.init_resultats()
                try:
                    with open('fichier/scores.json', 'w') as fichier:
                        nouveau_dictionnaire = json.dumps(dictionnaire)
                        fichier.write(nouveau_dictionnaire)

                except FileNotFoundError:
                    print('Fichier introuvable.')
                except IOError:
                    print('Erreur IO.')
                print("Bienvenue dans le jeu.")
            else:
                print("Vos scores précédents :\n")
                vb.joueur.resultats(dictionnaire)
                fct.separation()
            return dictionnaire

    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def jouer():
    """
    Selon le thème choisi par le joueur, la fonction lance une manche.
    """
    print("Thèmes : ")
    indice = 1
    for theme_nom in vb.librairie.retourne_themes():
        if len(vb.librairie.recuperer_theme(theme_nom[0]).retourne_question_theme()) > 0:
            print("    " + str(indice) + ". " + theme_nom[0])
            indice += 1
    print("    " + str(indice) + ". Revenir en arrière")
    print("")

    choix_theme = fct.validation_question("Choisissez un thème.", indice)
    fct.separation()

    if choix_theme == indice:
        menu_principal()
    theme_manche = vb.librairie.recuperer_theme(vb.librairie.retourne_themes()[choix_theme - 1][0])
    vb.joueur.creation_manche(theme_manche)


def ajouter_question():
    """
    Ajoute une question et ses réponses dans le thème précisé (dans l'objet Bibliothèque
    et dans le fichier du thème précisé).
    """
    print("Thèmes : ")
    for i in range(len(vb.librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + vb.librairie.retourne_themes()[i][0])
    print("")
    choix_theme = fct.validation_question("Choisissez un thème dans lequel rajouter une question.",
                                          len(vb.librairie.retourne_themes()))

    theme_a_modifier = vb.librairie.recuperer_theme(vb.librairie.retourne_themes()[choix_theme - 1][0])

    fct.separation()
    question_ajouter = input("Entrez la question : ")
    print("\nVous allez maintenant devoir entrer des réponses. Une seule réponse peut être bonne, "
          "les 3 autres doivent être fausses.")
    print("L'ordre n'a pas d'importance.\n")

    reponses_liste = []
    for i in range(4):
        reponse_ajouter = input("Entrez la réponse " + str(i + 1) + " : ")
        reponses_liste.append(reponse_ajouter)
    print("")

    bonne_reponse = fct.validation_question("Quelle réponse est la bonne ? Entrez le numéro de la réponse.", 4) - 1

    # Ajout de la question et réponses dans l'objet Theme
    liste = []
    for reponse_liste in reponses_liste:
        correction = False
        if reponse_liste == reponses_liste[bonne_reponse]:
            correction = True
        liste.append([reponse_liste, correction])
    theme_a_modifier.creation_question(question_ajouter, liste)

    # Ajout de la question dans le fichier theme
    reponses_liste.insert(0, reponses_liste[bonne_reponse])
    reponses_liste.insert(0, question_ajouter)
    theme_a_modifier.ecriture_question(reponses_liste)

    fct.separation()

    print("La question '" + question_ajouter + "' a été rajoutée dans le thème '" +
          vb.librairie.retourne_themes()[choix_theme - 1][0] + "', avec '" + reponses_liste[bonne_reponse + 2] +
          "' comme bonne réponse !")

    fct.separation()

    refaire = fct.validation_oui_non("Voulez-vous rajouter une nouvelle question ?")
    fct.separation()
    if refaire == "oui":
        ajouter_question()
    else:
        modifier()


def supprimer_question():
    """
    Supprime une question et ses réponses dans le thème précisé (dans l'objet Bibliothèque
    et dans le fichier du thème précisé).
    """
    """print("Thèmes : ")
    for i in range(len(vb.librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + vb.librairie.retourne_themes()[i][0])
    print("")"""
    print("Thèmes : ")
    indice_theme = 1
    for theme_nom in vb.librairie.retourne_themes():
        print("    " + str(indice_theme) + ". " + theme_nom[0])
        indice_theme += 1
    print("    " + str(indice_theme) + ". Revenir en arrière")
    print("")

    choix_theme = fct.validation_question("Choisissez le thème dans lequel supprimer une question", indice_theme)
    if choix_theme == indice_theme:
        modifier()

    theme_a_modifier = vb.librairie.recuperer_theme(vb.librairie.retourne_themes()[choix_theme - 1][0])
    fct.separation()

    if len(vb.librairie.recuperer_theme(vb.librairie.retourne_themes()[choix_theme - 1][0]).retourne_question_theme()) \
            == 0:
        print("Il n'y a pas de question dans ce thème.")
        fct.separation()
        supprimer_question()

    print("Questions du thème '" + vb.librairie.retourne_themes()[choix_theme - 1][0] + "' :")
    indice_question = 1
    questions_theme = list(theme_a_modifier.retourne_question_theme().keys())
    for question_supprimer in questions_theme:
        print("    " + str(indice_question) + ". " + question_supprimer)
        indice_question += 1
    print("")

    question_a_supprimer = fct.validation_question("Choisissez la question à supprimer.", indice_question - 1)
    fct.separation()

    valider_question = fct.validation_oui_non("Etes-vous sur de vouloir supprimer la question '" +
                                              questions_theme[question_a_supprimer - 1] + "' ?")
    if valider_question == "oui":
        theme_a_modifier.suppression_question(questions_theme[question_a_supprimer - 1])
        print("\nLa question '" + questions_theme[question_a_supprimer - 1] + "' a été supprimée !")

    else:
        print("\nAnnulation. Aucune question n'a été supprimée.")

    fct.separation()
    modifier()


def ajouter_theme():
    """
    Permet de créer un thème et de l'ajouter à l'application (en lui créant un fichier, en notant son nom dans le
    fichier thèmes, et en le rajoutant à la liste de thèmes).
    """
    nouveau_theme = input("Quel est le nom du thème que vous voulez ajouter : ")
    vb.librairie.creation_theme(nouveau_theme)

    fct.separation()
    modifier()


def supprimer_theme():
    """
    Permet de supprimer un thème en l'enlevant de l'application (en supprimant son fichier, et en le retirant du fichier
    des thèmes et de la liste des thèmes).
    """
    print("Thèmes : ")
    for i in range(len(vb.librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + vb.librairie.retourne_themes()[i][0])
    print("")

    numero_theme = fct.validation_question("Quel thème voulez-vous supprimer ? ", len(vb.librairie.retourne_themes()))
    fct.separation()

    validation_theme = fct.validation_oui_non("Etes-vous sur de vouloir supprimer le thème '" +
                                              vb.librairie.retourne_themes()[numero_theme - 1][0] + "' ?")
    if validation_theme == "oui":
        print("\nLe thème '" + vb.librairie.retourne_themes()[numero_theme - 1][0] + "' a été supprimé !")
        vb.librairie.suppression_theme(vb.librairie.retourne_themes()[numero_theme - 1][1][8:], numero_theme - 1)

    else:
        print("\nAnnulation. Aucun thème n'a été supprimé.")

    fct.separation()
    modifier()


def modifier():
    """
    Permet au joueur de modifier l'application en ajoutant/supprimant des thèmes/questions.
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
    # clear

    if mode == 1:
        ajouter_theme()
    elif mode == 2:
        ajouter_question()
    elif mode == 3:
        supprimer_theme()
    elif mode == 4:
        supprimer_question()
    else:
        menu_principal()


def quitter():
    """
    Permet de fermer le programme. Si on veut le relancer, il faudra l'exécuter à nouveau.
    """
    print("Au revoir " + vb.joueur.nom + ".\n")
    print("Application fermée.")


def menu_principal():
    """
    Affiche les différentes options dans le menu et appelle la fonction selon le choix du joueur.
    """
    print("Menu :")
    print("    1. Jouer")
    print("    2. Modifier")
    print("    3. Quitter")
    print("")
    mode = fct.validation_question("Choisissez une option.", 3)
    fct.separation()

    if mode == 1:
        jouer()
    elif mode == 2:
        modifier()
    elif mode == 3:
        quitter()


def initialisation_bibliotheque():
    themes = vb.librairie.retourne_fichier_bibliotheque()
    for theme in themes:
        for nom in theme:
            vb.librairie.initialisation_theme(nom)

    for theme_fichier in vb.librairie.retourne_themes():
        liste_questions = fct.recup_donnees_fichier(theme_fichier[1])
        for question in liste_questions:
            liste_reponses = []
            for reponse in range(2, len(question)):
                if question[reponse] == question[1]:
                    liste_reponses.append([question[reponse], True])

                else:
                    liste_reponses.append([question[reponse], False])
            vb.librairie.recuperer_theme(theme_fichier[1]).creation_question(question[0], liste_reponses)


def lancement_application():
    vb.initialisation_informations()
    initialisation_bibliotheque()
    vb.initialisation_joueur()

    fct.separation()
    dico_scores = introduction()
    menu_principal()
    # dessin = cg.Graphique(dico_scores)
