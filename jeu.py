import unittest

class Plateau:
    def __init__(self):
        self.grille = [[0] * 10 for _ in range(10)]  # Crée une grille vide de 10x10

    def position_valide(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10

    def placer_joueur(self, joueur):
        if self.position_valide(joueur.x, joueur.y):
            self.grille[joueur.y][joueur.x] = 1

    def effacer_joueur(self, joueur):
        if self.position_valide(joueur.x, joueur.y):
            self.grille[joueur.y][joueur.x] = 0

    def afficher_plateau(self):
        for ligne in self.grille:
            print(' '.join(map(str, ligne)))


class TestPlateau(unittest.TestCase):
    def test_placer_joueur(self):
        plateau = Plateau()
        joueur = Joueur(2, 3, 'haut')
        plateau.placer_joueur(joueur)
        self.assertEqual(plateau.grille[3][2], 1)

    def test_effacer_joueur(self):
        plateau = Plateau()
        joueur = Joueur(2, 3, 'haut')
        plateau.placer_joueur(joueur)
        plateau.effacer_joueur(joueur)
        self.assertEqual(plateau.grille[3][2], 0)


class Joueur:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction  # 'haut', 'bas', 'gauche', 'droite'

    def tourner_gauche(self):
        if self.direction == 'haut':
            self.direction = 'gauche'
        elif self.direction == 'gauche':
            self.direction = 'bas'
        elif self.direction == 'bas':
            self.direction = 'droite'
        else:
            self.direction = 'haut'

    def tourner_droite(self):
        if self.direction == 'haut':
            self.direction = 'droite'
        elif self.direction == 'droite':
            self.direction = 'bas'
        elif self.direction == 'bas':
            self.direction = 'gauche'
        else:
            self.direction = 'haut'

    def bouger(self, distance):
        new_x, new_y = self.x, self.y
        if self.direction == 'haut':
            new_y -= min(distance, self.y)
        elif self.direction == 'bas':
            new_y += min(distance, 9 - self.y)
        elif self.direction == 'gauche':
            new_x -= min(distance, self.x)
        else:
            new_x += min(distance, 9 - self.x)

        # Vérifier si les nouvelles coordonnées sont valides
        if 0 <= new_x < 10 and 0 <= new_y < 10:
            self.x, self.y = new_x, new_y

class TestJoueur(unittest.TestCase):
    def test_bouger_haut_limite(self):
        joueur = Joueur(0, 0, 'haut')  # Le joueur est positionné dans le coin supérieur gauche
        joueur.bouger(2)  # Essayer de se déplacer vers le haut de 2 cases depuis la position actuelle (0, 0)
        self.assertEqual(joueur.x, 0)  # Les coordonnées x ne devraient pas changer
        self.assertEqual(joueur.y, 0)  # Les coordonnées y ne devraient pas changer

    def test_bouger_bas_limite(self):
        joueur = Joueur(5, 9, 'bas')  # Le joueur est positionné dans le coin inférieur droit
        joueur.bouger(3)  # Essayer de se déplacer vers le bas de 3 cases depuis la position actuelle (5, 9)
        self.assertEqual(joueur.x, 5)  # Les coordonnées x ne devraient pas changer
        self.assertEqual(joueur.y, 9)  # Les coordonnées y ne devraient pas changer

    def test_bouger_gauche_limite(self):
        joueur = Joueur(0, 5, 'gauche')  # Le joueur est positionné sur le bord gauche
        joueur.bouger(4)  # Essayer de se déplacer vers la gauche de 4 cases depuis la position actuelle (0, 5)
        self.assertEqual(joueur.x, 0)  # Les coordonnées x ne devraient pas changer
        self.assertEqual(joueur.y, 5)  # Les coordonnées y ne devraient pas changer

    def test_bouger_droite_limite(self):
        joueur = Joueur(9, 2, 'droite')  # Le joueur est positionné sur le bord droit
        joueur.bouger(3)  # Essayer de se déplacer vers la droite de 3 cases depuis la position actuelle (9, 2)
        self.assertEqual(joueur.x, 9)  # Les coordonnées x ne devraient pas changer
        self.assertEqual(joueur.y, 2)  # Les coordonnées y ne devraient pas changer


    def test_tourner_gauche(self):
        joueur = Joueur(5, 5, 'haut')
        joueur.tourner_gauche()
        self.assertEqual(joueur.direction, 'gauche')

    def test_tourner_droite(self):
        joueur = Joueur(5, 5, 'haut')
        joueur.tourner_droite()
        self.assertEqual(joueur.direction, 'droite')

    def test_bouger_haut(self):
        joueur = Joueur(5, 5, 'haut')
        joueur.bouger(2)
        self.assertEqual(joueur.y, 3)

    def test_bouger_bas(self):
        joueur = Joueur(5, 5, 'bas')
        joueur.bouger(3)
        self.assertEqual(joueur.y, 8)

    def test_bouger_gauche(self):
        joueur = Joueur(5, 5, 'gauche')
        joueur.bouger(4)
        self.assertEqual(joueur.x, 1)

    def test_bouger_droite(self):
        joueur = Joueur(5, 5, 'droite')
        joueur.bouger(3)
        self.assertEqual(joueur.x, 8)


if __name__ == '__main__':
    unittest.main()
