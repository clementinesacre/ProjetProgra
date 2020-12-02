from Simplification import fonctions as f
import unittest


class CultureGeneraleTest(unittest.TestCase):
    """def test_aleatoire(self):
        self.assertEqual(len(cl.aleatoire([], 10), )"""

    def test_recup_donnees_fichier(self):
        self.assertEqual(f.recup_donnees_fichier("../fichier/geographie.csv"),
                         [['Combien vaut 2 + 2 = ?', '4', '3', '8', '4', '12'],
                          ['Quelle est la capitale de la Belgique ?', 'Bruxelles', 'Bruxelles', 'Namur',
                           'Ostende', 'Liege']])
        self.assertRaises(FileNotFoundError, lambda: f.recup_donnees_fichier("azerty"))
        self.assertRaises(IOError, lambda: f.recup_donnees_fichier(""))

    def test_validation_question(self):
        self.assertEqual(f.validation_question("Coucou", 10), 2)
        #self.assertRaises(IOError, lambda: f.recup_donnees_fichier("a"))

    def test_validation_oui_non(self):
        self.assertEqual(f.validation_oui_non("Coucou"), "oui")


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
