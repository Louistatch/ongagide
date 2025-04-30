from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(verbose_name="Description")
    composition = models.TextField(verbose_name="Composition", blank=True)
    usage = models.TextField(verbose_name="Mode d'emploi", blank=True)
    benefits = models.TextField(verbose_name="Avantages", blank=True)
    image = models.ImageField(upload_to='products/', verbose_name="Image")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})
