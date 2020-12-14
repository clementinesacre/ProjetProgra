# -*- coding: utf-8 -*-

from simplification import fonctions as f
from classe import utilisateur as ut
from classe import question_reponse as qr
from classe import theme as th
from classe import bibliotheque as bi
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
        c.initialisation_question(["Que fait 3-2", 1])
        self.assertEqual(c.nom_theme, 'geographie')
        self.assertEqual(c.nom_fichier, 'ressources/geographie.csv')
        self.assertEqual(c.question_theme, {'Que fait 3-2': []})
        # self.assertEqual(type(c.recuperer_question("Que fait 3-2")), "<class 'classe.question_reponse.Question'>")
        # self.assertRaises(FileNotFoundError, lambda: c.creation_question(["Que fait 5-2"]))
        # self.assertEqual(IOError, lambda: c.creation_question([""]))
        # self.assertRaises(FileNotFoundError, lambda: c.suppression_question('geo'))
        # self.assertRaises(IOError, lambda: c.suppression_question(''))

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
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier("a"))
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_utilisateur(self):
        self.assertEqual(ut.Utilisateur("clem").nom, "clem")
        self.assertEqual(ut.Utilisateur("clem").init_resultats(), {'geographie': [], 'math': []})

    def test_bibliotheque(self):
        Bibli = bi.Bibliotheque('librairie', "./ressources/themes.csv")
        Bibli.initialisation_theme('math.csv')
        obj = th.Theme('geo.csv')
        obj2 = th.Theme('')

        self.assertEqual(Bibli.nom_bibliotheque, 'librairie')
        self.assertEqual(Bibli.nom_fichier_bibliotheque,[['geographie.csv'], ['math.csv']])
        self.assertEqual(Bibli.retourne_themes(), ['math'])
        self.assertEqual(len(Bibli.liste_themes), 1)
        self.assertEqual(Bibli.recuperer_theme('test'), '')
        self.assertEqual(Bibli.dictionnaire_themes,  {'math': {}})
        self.assertRaises(FileNotFoundError, lambda: Bibli.suppression_theme(obj))
        self.assertRaises(IOError, lambda: Bibli.suppression_theme(obj2))


