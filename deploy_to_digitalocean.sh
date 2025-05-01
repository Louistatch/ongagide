#!/bin/bash

# Script de déploiement pour DigitalOcean
# Ce script facilite le déploiement de l'application AGIDE avec Supabase sur DigitalOcean

set -e  # Arrêt en cas d'erreur

# Vérifier si doctl est installé
if ! command -v doctl &> /dev/null; then
    echo "Error: doctl n'est pas installé. Veuillez l'installer: https://docs.digitalocean.com/reference/doctl/how-to/install/"
    exit 1
fi

# Vérifier si Docker est installé
if ! command -v docker &> /dev/null; then
    echo "Error: Docker n'est pas installé. Veuillez l'installer: https://docs.docker.com/get-docker/"
    exit 1
fi

# Vérifier si le fichier .env existe
if [ ! -f .env ]; then
    echo "Error: Le fichier .env n'existe pas. Veuillez le créer selon le modèle."
    exit 1
fi

# Source des variables d'environnement
source .env

# Demande d'authentification DigitalOcean
echo "== Authentification DigitalOcean =="
echo "Veuillez vous authentifier avec votre token DigitalOcean..."
doctl auth init
echo ""

# Menu de déploiement
echo "== Options de déploiement =="
echo "1) Déployer sur App Platform (conteneurs)"
echo "2) Déployer sur un Droplet (VM)"
echo "3) Quitter"
read -p "Choisissez une option [1-3]: " deploy_option

case $deploy_option in
    1)
        echo "== Déploiement sur App Platform =="
        
        # Création du registre de conteneurs si nécessaire
        echo "Création du registre de conteneurs..."
        doctl registry create agide-registry || true
        
        # Connexion au registre
        echo "Connexion au registre..."
        doctl registry login
        
        # Construction et push des images
        echo "Construction et push des images..."
        docker-compose build
        docker tag agide_web:latest registry.digitalocean.com/agide-registry/agide_web:latest
        docker push registry.digitalocean.com/agide-registry/agide_web:latest
        
        # Déploiement avec app-spec.yaml
        echo "Déploiement de l'application..."
        doctl apps create --spec app-spec.yaml
        
        echo "Déploiement terminé avec succès! Votre application sera bientôt disponible."
        ;;
        
    2)
        echo "== Déploiement sur un Droplet =="
        
        # Création d'un Droplet
        echo "Création d'un nouveau Droplet..."
        read -p "Nom du Droplet: " droplet_name
        read -p "Taille (s-1vcpu-1gb, s-1vcpu-2gb, s-2vcpu-2gb): " droplet_size
        
        doctl compute droplet create $droplet_name \
            --image ubuntu-22-04-x64 \
            --size $droplet_size \
            --region ${DO_REGION:-fra1} \
            --ssh-keys $(doctl compute ssh-key list --format ID --no-header)
        
        # Attendre que le Droplet soit prêt
        echo "Attente de la création du Droplet..."
        sleep 20
        
        # Récupérer l'IP du Droplet
        droplet_ip=$(doctl compute droplet get $droplet_name --format PublicIPv4 --no-header)
        
        echo "Droplet créé avec l'IP: $droplet_ip"
        echo "Attendez quelques instants pour que le Droplet soit complètement initialisé..."
        sleep 40
        
        # Installation de Docker sur le Droplet
        echo "Installation de Docker sur le Droplet..."
        ssh -o StrictHostKeyChecking=no root@$droplet_ip << EOF
        curl -fsSL https://get.docker.com -o get-docker.sh
        sh get-docker.sh
        apt-get update && apt-get install -y docker-compose
EOF
        
        # Création du répertoire d'application
        ssh -o StrictHostKeyChecking=no root@$droplet_ip "mkdir -p /opt/agide"
        
        # Copie des fichiers vers le Droplet
        echo "Copie des fichiers vers le Droplet..."
        scp -o StrictHostKeyChecking=no docker-compose.yml root@$droplet_ip:/opt/agide/
        scp -o StrictHostKeyChecking=no Dockerfile root@$droplet_ip:/opt/agide/
        scp -o StrictHostKeyChecking=no nginx.conf root@$droplet_ip:/opt/agide/
        scp -o StrictHostKeyChecking=no .env root@$droplet_ip:/opt/agide/
        scp -o StrictHostKeyChecking=no -r ./* root@$droplet_ip:/opt/agide/
        
        # Lancement de l'application sur le Droplet
        echo "Lancement de l'application..."
        ssh -o StrictHostKeyChecking=no root@$droplet_ip << EOF
        cd /opt/agide
        docker-compose up -d
EOF
        
        echo "Déploiement terminé avec succès!"
        echo "Votre application est disponible à l'adresse: http://$droplet_ip"
        echo ""
        echo "Pour configurer un nom de domaine et SSL, exécutez ces commandes sur le Droplet:"
        echo "apt-get install -y certbot python3-certbot-nginx"
        echo "certbot --nginx -d votre-domaine.com"
        ;;
        
    3)
        echo "Sortie du script de déploiement."
        exit 0
        ;;
        
    *)
        echo "Option invalide."
        exit 1
        ;;
esac

echo ""
echo "== Notes importantes =="
echo "1. Vérifiez les logs avec: 'doctl apps logs $DO_APP_NAME' ou 'docker-compose logs -f'"
echo "2. Pour mettre à jour l'application, relancez ce script"
echo "3. Pour des modifications manuelles, consultez le fichier docker-supabase-deployment.md"
echo ""
echo "Merci d'utiliser le script de déploiement AGIDE!" 