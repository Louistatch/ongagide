"""
Script de test pour vérifier la configuration WSGI sur Render

Ce script crée une application WSGI de test très simple pour vérifier
si le serveur WSGI fonctionne correctement.
"""

def application(environ, start_response):
    """Application WSGI de test."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<html><body><h1>Render Test OK</h1><p>Si vous voyez ce message, le serveur WSGI fonctionne correctement.</p></body></html>'] 