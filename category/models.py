from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Category Name")
    description = models.TextField(verbose_name="Category Description")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Category Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
