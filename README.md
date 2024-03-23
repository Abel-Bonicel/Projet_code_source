# Projet Code Source
## par Abel BONICEL
### Jeu "Attrape moi si tu peux !"

**Date de rendu limite :** Dimanche 24 mars à 23h50

**Objectif :** Développer le coeur d'un jeu à deux joueurs qui se déplacent sur une grille de 10*10.

**Règle du jeu :**

	-Grille : La grille est un espace de 10 par 10 cases.
	-Déplacement : A chaque tour, un joueur peut choisir parmi les actions suivantes:
		-Pivoter à gauche de 90°.
		-Pivoter à droite de 90°.
		-Avancer d'une ou 2 cases.
	-Sortie de grille : Si un joueur evence hors de la grille son déplacement est annulé. 
	-Visibilité : Un joueur ne peut voir qu'en ligne droite selon la direction actuelle (ligne ou colonne)

**But du jeu :** Un joueur gagne si, après avoir effectué une Action, il se trouve sur la même case que l'autre joueur

**Contraintes techniques :**

	1. Le projet dois être réalisé en Python.
	2. Le code doit être développé en TDD (Test-Diven Development).
	3. Se concentrer sur le développement des classes nécessaires pour gérer le jeu et les déplacements des joueurs.
	4. Eviter d'intégrer des interfaces graphiques ou des sorties sur la console. Le code doit se concentrer sur la logique du jeu.

**Critère de notation :**

	1. Qualité des test écrits.
	2. Organisation du code sous Git.
	3. Résultats des retours de Pylint pour vérifier la qualité du code.
	4. Documentation adéquate pour le code écrit.

**Remarque :** Le fonctionnalité du jeu est importante, mais la priorité est mise sur la qualité du code, les tests et la documentation.


# Méthode utilisé :

## Création machine virtuel et mise en place de git :

Pour mettre en oeuvre ce projet j'ai décidé d'utiliser une Machine Virtuelle Ubuntu. Ci-dessous je vais vous indiquer comment mettre en place le projet de la même façon que moi :

Créer une VM sous Ubuntu (Machine Virtuelle) grâce à un hyperviseur comme VMware, HyperV, VirtualBox...
Allez dans l'invite de commande puis créez un dossier pour le Projet avec la commande : 

`mkdir 'nom_du_dossier'`

Pour utiliser git nous aurons besoins de générer une clé ssh afin de communiquer avec le github. Pour cela faites la commande suivante :

`ssh-keygen`

Cela vas vous demander plusieurs informations mais cela n'est pas nécessaire et je vous recommande de rien mettre dans les champs : 

	```
	{	
	Generating public/private rsa key pair.
	Enter file in which to save the key (/home/user/.ssh/id_rsa): 
	Enter passphrase (empty for no passphrase): 
	Enter same passphrase again: 
	Your identification has been saved in id_rsa.key
	Your public key has been saved in id_rsa.key.pub
	The key fingerprint is:	SHA256:clé user@user-virtual-machine
	}
	``` 

Ensuite faite la commande cd pour aller dans le dossier ou la clé a été généré : 

`cd /home/user/.ssh/id_rsa`

Puis ouvrez le fichier id_rsa.key.pub avec une commande et copiez son contenu : 


`nano id_rsa.key.pub`
ou
`cat id_rsa.key.pub`

Allez dorénavent sur votre compte GitHub -> Profil -> Settings -> SSH and GPG keys et cliquez sur New ssh key
Mettez n'importe quel titre (c'est juste pour vous retrouvez) puis collez le contenu du fichier id_rsa.key.pub dans le champ : key.

Appliquez les modifications et retournez sur votre invite de commande. faite:
`cd /home/user/nom_du_dossier`
cela vous amène dans votre dossier et maintenant il faut installer git. Pour ce faire faites la commande :

`sudo apt install git`

mettez votre mot de passe et acceptez l'installation en appuyant sur y.

A la fin de l'installation et en vérifiant que vous êtes dans le bon dossier écrivez les commandes suivantes :

`git init`
`git config --gobal user.email "votre_email"`
`git config --global user.name "votre_nom"`

Enfin pour cloner le dépot github dans vôtre dossier il faut copier le code ssh de votre repository en cliquant sur code -> Local -> SSH puis de faire la commande suivante :

`git clone code_ssh_copié`

Et voilà vous avec cloné votre repository dans votre fichier sur la VM.

Commande de base de git : 

`Git add <file>`
`git commit -m "message de commit"`
`git branch -M <nom de la branche :main ,dev, ...>`
`git push origin <nom de la branche :main ,dev, ...>`

## Python : 

Pour commencer allez dans l'invite de commande et faites : 

`sudo apt install pyhton`

Puis utilisez un IDE (Environnement de Developpement) et codez ! 
(Pensez bien à enregistrer vos codes dans le dossier de votre projet)


