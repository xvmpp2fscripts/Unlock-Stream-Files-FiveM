import os
import argparse

def watermark(chemin, contenu):
    try:
        for dossier_actuel, sous_dossiers, fichiers in os.walk(chemin):
            chemin_readme = os.path.join(dossier_actuel, "LISEZ_MOI.txt")
            with open(chemin_readme, "w", encoding="utf-8") as f:
                f.write(contenu)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Créer un fichier LISEZ_MOI.txt dans tous les dossiers")
    parser.add_argument("-d", "--directory", required=True, help="Chemin du répertoire cible")
    args = parser.parse_args()

    contenu = """Décrypté par discord.gg/fscripts [XVMPP]"""
    watermark(args.directory, contenu)