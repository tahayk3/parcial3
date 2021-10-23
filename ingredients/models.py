from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    personas = models.CharField(max_length=100)

    def __str__(self):
        return self.name

