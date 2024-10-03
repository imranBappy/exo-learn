from django.contrib import admin
from .models import Exoplanet

# Register your models here.

@admin.register(Exoplanet)
class ExoplanetAdmin(admin.ModelAdmin):
    pass