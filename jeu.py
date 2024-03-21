import unittest

#Créer une grille de 10*10

#Faire une fonction de déplacement
#Faire la fonction de pivot droite
#Faire la fonction de pivot gauche
#Faire la fonction d'avancer 1 ou 2 cases
#Exception sortie de grille ce qui annule le mouvement
#Le joueur ne peut voir que ce qu'il y a devant lui 

#classe joueur 

import unittest

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
        if self.direction == 'haut':
            self.y -= min(distance, self.y)
        elif self.direction == 'bas':
            self.y += min(distance, 9 - self.y)
        elif self.direction == 'gauche':
            self.x -= min(distance, self.x)
        else:
            self.x += min(distance, 9 - self.x)


class TestJoueur(unittest.TestCase):
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
