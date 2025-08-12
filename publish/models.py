from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now, verbose_name="Created Date")
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    slug = models.SlugField(max_length=200, verbose_name="Slug")

    def __str__(self):
        return f"{self.title} by {self.author}"
