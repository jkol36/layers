from django.contrib import admin
from .models import Project, Photo, Project_Applicant

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'client', 'budget_min', 'budget_max', 'due_date', 'project_status', 'time_stamp']

class ApplicantAdmin(admin.ModelAdmin):
	list_display = ['designer', 'project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo)
admin.site.register(Project_Applicant, ApplicantAdmin)


