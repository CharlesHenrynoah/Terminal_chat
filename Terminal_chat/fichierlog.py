import datetime


def logs(pseudo, client_address):
    # Ouvrir le fichier logs.txt en mode append
    with open("logs.txt", "a") as f:
        # Obtenir la date et l'heure actuelles
        date_heure = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Ajouter une ligne au fichier de logs avec le pseudo et l'adresse complète du client
        f.write("{}: Nouvelle connexion de l'utilisateur {} ({}, {})\n".format(
            date_heure, pseudo, client_address[0], client_address[1]))
