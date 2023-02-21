from xml.parsers.expat import model
from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "complete", "created"]



admin.site.register(Task, TaskAdmin)