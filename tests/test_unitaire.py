# -*- coding: utf-8 -*-

from simplification import fonctions as f
from classe import utilisateur as ut
from classe import question_reponse as qr
from classe import theme as th
from classe import bibliotheque as bi
import unittest


class CultureGeneraleTest(unittest.TestCase):
    def test_aleatoire(self):
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 4)), 4)
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 1)), 1)
        """self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 6)), 1)"""

    def test_recup_donnees_fichier(self):
        """self.assertEqual(f.recup_donnees_fichier("../ressources/geographie.csv"),
                         [['Combien vaut 2 + 2 = ?', '4', '3', '8', '4', '12'],
                          ['Quelle est la capitale de la Belgique ?', 'Bruxelles', 'Bruxelles', 'Namur',
                           'Ostende', 'Liege']])"""   # soucis de chemin
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_validation_question(self):
        # self.assertEqual(f.validation_question("Coucou", 10), 2) # pas ok input
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier("a"))

    def test_validation_oui_non(self):
        pass

    def test_recup_donnees_fichier_json(self):
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_utilisateur(self):
        self.assertEqual(ut.Utilisateur("clem").nom, "clem")
        self.assertEqual(ut.Utilisateur("clem").init_resultats(), {'geographie': [], 'math': []})

    def test_reponse(self):
        self.assertEqual(qr.Reponse("4", True).nom_reponse, "4")
        self.assertEqual(qr.Reponse("4", True).type_reponse, True)

    def test_question(self):
        self.assertEqual(qr.Question("Quelle est la capitale de la Belgique ?").nom_question,
                         "Quelle est la capitale de la Belgique ?")

        obj1 = qr.Question("2 + 2 = ?")
        obj1.creation_reponses([["4", True], ["7", False], ["12", False], ["3", False]])
        self.assertEqual(obj1.reponses, [["4", True], ["7", False], ["12", False], ["3", False]])

    def test_theme(self):
        obj2 = th.Theme("math.csv")
        self.assertEqual(obj2.nom_theme, "math")
        self.assertEqual(obj2.nom_fichier, "ressources/math.csv")

    def test_nom_bibliotheque(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").nom_bibliotheque, 'librairie')

    def test_nom_fichier_bibliothque(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").nom_fichier_bibliotheque,
                         [['geographie.csv'], ['math.csv']])

    def test_retourne_themes(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").retourne_themes(), [])

    def test_liste_themes(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").liste_themes, [])

    def test_recuperer_theme(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").recuperer_theme('math'), None)

    def test_dictionnaire_themes(self):
        self.assertEqual(bi.Bibliotheque('librairie', "./ressources/themes.csv").dictionnaire_themes, {})

    def test_suppression_theme(self):
        obj = th.Theme('geo.csv')
        obj2 = th.Theme('')
        self.assertRaises(FileNotFoundError, lambda: bi.Bibliotheque('librairie', "./ressources/themes.csv")
                          .suppression_theme(obj))
        self.assertRaises(IOError, lambda: bi.Bibliotheque('librairie', "./ressources/themes.csv")
                          .suppression_theme(obj2))


