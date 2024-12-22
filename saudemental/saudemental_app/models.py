from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione outros campos que você deseja armazenar
    # Exemplo: bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username