from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
