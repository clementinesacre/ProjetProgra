# -*- coding: utf-8 -*-

from simplification import fonctions as f
from classe import utilisateur as ut
from classe import question_reponse as qr
from classe import theme as th
import unittest


class CultureGeneraleTest(unittest.TestCase):
    def test_aleatoire(self):
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 4)), 4)
        self.assertEqual(len(f.aleatoire(['Combien vaut 2 + 2 = ?', 'Quelle est la racine carrée de 25 ?',
                                          'Quelle est le carré de 8 ?', 'Quel chiffre est un chiffre premier ?',
                                          'Quel chiffre est une puissance de 2 ?'], 1)), 1)

    def test_recup_donnees_fichier(self):
        self.assertEqual(f.recup_donnees_fichier("../ressources/geographie.csv"),
                         [['Combien vaut 2 + 2 = ?', '4', '3', '8', '4', '12'],
                          ['Quelle est la capitale de la Belgique ?', 'Bruxelles', 'Bruxelles', 'Namur',
                           'Ostende', 'Liege']])
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_validation_question(self):
        self.assertEqual(f.validation_question("Coucou", 10), 2) # pas ok input
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier("a"))

    def test_validation_oui_non(self):
        self.assertEqual(f.validation_oui_non("Coucou"), "oui") # pas ok input

    def test_recup_donnees_fichier_json(self):
        donnees = {'test': {'geographie': [[54, '14/09/2020']], 'math': [[92.1, '19/09/2020']]}, 'clem':
            {'geographie': [[100.0, '02/12/2020'], [100.0, '02/12/2020'], [100.0, '08/12/2020'], [0.0, '08/12/2020'],
                            [100.0, '08/12/2020'], [0.0, '08/12/2020'], [0.0, '08/12/2020'], [100.0, '08/12/2020'],
                            [100.0, '08/12/2020'], [100.0, '08/12/2020']], 'math': [[100.0, '25/11/2020'],
                                                                                    [100.0, '25/11/2020'],
                                                                                    [50.0, '25/11/2020'],
                                                                                    [100.0, '25/11/2020'],
                                                                                    [0.0, '25/11/2020'],
                                                                                    [100.0, '25/11/2020'],
                                                                                    [100.0, '25/11/2020'],
                                                                                    [100.0, '25/11/2020'],
                                                                                    [100.0, '01/12/2020'],
                                                                                    [0.0, '01/12/2020'],
                                                                                    [50.0, '02/12/2020'],
                                                                                    [100.0, '02/12/2020'],
                                                                                    [50.0, '02/12/2020'],
                                                                                    [50.0, '02/12/2020'],
                                                                                    [100.0, '02/12/2020'],
                                                                                    [0.0, '02/12/2020'],
                                                                                    [0.0, '02/12/2020'],
                                                                                    [50.0, '02/12/2020'],
                                                                                    [33.33, '02/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [0.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [0.0, '08/12/2020'],
                                                                                    [0.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020'],
                                                                                    [100.0, '08/12/2020']]},
                   'pouspous': {'geographie': [], 'math': []},
                   'Pouspous ': {'geographie': [], 'math': []}, 'cle': {'geographie': [], 'math': []}}

        self.assertEqual(f.recup_donnees_fichier_json("../ressources/scores.json"), donnees)
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


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
