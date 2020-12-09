# -*- coding: utf-8 -*-

from simplification import fonctions as f
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
        #self.assertEqual(f.validation_question("Coucou", 10), 2)
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier("a"))

    def test_validation_oui_non(self):
        pass
        #self.assertEqual(f.validation_oui_non("Coucou"), "oui")

    def test_recup_donnees_fichier_json(self):
        donnees = {'test': {'geographie': [[54, '14/09/2020']], 'math': [[92.1, '19/09/2020']]}, 'clem':
            {'geographie': [[100.0, '02/12/2020'], [100.0, '02/12/2020'], [100.0, '08/12/2020'], [0.0, '08/12/2020'],
                            [100.0, '08/12/2020'], [0.0, '08/12/2020'], [0.0, '08/12/2020'], [100.0, '08/12/2020'],
                            [100.0, '08/12/2020'], [100.0, '08/12/2020']], 'math': [[100.0, '25/11/2020'],
                            [100.0, '25/11/2020'], [50.0, '25/11/2020'], [100.0, '25/11/2020'], [0.0, '25/11/2020'],
                            [100.0, '25/11/2020'], [100.0, '25/11/2020'], [100.0, '25/11/2020'], [100.0, '01/12/2020'],
                            [0.0, '01/12/2020'], [50.0, '02/12/2020'], [100.0, '02/12/2020'], [50.0, '02/12/2020'],
                            [50.0, '02/12/2020'], [100.0, '02/12/2020'], [0.0, '02/12/2020'], [0.0, '02/12/2020'],
                            [50.0, '02/12/2020'], [33.33, '02/12/2020'], [100.0, '08/12/2020'], [100.0, '08/12/2020'],
                            [0.0, '08/12/2020'], [100.0, '08/12/2020'], [0.0, '08/12/2020'], [0.0, '08/12/2020'],
                            [100.0, '08/12/2020'], [100.0, '08/12/2020'], [100.0, '08/12/2020'],
                            [100.0, '08/12/2020']]}, 'pouspous': {'geographie': [], 'math': []},
                   'Pouspous ': {'geographie': [], 'math': []}, 'cle': {'geographie': [], 'math': []}}

        self.assertEqual(f.recup_donnees_fichier_json("../ressources/scores.json"), donnees)
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_nom_utilisateur(self):
        pass





if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
