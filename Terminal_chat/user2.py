# -*- coding: utf-8 -*-
from client import Client
import threading

# Définir l'adresse IP et le port
HOST = '127.0.0.1'
PORT = 6000

# Demander à l'utilisateur de fournir un pseudo
pseudo = ""
while len(pseudo) == 0 or len(pseudo) > 20:
    pseudo = input("Entrez votre pseudo (maximum 20 caractères) : ")

# Créer une instance de la classe Client
client = Client(HOST, PORT)
client.connect()


def recevoir_messages():
    while True:
        try:
            message = client.receive()
            print(message)
        except:
            print("Une erreur s'est produite. Déconnexion du serveur.")
            client.disconnect()
            break


# Envoyer le pseudo au serveur
client.send(pseudo)

# Démarrer un thread pour recevoir les messages
thread_reception = threading.Thread(target=recevoir_messages)
thread_reception.start()

# Gérer l'envoi de messages
while True:
    message = input()
    if message.lower() == "/quit":
        client.send("/quit")
        break
    else:
        client.send(message)

# Fermer le socket client
client.disconnect()
