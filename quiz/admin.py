from django.contrib import admin
from .models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'exoplanet', 'options')  # Display fields in admin list view
    
   

# Register the Quiz model with the custom admin
admin.site.register(Quiz, QuizAdmin)
