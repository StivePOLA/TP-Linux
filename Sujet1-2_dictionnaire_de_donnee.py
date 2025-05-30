# Fonction pour collecter les informations utilisateur via l'entrée clavier
def collect_user_info():
    # Demande à l'utilisateur d'entrer son nom
    nom = input("Entrez votre nom : ")
    # Demande à l'utilisateur d'entrer son login
    login = input("Entrez votre login : ")
    # Demande à l'utilisateur d'entrer son mot de passe
    mot_de_passe = input("Entrez votre mot de passe : ")

    # Crée un dictionnaire pour stocker les informations utilisateur
    utilisateur = {
        "nom": nom,
        "login": login,
        "mot_de_passe": mot_de_passe
    }

    # Retourne ce dictionnaire
    return utilisateur

# Exemple d'utilisation de la fonction collect_user_info
info_utilisateur = collect_user_info()

# Affiche les informations collectées
print("Informations collectées :", info_utilisateur)
print("")  # Ligne vide pour aérer la sortie

# Stocke le mot de passe saisi par l'utilisateur dans une variable séparée
mot_de_passe_correct = info_utilisateur['mot_de_passe']

# Crée une liste de mots de passe "test" (simulant un dictionnaire de mots de passe courants)
dictionnaire_de_test =  [
    "123456", "password", "admin", "motdepasse", "monSuperMotDePasse", "azerty", mot_de_passe_correct]

# Fonction qui simule une attaque par dictionnaire
# Elle teste chaque mot de passe de la liste pour voir s'il correspond au mot de passe cible
def attaque_par_dictionnaire(mot_de_passe_cible, liste_mots_de_passe):
    # Parcourt chaque mot de passe dans la liste de test
    for tentative in liste_mots_de_passe:
        # Affiche le mot de passe testé
        print(f"Test du mot de passe : {tentative}")
        # Vérifie si la tentative correspond au mot de passe cible
        if tentative == mot_de_passe_cible:
            # Si oui, affiche que le mot de passe a été trouvé
            print(f"Mot de passe trouvé ! => {tentative}")
            # Retourne le mot de passe trouvé
            return tentative
    # Si aucun mot de passe de la liste ne correspond, affiche un message d'échec
    print("Mot de passe non trouvé.")
    # Retourne None pour indiquer l'échec
    return None

# Lance la simulation d'attaque par dictionnaire en utilisant le mot de passe correct
attaque_par_dictionnaire(mot_de_passe_correct, dictionnaire_de_test)
