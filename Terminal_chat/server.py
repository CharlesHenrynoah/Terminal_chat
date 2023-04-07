# -*- coding: utf-8 -*-

import socket
import threading
import fichierlog

# Définir l'adresse IP et le port
HOST = '127.0.0.1'
PORT = 6000

# Liste des clients connectés
clients = []


def afficher_utilisateurs_connectes():
    liste_pseudos = [client["pseudo"] for client in clients]
    print("Utilisateurs connectés ({}): {}".format(
        len(clients), ', '.join(liste_pseudos)))


def pseudo_deja_utilise(pseudo):
    for client in clients:
        if client["pseudo"].lower() == pseudo.lower():
            return True
    return False


def gerer_client(client_socket, client_address):
    # Recevoir le pseudo du client
    pseudo = client_socket.recv(1024).decode()

    # Enregistrer les logs
    fichierlog.logs(pseudo, client_address)

    # Vérifier si le pseudo est valide et s'il est déjà utilisé
    while len(pseudo) > 20 or pseudo_deja_utilise(pseudo):
        if len(pseudo) > 20:
            message = "Le pseudo est trop long. Veuillez en choisir un autre."
        else:
            message = "Le pseudo est déjà utilisé. Veuillez en choisir un autre."
        client_socket.sendall(message.encode())
        pseudo = client_socket.recv(1024).decode()

    # Envoyer le message "Tu es connecté" au client
    client_socket.sendall("Tu es connecté".encode())

    # Créer un dictionnaire pour stocker les informations du client
    nouveau_client = {"pseudo": pseudo, "socket": client_socket}

    # Ajouter le client à la liste des clients connectés
    clients.append(nouveau_client)

    # Afficher les utilisateurs connectés
    afficher_utilisateurs_connectes()

    # Afficher l'adresse IP et le port du client connecté
    print("Client « {} » est connecté depuis {}:{}".format(
        pseudo, client_address[0], client_address[1]))

    # Informer tous les autres clients qu'un nouveau client a rejoint le chat
    message_bienvenue = "{} a rejoint le chat.".format(pseudo)
    for client in clients:
        if client["socket"] != client_socket:
            client["socket"].sendall(message_bienvenue.encode())

    # Attendre les messages du client et les diffuser aux autres clients
    while True:
        try:
            message = client_socket.recv(1024).decode()
        except ConnectionResetError:
            message = "/quit"

        if message == "":
            # Si la chaîne reçue est vide, la connexion est fermée
            message = "/quit"
        elif message == "deconnection":
            # Si le client envoie un message "/quit", il se déconnecte
            message_depart = "{} a quitté le chat.".format(pseudo)
            clients.remove(nouveau_client)

            # Afficher les utilisateurs connectés
            afficher_utilisateurs_connectes()

            client_socket.close()
            for client in clients:
                client["socket"].sendall(message_depart.encode())
            break
        elif message == "/list":
            # Si le client envoie un message "/list", envoyer la liste des utilisateurs connectés
            liste_pseudos = [client["pseudo"] for client in clients]
            message_liste = "Utilisateurs connectés : " + \
                ", ".join(liste_pseudos)
            client_socket.sendall(message_liste.encode())
        else:
            message_diffuse = "{}: {}".format(pseudo, message)
            for client in clients:

                if client["socket"] != client_socket:
                    client["socket"].sendall(message_diffuse.encode())

    print("Client {} déconnecté.".format(pseudo))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

try:
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=gerer_client, args=(
            client_socket, client_address))
        thread.start()

finally:
    server_socket.close()
