# -*- coding: utf-8 -*-

from simplification import fonctions as f
from classe import utilisateur as ut
from classe import question_reponse as qr
from classe import theme as th
from classe import bibliotheque as bi
from classe import variable_globale as vg
import unittest


class CultureGeneraleTest(unittest.TestCase):

    def test_reponse(self):
        a = qr.Reponse(1, True)
        self.assertEqual(a.nom_reponse, 1)
        self.assertEqual(a.type_reponse, True)

    def test_question(self):
        obj1 = qr.Question("2 + 2 = ?")
        obj1.creation_reponses([["4", True], ["7", False], ["12", False], ["3", False]])
        self.assertEqual(qr.Question("Quelle est la capitale de la Belgique ?").nom_question,
                         "Quelle est la capitale de la Belgique ?")
        self.assertEqual(obj1.reponses, [["4", True], ["7", False], ["12", False], ["3", False]])

    def test_theme(self):
        c = th.Theme('geographie.csv')
        c.initialisation_question(["Que fait 3-2", 1, 1, 2, 5, 7])
        self.assertEqual(c.nom_theme, 'geographie')
        self.assertEqual(c.nom_fichier, 'ressources/geographie.csv')
        self.assertEqual(c.question_theme, {'Que fait 3-2': [[1, True], [2, False], [5, False], [7, False]]})

    def test_utilisateurs(self):
        d = ut.Utilisateur('pouspous')
        self.assertEqual(d.nom, 'pouspous')
        self.assertEqual(d.init_resultats(), {'geographie': [], 'math': []})

    def test_aleatoire(self):
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 4)), 4)
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 1)), 1)

    def test_recup_donnees_fichier(self):
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier('./'))

    def test_recup_donnees_fichier_json(self):
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier_json("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier_json('./'))

    def test_bibliotheque(self):
        Bibli = bi.Bibliotheque('librairie', "./ressources/themes.csv")
        Bibli.initialisation_theme('math.csv')

        self.assertEqual(Bibli.nom_bibliotheque, 'librairie')
        self.assertEqual(Bibli.nom_fichier_bibliotheque, [['geographie.csv'], ['math.csv']])
        self.assertEqual(Bibli.retourne_themes(), ['math'])
        self.assertEqual(len(Bibli.liste_themes), 1)
        self.assertEqual(Bibli.recuperer_theme('test'), '')
        self.assertEqual(Bibli.dictionnaire_themes, {'math': {}})

    def test_clem_biblio(self):
        # test un theme qui n'est pas dans la liste
        Bibli = bi.Bibliotheque('librairie', "./ressources/themes.csv")
        obj = th.Theme('geo.csv')
        self.assertRaises(ValueError, lambda: Bibli.suppression_theme(obj))

        # test une bibliotheque qui a un nom de fichier inexistant en suppresion de theme
        obj_b1 = bi.Bibliotheque("test1", "fichier_inexistant.csv")
        obj_b1.initialisation_theme("math.csv")
        obj_t1 = obj_b1.recuperer_theme("math")
        ######self.assertRaises(FileNotFoundError, lambda: obj_b1.suppression_theme(obj_t1))

        # test une bibliotheque qui a un nom de fichier vide en suppresion de theme
        obj_b2 = bi.Bibliotheque("test2", "")
        obj_b2.initialisation_theme("math.csv")
        obj_t2 = obj_b2.recuperer_theme("math")
        ######self.assertRaises(IOError, lambda: obj_b2.suppression_theme(obj_t2))

        # test une bibliotheque qui a un nom de fichier inexistant en création de theme
        #######self.assertRaises(FileNotFoundError, lambda: obj_b1.creation_theme("math"))

        # test une bibliotheque qui a un nom de fichier vide en création de theme
        ######self.assertRaises(IOError, lambda: obj_b2.creation_theme("math"))

    def test_clem_theme(self):
        question = ["ques", "bonrep", "rep1", "rep2", "rep3", "rep4"]

        # test d'un theme qui a un nom de fichier inexistant en creation de question
        obj_t3 = th.Theme("inexistant.csv")
        #########self.assertRaises(FileNotFoundError, lambda: obj_t3.creation_question(question))

        # test d'un theme qui a un nom de fichier vide en creation de question
        obj_t4 = th.Theme("")
        self.assertRaises(IOError, lambda: obj_t4.creation_question(question))

        # test une question qui n'est pas dans la liste
        question_a_supp = "question"
        self.assertRaises(KeyError, lambda: obj_t3.suppression_question(question_a_supp))

        # test d'un theme qui a un nom de fichier inexistant en suppression de question
        obj_t3.initialisation_question(question)
        ######self.assertRaises(FileNotFoundError, lambda: obj_t3.suppression_question("ques"))

        # test d'un theme qui a un nom de fichier vide en suppression de question
        obj_t4.initialisation_question(question)
        self.assertRaises(IOError, lambda: obj_t4.suppression_question("ques"))

    def test_clem_global(self):
        vg.initialisation_informations()
        self.assertEqual(vg.librairie.nom_bibliotheque, "Application")
