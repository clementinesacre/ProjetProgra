# -*- coding: utf-8 -*-
# Auteur : Cécile Bonnet - Clémentine Sacré


import csv
import json
import os
from datetime import date

from Simplification import fonctions as f


# from Graphique import console_graphique as cg


##############################################################################


class Bibliotheque:
    def __init__(self, nom_bibliotheque, nom_fichier_bibliotheque):
        self.__nom_bibliotheque = nom_bibliotheque
        self.__nom_fichier_bibliotheque = nom_fichier_bibliotheque
        self.__liste_themes = []
        self.__dictionnaire_themes = {}

    def retourne_fichier_bibliotheque(self):
        """
        Renvoie le fichier de l'objet Bibliotheque

        Post : retourne le nom du fichier de l'objet Bibliotheque sous forme de string.
        """
        return f.recup_donnees_fichier(self.__nom_fichier_bibliotheque)

    def initialisation_theme(self, nom_theme):
        """
        Crée un objet Theme et l'ajoute à la liste de l'objet Bibliotheque.
        """
        objet_t = Theme(nom_theme)
        self.__liste_themes.append(objet_t)

    def retourne_themes(self):
        """
        Renvoie tous les objets Theme que l'objet Bibliotheque contient dans une liste.

        Post : renvoie les thèmes dans une liste.
        """
        liste = []
        for theme_retourne in self.__liste_themes:
            liste.append(theme_retourne.nom_theme)
        return liste

    def recuperer_theme(self, nom_theme):
        """
        Retourne l'objet Theme sur base de son nom ou du nom de son fichier.
        """
        for theme_recuperer in range(len(self.__liste_themes)):
            if self.__liste_themes[theme_recuperer].nom_theme[0] == nom_theme or \
                    self.__liste_themes[theme_recuperer].nom_theme[1] == nom_theme:
                return self.__liste_themes[theme_recuperer]

    def retourne_total(self):
        """
        Renvoie les questions et réponses de tous les objet Theme de l'objet Bibliotheque.

        Post : renvoie un dictionnaire, avec comme clé le nom du thème (pas le nom du fichier).
        """
        for theme_total in self.__liste_themes:
            self.__dictionnaire_themes[theme_total.nom_theme[0]] = theme_total.retourne_question_theme()
        return self.__dictionnaire_themes

    def creation_theme(self, nom_nouveau_fichier):
        """
        Crée un nouveau thème, en créant son fichier, en ajoutant le thème dans le fichier thèmes et dans la liste de
        thème.
        """
        nouveau_theme = Theme(nom_nouveau_fichier + ".csv")
        nom_fichier = nouveau_theme.nom_theme[1]

        try:
            with open(nom_fichier, 'w', newline='') as csvfile:
                write = csv.writer(csvfile)
                write.writerow(["questions", "bonneReponse", "reponseA", "reponseB", "reponseC", "reponseD"])

            with open("fichier/themes.csv", 'a', newline='') as doss21:
                write = csv.writer(doss21)
                write.writerow([nom_fichier[8:]])

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

        self.__liste_themes.append(nouveau_theme)
        self.__dictionnaire_themes[nouveau_theme.nom_theme[0]] = ""

        print("\nLe thème '" + nom_nouveau_fichier + "' a été ajouté !")
        print("Vous allez maintenant devoir rajouter des questions dans le nouveau thème.")

    def suppression_theme(self, nom_du_fichier, indice):
        """
        Supprime un thème existant, en supprimant son fichier et en le retirant du fichier et de la liste de thèmes.
        """
        os.remove("fichier/" + nom_du_fichier)
        del self.__liste_themes[indice]

        liste_fichiers = []
        with open("fichier/themes.csv", "r") as doss1:
            lire = csv.reader(doss1)
            for ligne in lire:
                if nom_du_fichier != (','.join(ligne).rstrip()):
                    liste_fichiers.append(','.join(ligne))

        with open("fichier/themes.csv", 'w', newline='') as doss2:
            write = csv.writer(doss2)
            for i in liste_fichiers:
                write.writerow([i])


##############################################################################

class Theme:
    def __init__(self, nom_fichier):
        self.__nom_theme = nom_fichier[:-4]
        self.__nom_fichier = "fichier/" + nom_fichier
        self.__dictionnaire = {}
        self.__liste_questions = []

    @property
    def nom_theme(self):
        """
        Renvoie le nom de l'objet Theme et le nom du fichier qui contient les questions
        de l'objet Theme.

        Post : renvoie les deux informations dans une liste.
        """
        return [self.__nom_theme, self.__nom_fichier]

    def retourne_question_theme(self):
        """
        Renvoie les questions et réponses de tous les objet Theme de l'objet Bibliotheque.

        Post : renvoie un dictionnaire.
        """
        return self.__dictionnaire

    def recuperer_question(self, question_a_recuperer):
        """
        Retourne l'objet Theme sur base de son nom ou du nom de son fichier.
        """
        for question_recuperer in range(len(self.__liste_questions)):
            if self.__liste_questions[question_recuperer].nom_question == question_a_recuperer:
                return self.__liste_questions[question_recuperer]

    def creation_question(self, nom_question, reponses):
        """
        Permet de créer un objet Question et de l'ajouter au dictionnaire de l'objet Theme.
        Ces informations sont rajoutées avec la question comme clé du dictionnaire et
        les réponses comme valeurs du dictionnaire.
        Crée également les objet Réponse pour pouvoir les rajouter dans le dictionnaire.
        """
        objet_q = Question(nom_question)
        objet_q.creation_reponses(reponses)
        self.__dictionnaire[objet_q.nom_question] = objet_q.retourne_reponses_question()
        self.__liste_questions.append(objet_q)

    def ecriture_question(self, liste):
        """
        Ecrit une nouvelle question et les réponses associées dans le fichier d'un thème précis.
        """
        try:
            with open(self.__nom_fichier, "a", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',')
                nouveau_fichier.writerow(liste)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def suppression_question(self, questions):
        """
        Supprime une question précise en la supprimant du dictionnaire de questions ainsi que du fichier de thème dans
        lequel elle se trouvait.
        """
        del self.__dictionnaire[questions]
        try:
            with open(self.__nom_fichier, "w", newline='') as fichier:
                nouveau_fichier = csv.writer(fichier, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                nouveau_fichier.writerow(["questions", "bonneReponse", "reponseA", "reponseB", "reponseC", "reponseD"])
                for question_supprimer in self.__dictionnaire:
                    reponses = self.__dictionnaire[question_supprimer]
                    nouveau_fichier.writerow([question_supprimer, list(filter(lambda x: x[1] is True, reponses))[0][0],
                                              reponses[0][0], reponses[1][0], reponses[2][0], reponses[3][0]])

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')


##############################################################################

class Question:
    def __init__(self, nom_question):
        self.__nom_question = nom_question
        self.__liste_reponse = []

    @property
    def nom_question(self):
        """
        Renvoie la question de l'objet Question.

        Post : renvoie une string.
        """
        return self.__nom_question

    def retourne_reponses_question(self):
        """
        Renvoie les reponses de l'objet Question.

        Post : renvoie une liste de liste.
        """
        return self.__liste_reponse

    def creation_reponses(self, reponses):
        """
        Permet de créer un objet Réponse et de l'ajouter à la liste de l'objet Question.
        """
        for reponse_creation in reponses:
            objet_r = Reponse(reponse_creation[0], reponse_creation[1])
            self.__liste_reponse.append(objet_r.nom_reponse)


##############################################################################

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


##############################################################################

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

    def resultats(self, dico):
        """
        Affiche tout résultats confondus de l'utilisateur connecté.
        """
        print(dico[self.__nom])
        for theme_resultats in dico[self.__nom]:
            print(theme_resultats, " : ")
            for score in dico[self.__nom][theme_resultats]:
                print("    ", score[0], "% - ", score[1])
            print("")

    def creation_manche(self, theme_manche):
        """
        Crée un objet Manche et le lance.
        """
        manche = Manche(theme_manche)
        manche.lancer_manche()


##############################################################################


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
        questions_liste = librairie.retourne_total()[self.__theme]

        self.__nbr_questions = f.validation_question("Combien de questions pour la partie ?", len(questions_liste))
        f.separation()

        liste_questions_aleatoires = f.aleatoire(questions_liste, self.__nbr_questions)
        points_joueur = 0
        for question_manche in liste_questions_aleatoires:
            print(question_manche)
            reponses = librairie.recuperer_theme(self.__theme).recuperer_question(question_manche). \
                retourne_reponses_question()
            for i in range(len(reponses)):
                print("    " + str(i + 1) + ". " + reponses[i][0])

            reponse_joueur = f.validation_question("Quelle réponse choisissez-vous ?", len(reponses))

            if reponses[reponse_joueur - 1][1]:
                print("\nCorrect !")
                points_joueur += 1
            else:
                print("\nFaux !")

            f.separation()

        print("Vous avez", points_joueur, "bonne(s) réponse(s) sur " + str(len(liste_questions_aleatoires)) + ".")
        self.__pourcentage = points_joueur / len(liste_questions_aleatoires) * 100

        self.ajout_score()

        f.separation()
        menu()

    def ajout_score(self):
        """
        Permet d'ajouter un score à l'objet Utilisateur.
        """
        try:
            with open('fichier/scores.json', 'r') as file:
                dico_python = json.load(file)
                dico_python[joueur.nom][self.__theme].append([round(self.__pourcentage, 2), self.__date])
            with open('fichier/scores.json', 'w') as fichier:
                dico_json = json.dumps(dico_python)
                fichier.write(dico_json)

        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')


# initialisation
"""
Initalise les informations de l'application, telles que
la librairie, les thèmes, les questions et réponses.
Initialise ces informations en global pour que tout le monde
puisse y accéder de n'importe où.
"""
librairie = Bibliotheque("Application", "fichier/themes.csv")

themes = librairie.retourne_fichier_bibliotheque()
for theme in themes:
    for nom in theme:
        librairie.initialisation_theme(nom)

for theme_fichier in librairie.retourne_themes():
    liste_questions = f.recup_donnees_fichier(theme_fichier[1])
    for question in liste_questions:
        liste_reponses = []
        for reponse in range(2, len(question)):
            if question[reponse] == question[1]:
                liste_reponses.append([question[reponse], True])

            else:
                liste_reponses.append([question[reponse], False])
        librairie.recuperer_theme(theme_fichier[1]).creation_question(question[0], liste_reponses)


def introduction():
    """
    Lance l'application en demandant le pseudo du joueur.
    Si le joueur est déjà encodé dans la base, on affiche ses scores précédents.
    Si il n'est pas encore encodé, son pseudo est enregistré dans l'application.
    """
    try:
        with open('fichier/scores.json') as file:
            dictionnaire = json.load(file)

            if joueur.nom not in dictionnaire:
                dictionnaire[joueur.nom] = joueur.init_resultats()
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
                joueur.resultats(dictionnaire)
                f.separation()
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
    for i in range(len(librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + librairie.retourne_themes()[i][0])
    print("RETOUR??")
    print("")

    choix_theme = f.validation_question("Choisissez un thème.", len(librairie.retourne_themes()))
    f.separation()

    theme_manche = librairie.retourne_themes()[choix_theme - 1][0]
    joueur.creation_manche(theme_manche)


def ajouter_question():
    """
    Ajoute une question et ses réponses dans le thème précisé (dans l'objet Bibliothèque
    et dans le fichier du thème précisé).
    """
    print("Thèmes : ")
    for i in range(len(librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + librairie.retourne_themes()[i][0])
    print("")
    choix_theme = f.validation_question("Choisissez un thème dans lequel rajouter une question.",
                                        len(librairie.retourne_themes()))

    theme_a_modifier = librairie.recuperer_theme(librairie.retourne_themes()[choix_theme - 1][0])

    f.separation()
    question_ajouter = input("Entrez la question : ")
    print("\nVous allez maintenant devoir entrer des réponses. Une seule réponse peut être bonne, "
          "les 3 autres doivent être fausses.")
    print("L'ordre n'a pas d'importance.\n")

    reponses_liste = []
    for i in range(4):
        reponse_ajouter = input("Entrez la réponse " + str(i + 1) + " : ")
        reponses_liste.append(reponse_ajouter)
    print("")

    bonne_reponse = f.validation_question("Quelle réponse est la bonne ? \
                                                Entrez le numéro de la réponse.", 4) - 1

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

    f.separation()

    print("La question '" + question_ajouter + "' a été rajoutée dans le thème '" +
          librairie.retourne_themes()[choix_theme - 1][0] + "', avec '" + reponses_liste[bonne_reponse + 2] +
          "' comme bonne réponse !")

    f.separation()

    refaire = f.validation_oui_non("Voulez-vous rajouter une nouvelle question ?")
    f.separation()
    if refaire == "oui":
        ajouter_question()
    else:
        modifier()


def supprimer_question():
    """
    Supprime une question et ses réponses dans le thème précisé (dans l'objet Bibliothèque
    et dans le fichier du thème précisé).
    """
    print("Thèmes : ")
    for i in range(len(librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + librairie.retourne_themes()[i][0])
    print("")
    choix_theme = f.validation_question("Choisissez le thème dans lequel supprimer une question",
                                        len(librairie.retourne_themes()))

    theme_a_modifier = librairie.recuperer_theme(librairie.retourne_themes()[choix_theme - 1][0])
    f.separation()

    print("Questions du thème '" + librairie.retourne_themes()[choix_theme - 1][0] + "' :")
    indice = 1
    questions_theme = list(theme_a_modifier.retourne_question_theme().keys())
    for question_supprimer in questions_theme:
        print("    " + str(indice) + ". " + question_supprimer)
        indice += 1
    print("")

    question_a_supprimer = f.validation_question("Choisissez la question à supprimer.", indice - 1)
    f.separation()

    valider_question = f.validation_oui_non("Etes-vous sur de vouloir supprimer la question '" +
                                            questions_theme[question_a_supprimer - 1] + "' ?")
    if valider_question == "oui":
        theme_a_modifier.suppression_question(questions_theme[question_a_supprimer - 1])
        print("\nLa question '" + questions_theme[question_a_supprimer - 1] + "' a été supprimée !")

    else:
        print("\nAnnulation. Aucune question n'a été supprimée.")

    f.separation()
    modifier()


def ajouter_theme():
    """
    Permet de créer un thème et de l'ajouter à l'application (en lui créant un fichier, en notant son nom dans le
    fichier thèmes, et en le rajoutant à la liste de thèmes).
    """
    nouveau_theme = input("Quel est le nom du thème que vous voulez ajouter : ")
    librairie.creation_theme(nouveau_theme)

    f.separation()
    modifier()


def supprimer_theme():
    """
    Permet de supprimer un thème en l'enlevant de l'application (en supprimant son fichier, et en le retirant du fichier
    des thèmes et de la liste des thèmes).
    """
    print("Thèmes : ")
    for i in range(len(librairie.retourne_themes())):
        print("    " + str(i + 1) + ". " + librairie.retourne_themes()[i][0])
    print("")

    numero_theme = f.validation_question("Quel thème voulez-vous supprimer ? ", len(librairie.retourne_themes()))
    f.separation()

    validation_theme = f.validation_oui_non("Etes-vous sur de vouloir supprimer le thème '" +
                                            librairie.retourne_themes()[numero_theme - 1][0] + "' ?")
    if validation_theme == "oui":
        print("\nLe thème '" + librairie.retourne_themes()[numero_theme - 1][0] + "' a été supprimé !")
        librairie.suppression_theme(librairie.retourne_themes()[numero_theme - 1][1][8:], numero_theme - 1)

    else:
        print("\nAnnulation. Aucun thème n'a été supprimé.")

    f.separation()
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
    mode = f.validation_question("Choisissez une option.", 5)
    f.separation()
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
        menu()


def quitter():
    """
    Permet de fermer le programme. Si on veut le relancer, il faudra l'exécuter à nouveau.
    """
    print("Au revoir ", joueur.nom, ".\n")
    print("Application fermée.")


def menu():
    """
    Affiche les différentes options dans le menu et appelle la fonction selon le choix du joueur.
    """
    print("Menu :")
    print("    1. Jouer")
    print("    2. Modifier")
    print("    3. Quitter")
    print("")
    mode = f.validation_question("Choisissez une option.", 3)
    f.separation()

    if mode == 1:
        jouer()
    elif mode == 2:
        modifier()
    elif mode == 3:
        quitter()


pseudo = input("Bonjour. Veuillez entrez votre pseudo : ")
joueur = Utilisateur(pseudo)


def lancement_application():
    f.separation()
    dico_scores = introduction()
    menu()
    # dessin = cg.Graphique(dico_scores)
