from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField() #null = false, blank = false
    categories = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reaction_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']