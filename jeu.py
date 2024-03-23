import unittest


class Plateau:
    """Classe représentant le plateau de jeu."""
    def __init__(self):
        """Initialise le plateau avec une grille vide de 10x10."""
        self.grille = [[0] * 10 for _ in range(10)]

    def position_valide(self, x, y):
        """Vérifie si les coordonnées (x, y) sont valides sur le plateau."""
        return 0 <= x < 10 and 0 <= y < 10

    def placer_joueur(self, joueur):
        """Place le joueur sur le plateau s'il se trouve sur une position valide."""
        if self.position_valide(joueur.x, joueur.y):
            self.grille[joueur.y][joueur.x] = 1

    def effacer_joueur(self, joueur):
        """Efface la position du joueur sur le plateau."""
        if self.position_valide(joueur.x, joueur.y):
            self.grille[joueur.y][joueur.x] = 0


class TestPlateau(unittest.TestCase):
    """Classe de test pour la classe Plateau."""
    def test_placer_joueur(self):
        """Teste la fonction placer_joueur."""
        plateau = Plateau()
        joueur = Joueur(2, 3, 'haut')
        plateau.placer_joueur(joueur)
        self.assertEqual(plateau.grille[3][2], 1)

    def test_effacer_joueur(self):
        """Teste la fonction effacer_joueur."""
        plateau = Plateau()
        joueur = Joueur(2, 3, 'haut')
        plateau.placer_joueur(joueur)
        plateau.effacer_joueur(joueur)
        self.assertEqual(plateau.grille[3][2], 0)


class Joueur:
    """Classe représentant un joueur."""
    def __init__(self, x, y, direction):
        """Initialise les coordonnées et la direction du joueur."""
        self.x = x
        self.y = y
        self.direction = direction  # 'haut', 'gauche', 'droite'

    def tourner_gauche(self):
        """Fait tourner le joueur vers la gauche."""
        if self.direction == 'haut':
            self.direction = 'gauche'
        elif self.direction == 'gauche':
            self.direction = 'bas'
        elif self.direction == 'bas':
            self.direction = 'droite'
        else:
            self.direction = 'haut'

    def tourner_droite(self):
        """Fait tourner le joueur vers la droite."""
        if self.direction == 'haut':
            self.direction = 'droite'
        elif self.direction == 'droite':
            self.direction = 'bas'
        elif self.direction == 'bas':
            self.direction = 'gauche'
        else:
            self.direction = 'haut'

    def bouger(self, distance):
        """Déplace le joueur d'une ou deux cases dans sa direction actuelle."""
        if distance not in (1, 2):
            raise ValueError("La distance doit être de 1 ou 2")

        if self.direction == 'haut':
            self.y -= min(distance, self.y)
        elif self.direction == 'bas':
            self.y += min(distance, 9 - self.y)
        elif self.direction == 'gauche':
            self.x -= min(distance, self.x)
        else:
            self.x += min(distance, 9 - self.x)


class TestJoueur(unittest.TestCase):
    """Classe de test pour la classe Joueur."""
    def test_bouger_haut(self):
        """Teste la fonction bouger en déplaçant le joueur vers le haut."""
        joueur = Joueur(5, 5, 'haut')
        joueur.bouger(2)
        self.assertEqual(joueur.y, 3)

    def test_bouger_bas(self):
        """Teste la fonction bouger en déplaçant le joueur vers le bas."""
        joueur = Joueur(5, 5, 'bas')
        joueur.bouger(1)
        self.assertEqual(joueur.y, 6)

    def test_bouger_gauche(self):
        """Teste la fonction bouger en déplaçant le joueur vers la gauche."""
        joueur = Joueur(5, 5, 'gauche')
        joueur.bouger(2)
        self.assertEqual(joueur.x, 3)

    def test_bouger_droite(self):
        """Teste la fonction bouger en déplaçant le joueur vers la droite."""
        joueur = Joueur(5, 5, 'droite')
        joueur.bouger(1)
        self.assertEqual(joueur.x, 6)

class Visibilite:
    """Classe représentant la visibilité du joueur sur le plateau."""
    def __init__(self, plateau):
        """Initialise la visibilité avec le plateau de jeu."""
        self.plateau = plateau

    def ligne_visible(self, joueur):
        """Retourne les cases visibles dans la ligne directe du joueur."""
        x, y = joueur.x, joueur.y
        visible = []

        if joueur.direction == 'haut':
            for i in range(y - 1, -1, -1):
                if self.plateau.position_valide(x, i):
                    visible.append((x, i))
                else:
                    break 
        elif joueur.direction == 'bas':
            for i in range(y + 1, 10):
                if self.plateau.position_valide(x, i):
                    visible.append((x, i))
                else:
                    break
        elif joueur.direction == 'gauche':
            for i in range(x - 1, -1, -1):
                if self.plateau.position_valide(i, y):
                    visible.append((i, y))
                else:
                    break
        elif joueur.direction == 'droite':
            for i in range(x + 1, 10):  # Parcours des colonnes vers la droite
                if self.plateau.position_valide(i, y):
                    visible.append((i, y))
                else:
                    break

        return visible

class TestVisibilite(unittest.TestCase):
    """Classe de test pour la classe Visibilite."""
    def setUp(self):
        """Initialise les objets nécessaires pour les tests."""
        self.plateau = Plateau()
        self.visibilite = Visibilite(self.plateau)

    def test_ligne_visible_haut(self):
        """Teste la visibilité lorsque le joueur regarde vers le haut."""
        joueur = Joueur(5, 5, 'haut')  # Joueur au centre du plateau, face vers le haut
        visible = self.visibilite.ligne_visible(joueur)
        self.assertEqual(len(visible), 5)  # Le joueur devrait voir 5 cases vers le haut

    def test_ligne_visible_bas(self):
        """Teste la visibilité lorsque le joueur regarde vers le bas."""
        joueur = Joueur(5, 5, 'bas')  # Joueur au centre du plateau, face vers le bas
        visible = self.visibilite.ligne_visible(joueur)
        self.assertEqual(len(visible), 4)  # Le joueur devrait voir 4 cases vers le bas

    def test_ligne_visible_gauche(self):
        """Teste la visibilité lorsque le joueur regarde vers la gauche."""
        joueur = Joueur(5, 5, 'gauche')  # Joueur au centre du plateau, face vers la gauche
        visible = self.visibilite.ligne_visible(joueur)
        self.assertEqual(len(visible), 5)  # Le joueur devrait voir 5 cases vers la gauche

    def test_ligne_visible_droite(self):
        """Teste la visibilité lorsque le joueur regarde vers la droite."""
        joueur = Joueur(5, 5, 'droite')  # Joueur au centre du plateau, face vers la droite
        visible = self.visibilite.ligne_visible(joueur)
        self.assertEqual(len(visible), 4)  # Le joueur devrait voir 4 cases vers la droite


def fin_du_jeu(joueur1, joueur2):
    """Vérifie si un joueur a gagné en se retrouvant sur la même case que l'autre joueur."""
    return joueur1.x == joueur2.x and joueur1.y == joueur2.y


class TestFinDuJeu(unittest.TestCase):
    """Classe de test pour la fonction de fin du jeu."""
    def test_fin_du_jeu_false(self):
        """Teste le cas où le jeu n'est pas terminé."""
        joueur1 = Joueur(3, 4, 'haut')
        joueur2 = Joueur(7, 7, 'droite')
        self.assertFalse(fin_du_jeu(joueur1, joueur2))

    def test_fin_du_jeu_true(self):
        """Teste le cas où un joueur a gagné."""
        joueur1 = Joueur(3, 4, 'haut')
        joueur2 = Joueur(3, 4, 'haut')
        self.assertTrue(fin_du_jeu(joueur1, joueur2))


if __name__ == '__main__':
    unittest.main()