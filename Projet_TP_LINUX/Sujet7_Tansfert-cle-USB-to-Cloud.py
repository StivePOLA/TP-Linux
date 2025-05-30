import subprocess
import os
import getpass
import time

def detecter_cle_usb_linux():
    """
    Détecte le chemin de montage d'une clé USB sur Kali Linux (ou autres distros Linux).
    
    Retourne le chemin de montage si trouvé, sinon None.
    """
    # Récupérer le nom d'utilisateur courant
    utilisateur = getpass.getuser()
    
    # Les chemins courants où les clés USB sont montées
    chemins_possibles = [
        f"/media/{utilisateur}",
        f"/run/media/{utilisateur}"
    ]
    
    # Parcourir les chemins possibles pour détecter un dossier monté
    for base_path in chemins_possibles:
        if os.path.exists(base_path):
            for dossier in os.listdir(base_path):
                chemin_cle = os.path.join(base_path, dossier)
                # Vérifier que c'est un point de montage
                if os.path.ismount(chemin_cle):
                    return chemin_cle
    return None

def copier_avec_rclone(source_local, dossier_distant, remote="gdrive"):
    """
    Copie le contenu du dossier source vers Google Drive avec rclone.

    :param source_local: Chemin local de la clé USB.
    :param dossier_distant: Chemin distant dans Google Drive.
    :param remote: Nom de la configuration rclone (par défaut 'gdrive').
    """
    if not os.path.exists(source_local):
        print(f"Erreur❌: le dossier source '{source_local}' n'existe pas.")
        return
    
    # Construire la commande rclone copy
    commande = [
        "rclone", "copy",
        source_local,
        f"{remote}:{dossier_distant}",
        "--progress",
        "--verbose"
    ]

    try:
        print(f"📤 Lancement de la copie de '{source_local}' vers '{remote}:{dossier_distant}'...")
        subprocess.run(commande, check=True)
        print("Copie terminée avec succès✅.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la copie ❌: {e}")

def main():
    print("🔎 Détection de la clé USB...")
    chemin_usb = detecter_cle_usb_linux()

    if chemin_usb:
        print(f"🔗 Clé USB détectée : {chemin_usb}")
        # Modifier ici le chemin distant souhaité sur Google Drive
        dossier_distant = "Sauvegardes/cle_usb"
        copier_avec_rclone(chemin_usb, dossier_distant)
    else:
        print("Aucune clé USB détectée. Veuillez insérer une clé USB et relancer le script 🔎.")

if __name__ == "__main__":
    main()
