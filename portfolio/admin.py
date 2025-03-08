from django.contrib import admin
from .models import Technology, Project, OpenSourceContribution, WorkExperience
from .forms import TechnologyAdminForm

class TechnologyAdmin(admin.ModelAdmin):
    model = Technology
    form = TechnologyAdminForm
    
    list_display = ['name', 'description', 'experience_years', 'proficiency', 'logo', 'user']
    
    def logo(self, obj):
        return obj.get_logo_html() if obj.logo else '-'
    
    logo.short_description = 'Logo'
    logo.allow_tags = True
    
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    
    list_display = ['name', 'description', 'image', 'play_store_url', 'app_store_url', 'website_url', 'user']
    
    def logo(self, obj):
        return obj.get_logo_html() if obj.logo else '-'
    
    logo.short_description = 'Logo'
    logo.allow_tags = True

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(OpenSourceContribution)
admin.site.register(WorkExperience)
