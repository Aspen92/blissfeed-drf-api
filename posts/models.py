from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner'.
    """
    image_filter_choices = [
        ('funny', 'Funny'),
        ('awesome', 'Awesome'),
        ('inspiration', 'Inspiration'),
        ('health', 'Health'),
        ('beautiful', 'Beautiful'),
        ('amazing', 'Amazing'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../post_default_cut8cb', blank=True)

    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
