import os
import shutil
import time

# Définir le répertoire où le contenu de la clé USB sera copié
DEST_DIR = "/home/styve/Bureau/TP_Linux/Test/"

# Fonction pour détecter si une clé USB est montée
def get_mounted_usb():
    # Nom de l'utilisateur actuel (utilisé pour construire le chemin des clés USB)
    USER = os.getlogin()
    # Chemin par défaut où les périphériques USB sont montés sous Kali (pour l'utilisateur kali)
    media_path = f"/media/{USER}"
    
    # Vérifier si ce dossier existe (parfois, il n'existe pas si aucun périphérique n'a été monté)
    if not os.path.exists(media_path):     
        return None

    # Parcourir tous les dossiers montés dans /media/Utilisateur
    for item in os.listdir(media_path):
        usb_path = os.path.join(media_path, item)
        # Vérifier si l'élément est bien un point de montage (clé USB insérée)
        if os.path.ismount(usb_path):
            return usb_path  # Retourner le chemin de la clé USB
    return None  # Si aucune clé n'est trouvée

# Fonction qui copie le contenu de la clé USB vers un dossier local
def copy_usb_content(src, dest):
    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(dest):
        os.makedirs(dest)

    print(f"[INFO]📤 Le transfert de fichiers de '{src}' vers '{dest}' est en cours")

    # Parcourir tous les fichiers et dossiers à la racine de la clé USB
    for item in os.listdir(src):
        s = os.path.join(src, item)  # Chemin source complet
        d = os.path.join(dest, item)  # Chemin de destination

        try:
            # Si c'est un dossier, copier récursivement tout le contenu
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)  # dirs_exist_ok=True permet d'écraser les dossiers existants
            else:
                shutil.copy2(s, d)  # Copier un fichier unique avec ses métadonnées
        except Exception as e:
            print(f"[ERREUR] ❌ Échec lors du transfert de {item} : {e}")

# Fonction principale qui lance le processus de détection et de copie
def main():
    print("[INFO]🔎 Attente d'une clé USB...")

    # Boucle infinie pour surveiller en permanence l'arrivée d'une clé USB
    while True:
        usb_path = get_mounted_usb()  # Vérifie si une clé est montée
        if usb_path:
            print(f"🔗 Clé USB détectée : '{usb_path}'")
            # Générer un nom unique pour chaque sauvegarde en utilisant la date et l'heure
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            dest_path = os.path.join(DEST_DIR, f"usb_{timestamp}")

            # Lancer la copie de la clé
            copy_usb_content(usb_path, dest_path)

            print("[INFO] Copie terminée avec success ✅. En attente du retrait de la clé...")

            # Attendre que la clé soit retirée avant de continuer
            while get_mounted_usb():
                time.sleep(1)

            print(f"[INFO] Clé USB '{usb_path}' retirée. Nouvelle attente🔎...")

        # Attendre 2 secondes avant de vérifier à nouveau
        time.sleep(2)

# Point d’entrée du programme
if __name__ == "__main__":
    main()
