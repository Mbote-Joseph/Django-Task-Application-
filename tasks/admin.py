from django.contrib import admin
from . import models

# Register your models here.
class Task(admin.ModelAdmin):
    list_display=('title', 'description', 'created_at', 'updated_at', 'completed')

admin.site.register(models.Tasks)