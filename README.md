# TP-Linux
TP Linux: Sujet 1,2,6 et 7
*************Sujet1-2_dictionnaire_de_donnee.py*************

Simulation d'une Attaque par Dictionnaire (en Python)
Ce script Python simule une attaque par dictionnaire en testant une liste de mots de passe courants pour tenter de "deviner" celui saisi par un utilisateur.

Fonctionnalités
Demande à l'utilisateur de saisir :son nom, son login, son mot de passe
Affiche les informations collectées (à des fins de démonstration uniquement)
Simule une attaque par dictionnaire en testant une liste de mots de passe courants pour retrouver le mot de passe saisi.

Prérequis à installer afin d'executer ce script sur un machine ayant pour systeme d'exploitation Kali Linux 
1. Installer Python 3
Le script utilise Python 3.
- Vérification : python3 --version
- Installation (si nécessaire) :
sudo apt update
sudo apt install python3
2.Un éditeur de texte ou IDE (facultatif mais recommandé)
Vous pouvez utiliser :VS Code, PyCharm...

*************Sujet6_Transfert-cle-USB-to-PC.py*************

Script de Sauvegarde Automatique de Clé USB
Ce script permet de détecter automatiquement une clé USB insérée et de copier tout son contenu vers un dossier local défini.
Ce script ne gère qu’une seule clé USB à la fois.

Fonctionnalités
Surveille en continu l'insertion d'une clé USB.
Copie automatiquement tous les fichiers et dossiers de la clé dans un dossier local.

Prérequis à installer afin d'executer ce script sur un machine ayant pour systeme d'exploitation Kali Linux 
1. Installer Python 3
Le script utilise Python 3.
- Vérification : python3 --version
- Installation (si nécessaire) :
sudo apt update
sudo apt install python3
2.Créer le dossier de destination si nécessaire :
mkdir -p /home/styve/Bureau/TP_Linux/Test/

*************Sujet6_Transfert-cle-USB-to-Cloud.py*************

Script de Sauvegarde USB vers Google Drive avec rclone
Ce script Python permet de détecter automatiquement une clé USB branchée sur un système Linux (comme Kali Linux), puis de copier son contenu vers Google Drive à l’aide de l’outil rclone.
Ce script ne gère qu’une seule clé USB à la fois.

Fonctionnement
Le script cherche une clé USB montée dans les répertoires habituels (/media/<utilisateur> ou /run/media/<utilisateur>).
Si une clé est détectée, son contenu est copié vers le dossier Sauvegardes/cle_usb sur Google Drive.
Le nom de la configuration rclone peut être modifié si besoin.

Prérequis à installer afin d'executer ce script sur un machine ayant pour systeme d'exploitation Kali Linux 
1. Installer Python 3
Le script utilise Python 3.
- Vérification : python3 --version
- Installation (si nécessaire) :
sudo apt update
sudo apt install python3

2. Installer l'outil rclone: rclone est l'outil utilisé pour transférer les fichiers vers Google Drive.
Installation sur Linux (ex: Debian, Kali, Ubuntu) : sudo apt install rclone

3. Configurer Google Drive avec rclone
Lancez la configuration : rclone config
Suivez les étapes pour :
Créer un nouveau remote (ex: gdrive), Choisir Google Drive comme service,Se connecter à votre compte Google, Finaliser la configuration


