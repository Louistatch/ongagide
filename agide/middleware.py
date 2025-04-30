import logging

logger = logging.getLogger('django')

class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log pour déboguer les requêtes
        logger.info(f"Requête reçue: {request.method} {request.path} {request.META.get('REMOTE_ADDR')}")
        
        # Logguer les en-têtes de débogage
        for key, value in request.META.items():
            if key.startswith('HTTP_') or key in ('REMOTE_ADDR', 'SERVER_NAME'):
                logger.info(f"Header: {key}: {value}")
        
        response = self.get_response(request)
        
        # Log pour déboguer les réponses
        logger.info(f"Réponse: {response.status_code}")
        
        return response 