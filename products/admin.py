from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'composition', 'usage', 'benefits')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'slug', 'is_active')
        }),
        ('Description', {
            'fields': ('description', 'composition', 'usage', 'benefits')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
