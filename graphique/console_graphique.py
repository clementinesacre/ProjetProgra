import tkinter as tk
import logging
logger = logging.getLogger("cultureg")

class Graphique:
    def __init__(self, dictionnaire):
        """
        Permet d'initialiser les différentes fonctionnalités de la librairie graphique.

        PRE : 'dictionnaire' est un dictionnaire avec des pseudo comme clés et des autres dictionnaires comme valeurs.
        Ces autres dictionnaires contiennent des thèmes comme clés, et des listes de listes de scores comme valeurs.
        POST : Crée la fenêtre, et la lance, crée le bouton pour revenir en arrière et le titre. Appelle la fonction
        qui place ces dernières données.
        """
        self.__dic = dictionnaire
        self.__racine = tk.Tk(className='Application')
        a_rajouter = 2
        maximum = 15
        for i in self.__dic:
            for j in self.__dic[i]:
                if len(self.__dic[i][j]) > maximum:
                    maximum = len(self.__dic[i][j])
                    a_rajouter = len(self.__dic[i][j]) + 1
        self.__canv = tk.Canvas(self.__racine, bg="#E7EBD6", height=500, width=525 + a_rajouter * 17)
        logger.info('graphique/console_graphique.py : __init__() : Création de tk.Canvas')
        self.__canv.pack()
        logger.info('graphique/console_graphique.py : __init__() : Mise en place de tk.Canvas')

        self.__liste_joueur = []
        self.__liste_theme = []
        self.__liste_score = []
        self.__joueur_courant = "jack"

        self.__quitter = tk.Button(self.__racine, text="Back", height=2, width=15, bg='#5D5F56', fg='#ffffff', bd=1,
                                   activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                   command=lambda: self.revenir_menu())
        logger.info('graphique/console_graphique.py : __init__() : Création de tk.Button quitter')

        self.__titre_joueur = tk.Label(self.__racine, text="Noms des joueurs :", bg='#E7EBD6', height=2, width=18,
                                       fg='#5D5F56', font=10)
        logger.info('graphique/console_graphique.py : __init__() : Création de tk.Label titre_joueur')

        self.initialisation()

    def initialisation(self):
        """
        Permet d'afficher les différents pseudos.

        PRE : -
        POST : Crée et place les boutons contenant les pseudos des joueurs. Place également le bouton permettant de
        revenir en arrière, et le titre.
        """
        self.__titre_joueur.place(x=16, y=20)
        logger.info('graphique/console_graphique.py : initialisation() : Placement de tk.Label titre_joueur')

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        for joueur in self.__dic:
            button1 = tk.Button(self.__racine, text=joueur, height=2, width=15, bg='#86887F', fg='#ffffff', bd=1,
                                activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                command=lambda nom=joueur: self.matieres(nom))
            logger.info('graphique/console_graphique.py : initialisation() : Création de tk.Button joueur : ' + joueur)
            button1.place(x=x_initial * compteur_x + 15, y=y_initial * compteur_y)
            logger.info('graphique/console_graphique.py : initialisation() : Placement de tk.Button joueur : ' + joueur)
            self.__liste_joueur.append(button1)
            if (y_initial * compteur_y) >= 400:
                compteur_x = 5
                compteur_y = 0
            compteur_y += 1

        self.__racine.mainloop()

    def matieres(self, joueur):
        """
        Permet d'afficher les différents thèmes contenant des scores d'un joueur.

        PRE : 'joueur' est une string.
        POST : Supprime les boutons créés et placés précédemment. Crée et place les boutons contenant les thèmes. Place
        également le bouton permettant de revenir en arrière.
        """
        self.__joueur_courant = joueur
        for bouton in self.__liste_joueur:
            bouton.destroy()
            logger.info('graphique/console_graphique.py : matieres() : Suppression de tk.Button joueurs')
        self.__titre_joueur.destroy()
        logger.info('graphique/console_graphique.py : matieres() : Suppression de tk.Label titre_joueurs')

        self.__quitter.place(x=20, y=20)
        logger.info('graphique/console_graphique.py : matieres() : Placement de tk.Button quitter')

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        for theme in self.__dic[self.__joueur_courant]:
            if len(self.__dic[self.__joueur_courant][theme]) > 0:
                button2 = tk.Button(self.__racine, text=theme, height=2, width=15, bg='#86887F', fg='#ffffff', bd=1,
                                    activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                    command=lambda nom=theme: self.points(nom))
                logger.info('graphique/console_graphique.py : matieres() : Création de tk.Button theme: ' + theme )
                button2.place(x=x_initial * compteur_x + 17, y=y_initial * compteur_y)
                logger.info('graphique/console_graphique.py : matieres() : Placement de tk.Button theme: ' + theme )

                self.__liste_theme.append(button2)
                if (y_initial * compteur_y) >= 400:
                    compteur_x = 5
                    compteur_y = 0
                compteur_y += 1

    def points(self, theme):
        """
        Permet d'afficher les différents scores d'un thème d'un joueur.

        PRE : 'thème' est une string.
        POST : Supprime les boutons créés et placés précédemment. Crée et place des zones de texte  avec les scores.
        Place également le bouton permettant de revenir en arrière.
        """
        for bouton in self.__liste_theme:
            bouton.destroy()
            logger.info('graphique/console_graphique.py : points() : Suppression de tk.Button themes')

        self.__quitter.place(x=20, y=20)
        logger.info('graphique/console_graphique.py : points() : Placement de tk.Button quitter')

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        base = 400
        for score in self.__dic[self.__joueur_courant][theme]:
            label = tk.Label(self.__racine, text=(str(score[1]) + " : " + str(score[0]) + "%"), bg='#FF9966', height=2,
                             width=17, fg='#000000', relief="sunken")
            logger.info('graphique/console_graphique.py : points() : Création de tk.Label score: ' + str(score))
            label.place(x=x_initial * compteur_x + 17, y=y_initial * compteur_y)
            logger.info('graphique/console_graphique.py : points() : Placement de tk.Label score: ' + str(score))
            if (y_initial * compteur_y) > base - 50:
                compteur_x += 4
                compteur_y = 0
            compteur_y += 1
            self.__liste_score.append(label)

    def revenir_menu(self):
        """
        Permet de revenir au menu principal avec les différents joueurs.

        PRE : -
        POST : Supprime les boutons créés et placés précédemment. Recrée le bouton qui permet de revenir en arrière et
        le titre.
        """
        for points in self.__liste_score:
            points.destroy()
            logger.info('graphique/console_graphique.py : revenir_menu() : Suppression de tk.Label scores')

        for theme in self.__liste_theme:
            theme.destroy()
            logger.info('graphique/console_graphique.py : revenir_menu() : Suppression de tk.Button theme')

        self.__quitter.destroy()
        logger.info('graphique/console_graphique.py : revenir_menu() : Suppression de tk.Button quitter')

        self.__quitter = tk.Button(self.__racine, text="Back", height=2, width=15, bg='#5D5F56', fg='#ffffff', bd=1,
                                   activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                   command=lambda: self.revenir_menu())
        logger.info('graphique/console_graphique.py : revenir_menu() : Création de tk.Button quitter')

        self.__titre_joueur = tk.Label(self.__racine, text="Noms des joueurs :", bg='#E7EBD6', height=2, width=18,
                                       fg='#5D5F56', font=10)
        logger.info('graphique/console_graphique.py : revenir_menu() : Création de tk.Label titre_joueur')

        self.initialisation()

