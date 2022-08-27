from django.contrib.auth.models import AbstractUser
from django.db import models

'''
Modelo de Gremio
'''
class Gremio(models.Model):
    name = models.CharField(max_length=64)
    picture = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

'''
Modelo de usuario
'''
class User(AbstractUser):
    gremio = models.ForeignKey(Gremio, on_delete=models.CASCADE, related_name="miembros", blank=True , null=True)
    def __str__(self):
        return f"{self.username}"