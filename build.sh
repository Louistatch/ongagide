#!/usr/bin/env bash
# Script pour déployer l'application Django sur Render

# Sortir en cas d'erreur
set -o errexit

# Afficher les commandes pendant l'exécution
set -o xtrace

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
pip install --no-cache-dir -r requirements.txt

# Créer le répertoire staticfiles s'il n'existe pas
mkdir -p staticfiles

# Tenter la collecte des fichiers statiques, mais continuer même en cas d'échec
python manage.py collectstatic --noinput || echo "Collectstatic failed, but continuing"

# Appliquer les migrations
python manage.py migrate 