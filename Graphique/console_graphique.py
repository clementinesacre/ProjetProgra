import tkinter as tk


class Graphique:
    def __init__(self, dictionnaire):
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
        self.__canv.pack()

        self.__liste_joueur = []
        self.__liste_theme = []
        self.__liste_score = []
        self.__joueur_courant = "jack"

        self.__quitter = tk.Button(self.__racine, text="Back", height=2, width=15, bg='#5D5F56', fg='#ffffff', bd=1,
                                   activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                   command=lambda: self.revenir_menu())
        self.__titre_joueur = tk.Label(self.__racine, text="Noms des joueurs :", bg='#E7EBD6', height=2, width=18,
                                       fg='#5D5F56', font=10)

        self.initialisation()

    def initialisation(self):
        self.__titre_joueur.place(x=16, y=20)

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        for joueur in self.__dic:
            button1 = tk.Button(self.__racine, text=joueur, height=2, width=15, bg='#86887F', fg='#ffffff', bd=1,
                                activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                command=lambda nom=joueur: self.matieres(nom))
            button1.place(x=x_initial * compteur_x + 15, y=y_initial * compteur_y)
            self.__liste_joueur.append(button1)
            if (y_initial * compteur_y) >= 400:
                compteur_x = 5
                compteur_y = 0
            compteur_y += 1

        self.__racine.mainloop()

    def matieres(self, joueur):
        self.__joueur_courant = joueur
        for bouton in self.__liste_joueur:
            bouton.destroy()
        self.__titre_joueur.destroy()

        self.__quitter.place(x=20, y=20)

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        for theme in self.__dic[self.__joueur_courant]:
            if len(self.__dic[self.__joueur_courant][theme]) > 0:
                button2 = tk.Button(self.__racine, text=theme, height=2, width=15, bg='#86887F', fg='#ffffff', bd=1,
                                    activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                    command=lambda nom=theme: self.points(nom))
                button2.place(x=x_initial * compteur_x + 17, y=y_initial * compteur_y)
                self.__liste_theme.append(button2)
                if (y_initial * compteur_y) >= 400:
                    compteur_x = 5
                    compteur_y = 0
                compteur_y += 1

    def points(self, theme):
        for bouton in self.__liste_theme:
            bouton.destroy()

        self.__quitter.place(x=20, y=20)

        x_initial = 40
        y_initial = 80
        compteur_x = 1
        compteur_y = 1
        base = 400
        for score in self.__dic[self.__joueur_courant][theme]:
            label = tk.Label(self.__racine, text=(str(score[1]) + " : " + str(score[0]) + "%"), bg='#FF9966', height=2,
                             width=17, fg='#000000', relief="sunken")
            label.place(x=x_initial * compteur_x + 17, y=y_initial * compteur_y)
            if (y_initial * compteur_y) > base - 50:
                compteur_x += 4
                compteur_y = 0
            compteur_y += 1
            self.__liste_score.append(label)

    def revenir_menu(self):
        for points in self.__liste_score:
            points.destroy()
        for theme in self.__liste_theme:
            theme.destroy()
        self.__quitter.destroy()
        self.__quitter = tk.Button(self.__racine, text="Back", height=2, width=15, bg='#5D5F56', fg='#ffffff', bd=1,
                                   activebackground='#FFFFFF', activeforeground='#CCCCFF', cursor='circle',
                                   command=lambda: self.revenir_menu())
        self.__titre_joueur = tk.Label(self.__racine, text="Noms des joueurs :", bg='#E7EBD6', height=2, width=18,
                                       fg='#5D5F56', font=10)
        self.initialisation()


"""
k =  {"test": {"geographie": [[54, "14/09/2020"]], "math": [[92.1, "19/09/2020"]]}, "clem": {"geographie": [],
    "math": [[100.0, "25/11/2020"], [100.0, "25/11/2020"], [50.0, "25/11/2020"], [100.0, "25/11/2020"],
    [0.0, "25/11/2020"], [100.0, "25/11/2020"], [100.0, "25/11/2020"], [100.0, "25/11/2020"], [10, "cc"],
    [20, "ll"], [100.0, "25/11/2020"], [100.0, "25/11/2020"], [50.0, "25/11/2020"], [100.0, "25/11/2020"]]},
      "gui" : {"geographie": [[36, "11/09/2020"]], "math": [[82.1, "19/19/2020"]]}}

obj1 = Graphique(k)"""
