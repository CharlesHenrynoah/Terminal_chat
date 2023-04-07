# Terminal_chat

Cet exemple de code permet de créer un chat en Python en utilisant des sockets et des threads. Les utilisateurs peuvent se connecter au serveur, choisir un pseudo et discuter avec les autres utilisateurs connectés.

# Utilisation

Exécutez le fichier server.py pour lancer le serveur.
Les utilisateurs doivent exécuter le fichier user2.py pour se connecter au serveur et commencer à discuter.

# Fonctionnalités

Le chat dispose des fonctionnalités suivantes :
Les utilisateurs peuvent se connecter au serveur en spécifiant un pseudo.
Le serveur enregistre les connexions dans un fichier de logs.
Les utilisateurs peuvent discuter avec les autres utilisateurs connectés.
Les utilisateurs peuvent voir la liste des utilisateurs connectés en tapant /list.
Les utilisateurs peuvent quitter le chat en tapant /quit.

# Structure du projet

client.py: contient la classe Client, qui gère la connexion au serveur.
fichierlog.py: contient la fonction logs, qui enregistre les connexions dans un fichier de logs.
server.py: contient le code du serveur.
user2.py: contient le code du client.

# Licence
Ce code est sous licence MIT.

# Auteur

Ce code a été écrit par Charles-Henry Noah
