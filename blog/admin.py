from django.contrib import admin
from .models import Post, Category, Tag, Comment
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='extends'
            )
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'status', 'publish_date', 'views', 'created_at')
    list_filter = ('status', 'categories', 'tags', 'publish_date', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views', 'created_at', 'updated_at')
    filter_horizontal = ('categories', 'tags')
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'slug', 'author', 'status', 'publish_date')
        }),
        ('Contenu', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('Catégories et Tags', {
            'fields': ('categories', 'tags')
        }),
        ('Statistiques', {
            'fields': ('views',),
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    list_per_page = 20
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Nombre d\'articles'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Nombre d\'articles'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'content', 'post__title')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
