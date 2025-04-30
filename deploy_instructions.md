# Instructions de déploiement pour ONG AGIDE

## Déploiement sur PythonAnywhere

1. **Créez un compte sur PythonAnywhere**
   - Rendez-vous sur [PythonAnywhere](https://www.pythonanywhere.com) et créez un compte gratuit

2. **Créez une application Web**
   - Allez dans la section "Web" du tableau de bord
   - Cliquez sur "Add a new web app"
   - Choisissez "Manual configuration"
   - Sélectionnez Python 3.8 (ou plus récent)

3. **Configurez votre environnement virtuel**
   - Ouvrez une console Bash depuis le tableau de bord
   - Exécutez les commandes suivantes:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 ongagide-env
   git clone https://github.com/Louistatch/ongagide.git
   cd ongagide
   pip install -r requirements.txt
   ```

4. **Configurez l'application Web**
   - Dans la section "Web", configurez:
     - Source code: `/home/yourusername/ongagide`
     - Working directory: `/home/yourusername/ongagide`
     - Virtual environment: `/home/yourusername/.virtualenvs/ongagide-env`
   
   - Modifiez le fichier WSGI en cliquant sur le lien dans la section "Code" et remplacez-le par:
   ```python
   import os
   import sys

   # Ajouter le chemin du projet
   path = '/home/yourusername/ongagide'
   if path not in sys.path:
       sys.path.append(path)

   # Définir les variables d'environnement
   os.environ['DJANGO_SETTINGS_MODULE'] = 'agide.settings'

   # Importer l'application
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

5. **Configurez les fichiers statiques**
   - Dans la section "Web", ajoutez:
     - URL: `/static/`
     - Directory: `/home/yourusername/ongagide/staticfiles`

6. **Collectez les fichiers statiques**
   - Dans la console Bash:
   ```bash
   cd ~/ongagide
   python manage.py collectstatic --noinput
   ```

7. **Appliquez les migrations**
   - Dans la console Bash:
   ```bash
   cd ~/ongagide
   python manage.py migrate
   ```

8. **Rechargez l'application**
   - Cliquez sur le bouton vert "Reload" dans la section "Web"

9. **Visitez votre site**
   - Votre site est maintenant accessible à l'adresse: `yourusername.pythonanywhere.com`

## Sécurité

N'oubliez pas de:
- Changer les clés secrètes (`SECRET_KEY`) dans settings.py
- Stocker les variables sensibles dans des variables d'environnement
- Configurer HTTPS pour votre site (disponible avec un compte payant sur PythonAnywhere)

## Autres options de déploiement

Si PythonAnywhere ne vous convient pas, voici d'autres options:
- Heroku
- DigitalOcean
- Render
- Railway
- AWS Elastic Beanstalk

## Déploiement sur Render

Render est une alternative moderne avec un généreux niveau gratuit:

1. **Créez un compte sur Render**
   - Inscrivez-vous sur [Render](https://render.com)

2. **Créez un nouveau service Web**
   - Choisissez "Web Service"
   - Connectez votre dépôt GitHub
   - Sélectionnez le dépôt `ongagide`

3. **Configurez votre service**
   - Nom: `ongagide`
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn agide.wsgi:application`

4. **Ajoutez les variables d'environnement**
   - `DEBUG`: `False`
   - `SECRET_KEY`: (une valeur secrète complexe)
   - `ALLOWED_HOSTS`: `ongagide.onrender.com`

5. **Ajoutez gunicorn à vos dépendances**
   - Ajoutez `gunicorn>=21.2.0` à votre fichier requirements.txt

6. **Créez un fichier build.sh**
   - Ce fichier aidera Render à déployer correctement votre application

Votre application sera déployée automatiquement lorsque vous poussez des modifications vers GitHub. 