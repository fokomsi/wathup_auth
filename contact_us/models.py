from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    traite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return f"{self.nom} - {self.sujet}"