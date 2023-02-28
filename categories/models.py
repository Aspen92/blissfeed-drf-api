from django.db import models


class Category(models.Model):
    """
    Model for posts categories.
    """
    category = models.CharField(max_length=60, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Category: {self.category}'
