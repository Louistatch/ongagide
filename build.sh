#!/usr/bin/env bash
# Script pour déployer l'application Django sur Render ou DigitalOcean

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

# Créer les tables si elles n'existent pas
python manage.py makemigrations --noinput || echo "makemigrations failed, but continuing"

# Appliquer les migrations avec un niveau de détail élevé
python manage.py migrate --noinput --verbosity 2 || echo "migrate failed, but continuing"

# Créer un superutilisateur si nécessaire (ne pas échouer si l'utilisateur existe déjà)
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell || echo "Creating superuser failed, but continuing" 