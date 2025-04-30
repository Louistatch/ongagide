# Site Web AGIDE

Site web officiel de l'Association pour la Gestion Intégrée et Durable de L'Environnement (AGIDE).

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate     # Sur Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer les variables d'environnement :
Créer un fichier `.env` à la racine du projet avec les variables suivantes :
```
DEBUG=True
SECRET_KEY=votre_clé_secrète
DATABASE_URL=postgres://user:password@localhost:5432/agide_db
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement :
```bash
python manage.py runserver
```

## Structure du projet

- `core/` : Configuration principale et modèles de base
- `products/` : Gestion des produits CHAMPIGROW
- `contact/` : Formulaire de contact et gestion des messages
- `pages/` : Pages statiques (Accueil, À propos, etc.)
- `static/` : Fichiers statiques (CSS, JS, images)
- `templates/` : Templates HTML

## Fonctionnalités principales

- Présentation de l'ONG et de ses activités
- Catalogue des produits CHAMPIGROW
- Formulaire de contact
- Gestion des actualités
- Interface d'administration
- Design responsive et optimisé pour les connexions lentes 