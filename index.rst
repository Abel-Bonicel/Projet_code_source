.. Projet_code_source documentation master file, created by
   sphinx-quickstart on Sat Mar 23 10:54:38 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Projet_code_source's documentation!
==============================================

.. Mon Projet de Documentation
.. toctree::
   :maxdepth: 2
   :caption: Contenu :

   introduction
   installation
   utilisation
   module
   classe
   fonction
   conclusion

Introduction
=============

Bienvenue dans la documentation de mon Projet !

Présentation du Jeu
--------------------

Le jeu est un jeu de plateau stratégique où deux joueurs s'affrontent pour atteindre un objectif commun sur un plateau de jeu de taille 10x10. Chaque joueur contrôle un personnage représenté par une position sur le plateau et une direction dans laquelle il regarde.

Le but du jeu est de guider votre personnage vers la case où se trouve le personnage adverse. Le premier joueur à atteindre la même case que son adversaire remporte la partie.

Fonctionnalités Principales
----------------------------

- **Placer le joueur sur le plateau :** Permet de positionner un joueur sur une case valide du plateau.
- **Effacer la position du joueur :** Efface la position d'un joueur du plateau.
- **Tourner à gauche ou à droite :** Permet à un joueur de changer sa direction de regard.
- **Déplacer le joueur :** Déplace un joueur d'une ou deux cases dans la direction dans laquelle il regarde.
- **Déterminer la visibilité :** Calcule les cases visibles dans la ligne directe du joueur.
- **Vérifier la fin du jeu :** Verifie si l'un des joueurs a gagné en se retrouvant sur la même case que l'autre joueur.

Cette documentation vise à fournir une référence complète pour comprendre le fonctionnement interne du jeu et à faciliter le développement de fonctionnalités supplémentaires.



Installation
============

Pour commencer à travailler sur le code source de ce jeu, suivez les étapes ci-dessous pour configurer votre environnement de développement.

1. **Configuration de la Machine Virtuelle :**

    - Créez une machine virtuelle à l'aide de VMware ou tout autre outils de virtualisation de votre choix.
    - Installez un système d'exploitation compatible, tel que Linux ou Windows, selon vos préférences. J'ai personnellement pris Ubuntu.

2. **Installation de Git :**

    - Assurez-vous que Git est installé sur votre machine virtuelle en exécutant la commande suivante dans un terminal :
    
      .. code-block:: bash
      
          sudo apt-get install git   

    - Configurez Git en associant une clé SSH à votre compte GitLab ou GitHub, selon vos besoins.

      .. code-block:: bash
      
          ssh-keygen

3. **Installation de Visual Studio Code :**

    - Téléchargez et installez Visual Studio Code.
    - Lancez Visual Studio Code et installez les extensions recommandées pour le développement Python.

4. **Clonage du Répertoire Git :**

    - Ouvrez un terminal dans votre machine virtuelle.
    - Clonez le répertoire Git contenant le code source du jeu en utilisant la commande suivante :

      .. code-block:: bash
      
          git clone <lien_SSH>   # Remplacez <lien_SSH> par l'e lien SSH du dépôt GitLab ou GitHub

5. **Allez dans le dossier cloné :**

    - Accédez au répertoire du projet cloné.

      .. code-block:: bash
      
          cd <nom de votre dossier git>   # Crée un environnement virtuel nommé 'venv'


Vous êtes maintenant pret à commencer à développer et à contribuer au jeu !


Utilisation
===========

Ce jeu est conçu pour être facilement utilisable et modifiable. Voici les principales fonctionnalités et utilisations du code :

1. **Exécution du Jeu :**

    - Pour exécuter le jeu, allez dans vs code ou en utilisant la commande suivante dans un terminal :

      .. code-block:: bash
      
          python jeu.py

2. **Modification du Jeu :**

    - Vous pouvez facilement modifier le comportement du jeu en modifiant le code source Python. Les fonctionnalités principales du jeu sont mises dans les classes telles que ``Plateau``, ``Joueur``, et ``Visibilite``.
    - Pour ajouter de nouvelles fonctionnalités, modifiez les méthodes existantes ou ajoutez de nouvelles méthodes et classes selon vos besoins.
    - Assurez-vous de respecter les conventions de nommage et de maintenir la cohérence du code avec les commentaires explicatifs pour faciliter la compréhension et la maintenance.

3. **Test du Code :**

    - Le code est livré avec un ensemble de tests unitaires pour vérifier le bon fonctionnement des différentes fonctionnalités. Vous pouvez exécuter ces tests à l'aide de la commande suivante :

      .. code-block:: bash
      
          python -m unittest

    - Assurez-vous que tous les tests passent avec succès avant de publier ou de déployer des modifications dans le code.

4. **Documentation du Code :**

    - La documentation du code est générée à l'aide de Sphinx, un outil de documentation python. Pour générer la documentation, suivez les instructions fournies dans le fichier ``docs/README.rst``.

5. **Contribuer au Projet :**

    - Si vous souhaitez contribuer au projet en proposant des améliorations ou des correctif, veuillez soumettre une demande d'extraction (pull request) sur le dépôt GitLab ou GitHub du projet.
    - Assurez-vous de suivre les directives de contribution fournies dans le fichier ``CONTRIBUTING.md``.

En suivant ces instructions, vous pourrez facilement utiliser, modifier et contribuer au développement de ce jeu.


Classes
=======

Le code est structuré autour de plusieurs classes qui représentent les éléments clé du jeu. Chaque classe a un rôle spécifique dans le fonctionnement global du jeu. Voici une description de ces classes :

1. **Plateau** :
   
   La classe ``Plateau`` représente le plateau de jeu où les joueurs évoluent. Elle contient une grille de dimensions 10x10 et fournit des méthodes pour placer et effacer les joueurs sur le plateau.

2. **Joueur** :

   La classe ``Joueur`` représente un joueur dans le jeu. Chaque joueur a des attributs tels que sa position (coordonnées x, y) et sa direction (haut, bas, gauche, droite). La classe fournit des méthodes pour faire tourner le joueur vers la gauche ou la droite, ainsi que pour le déplacer d'une ou deux cases dans sa direction actuelle.

3. **Visibilite** :

   La classe ``Visibilite`` gère la visibilité du joueur sur le plateau. Elle fournit une méthode pour déterminer les cases visibles dans la ligne directe du joueur en fonction de sa position et de sa direction.

Chaque classe est conçue de manière à être modulaire et à encapsuler les fonctionnalités pertinentes du jeu. Cela permet une meilleure organisation du code et facilite la compréhension, la modification et l'extension du jeu.


Fonctions
=========

Le code comprend également plusieurs fonctions qui complètent les fonctionnalités des classes et contribuent au bon déroulement du jeu. Voici une présentation des principales fonctions du jeu :

1. **position_valide(x, y)** :
   
   Cette fonction vérifie si les coordonnées données (x, y) sont valides sur le plateau de jeu. Elle renvoie ``True`` si les coordonnees sont valides et ``False`` sinon.

2. **placer_joueur(joueur)** :

   Cette fonction place un joueur sur le plateau de jeu, à condition que sa position soit valide. Elle met à jour la grille du plateau en définissant la position du joueur.

3. **effacer_joueur(joueur)** :

   Cette fonction éfface la position d'un joueur sur le plateau de jeu. Si le joueur se trouve sur une position valide, cette fonction réinitialise la case correspondante de la grille du plateau.

4. **bouger(distance)** :

   Cette fonction permet à un joueur de se déplacer d'une ou deux cases dans sa direction actuelle. Elle prend en compte la distance spécifiée et les limites du plateau pour déterminer la nouvelle position du joueur.

5. **ligne_visible(joueur)** :

   Cette fonction de la classe ``Visibilite`` calcule les cases visibles dans la ligne directe d'un joueur en fonction de sa position et de sa direction. Elle renvoie une liste de coordonnées représentant les cases visibles.

6. **fin_du_jeu(joueur1, joueur2)** :

   Cette fonction vérifie si le jeu est terminé en comparant les positions de deux joueurs. Si les deux joueurs se trouvent sur la même case, la fonction renvoie ``True``, indiquant que le jeu est terminé avec un gagnant.

Chaque fonction remplit un rôle spécifique dans le jeu et contribue à son fonctionnement global. Elles sont conçues pour être réutilisables et permettre une meilleure modularité du code.


Conclusion
==========

Le jeu présenté dans cette documentation offre une simulation simple mais divertissante d'un joueur se déplaçant sur un plateau virtuel. À travert l'utilisation de classes et de fonctions bien définies, le code fournit une base solide pour développer des fonctionnalités supplémentaires ou pour être utilisé comme base d'un projet plus complexe.

En explorant le code source, vous découvrirez comment les classes et les fonctions intéragissent pour créer une expérience de jeu cohérente. N'hésitez pas à examiner le code en détail, à le modifier et à l'adapter à vos besoins spécifiques.

Nous espérons que cette documentation vous a été utile pour comprendre le fonctionnement du jeu et pour explorer les concepts de base de la programmation orientée objet en Python.

Nous vous remercions de l'interêt que vous portez à ce projet et vous encourageons à continuer à explorer et à apprendre !






Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
