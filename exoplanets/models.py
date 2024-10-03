from django.db import models

# Create your models here.

class Exoplanet(models.Model):
    name = models.CharField(max_length=250)
    details = models.TextField(max_length=500)
    img = models.URLField(max_length=500)

    def __str__(self):  
        return self.name