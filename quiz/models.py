from django.db import models
from exoplanets.models import Exoplanet
import json


class Quiz(models.Model):
    question = models.CharField(max_length=250)
    exoplanet = models.ForeignKey(Exoplanet, on_delete=models.CASCADE, related_name='quizzes')
    options = models.TextField()
    def __str__(self):  
        return self.question