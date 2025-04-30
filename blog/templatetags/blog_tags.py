from django import template
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from django.template.defaultfilters import truncatewords

register = template.Library()

@register.filter
def truncate_html(value, length):
    """Tronque le HTML en gardant les balises valides"""
    if not value:
        return ''
    # Supprimer les balises HTML
    text = strip_tags(value)
    # Tronquer le texte
    return truncatewords(text, length)

@register.filter
def get_comment_count(post):
    """Retourne le nombre de commentaires actifs pour un post"""
    return post.comments.filter(active=True).count()

@register.filter
def get_like_count(obj):
    """Retourne le nombre de likes pour un post ou un commentaire"""
    return obj.likes.count()

@register.filter
def is_liked_by(obj, user):
    """Vérifie si un utilisateur a liké un post ou un commentaire"""
    if not user.is_authenticated:
        return False
    return user in obj.likes.all()

@register.filter
def get_reply_count(comment):
    """Retourne le nombre de réponses à un commentaire"""
    return comment.replies.filter(active=True).count() 