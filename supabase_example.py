from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .supabase_integration import supabase

def supabase_example_view(request):
    """
    Vue d'exemple montrant comment utiliser Supabase dans Django
    """
    context = {
        'title': 'Exemple Supabase',
    }
    
    # Récupérer des données depuis Supabase
    try:
        # Supposons une table "products" dans Supabase
        products = supabase.query('products', {'select': '*', 'limit': 10})
        context['products'] = products
    except Exception as e:
        context['error'] = str(e)
    
    return render(request, 'supabase_example.html', context)

@require_http_methods(["POST"])
def supabase_create_product(request):
    """
    Exemple d'API pour créer un produit dans Supabase
    """
    try:
        data = json.loads(request.body)
        result = supabase.insert('products', data)
        return JsonResponse({'status': 'success', 'data': result})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_http_methods(["PUT"])
def supabase_update_product(request, product_id):
    """
    Exemple d'API pour mettre à jour un produit dans Supabase
    """
    try:
        data = json.loads(request.body)
        result = supabase.update('products', data, {'id': f'eq.{product_id}'})
        return JsonResponse({'status': 'success', 'data': result})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_http_methods(["DELETE"])
def supabase_delete_product(request, product_id):
    """
    Exemple d'API pour supprimer un produit dans Supabase
    """
    try:
        result = supabase.delete('products', {'id': f'eq.{product_id}'})
        return JsonResponse({'status': 'success', 'data': result})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400) 