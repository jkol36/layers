from django.contrib import admin
from .models import Project, Photo

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'client', 'budget_min', 'budget_max', 'due_date', 'project_status']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo)

