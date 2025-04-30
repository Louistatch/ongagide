from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('Administration AGIDE')
admin.site.site_title = _('Administration AGIDE')
admin.site.index_title = _('Bienvenue dans l\'administration AGIDE')

# Personnalisation du style
admin.site.enable_nav_sidebar = False 