from django.db import models

# Create your models here.

class Logo(models.Model):
    nama = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')
    
    def __str__(self):
        return self.nama