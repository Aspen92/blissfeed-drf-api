from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Post(models.Model):
    """
    Post model, related to 'owner'.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../post_default_cut8cb', blank=True)
    image_filter_choices = [
        ('2023', '2023'),
    ]
    image_filter = models.CharField(
        max_length=12, choices=image_filter_choices, default='normal'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
