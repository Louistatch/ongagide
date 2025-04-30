#!/usr/bin/env bash
# Script pour déployer l'application Django sur Render

# Sortir en cas d'erreur
set -o errexit

# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Appliquer les migrations
python manage.py migrate 