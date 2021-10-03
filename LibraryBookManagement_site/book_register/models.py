from django.db import models

# Create book models.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre= models.CharField(max_length=50)
    height= models.CharField(max_length=15)
    publisher= models.CharField(max_length=100)

    class Meta:
       unique_together = ("name", "author","genre","height","publisher")