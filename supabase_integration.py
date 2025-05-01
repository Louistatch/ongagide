import os
import requests
from django.conf import settings

class SupabaseClient:
    """
    Client pour interagir avec Supabase depuis Django
    """
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.headers = {
            'apikey': self.supabase_key,
            'Authorization': f'Bearer {self.supabase_key}',
            'Content-Type': 'application/json'
        }
    
    def query(self, table, query_params=None):
        """
        Exécute une requête sur une table Supabase
        """
        url = f"{self.supabase_url}/rest/v1/{table}"
        response = requests.get(url, headers=self.headers, params=query_params)
        response.raise_for_status()
        return response.json()
    
    def insert(self, table, data):
        """
        Insère des données dans une table Supabase
        """
        url = f"{self.supabase_url}/rest/v1/{table}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def update(self, table, data, query_params):
        """
        Met à jour des données dans une table Supabase
        """
        url = f"{self.supabase_url}/rest/v1/{table}"
        response = requests.patch(url, headers=self.headers, json=data, params=query_params)
        response.raise_for_status()
        return response.json()
    
    def delete(self, table, query_params):
        """
        Supprime des données d'une table Supabase
        """
        url = f"{self.supabase_url}/rest/v1/{table}"
        response = requests.delete(url, headers=self.headers, params=query_params)
        response.raise_for_status()
        return response.json()
    
    def run_rpc(self, function_name, params=None):
        """
        Exécute une fonction stockée dans Supabase
        """
        url = f"{self.supabase_url}/rest/v1/rpc/{function_name}"
        response = requests.post(url, headers=self.headers, json=params)
        response.raise_for_status()
        return response.json()
    
    def get_auth_user(self, token):
        """
        Récupère les informations d'un utilisateur authentifié
        """
        headers = self.headers.copy()
        headers['Authorization'] = f'Bearer {token}'
        url = f"{self.supabase_url}/auth/v1/user"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Créer une instance globale du client
supabase = SupabaseClient() 