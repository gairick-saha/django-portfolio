from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SocialMediaAccount
from .forms import CustomUserCreationForm, CustomUserChangeForm, SocialMediaAccountAdminForm
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'primary_phone_number', 'secondary_phone_number']
    fieldsets = (
        ('Basic Details', {
            'fields': ['username', 'password' ]
        }),
        ('Personal Details', {
            'fields': ['first_name', 'last_name', 'address', 'designation', 'about']
        }),
        ('Contact Details', {
            'fields': ['email', 'primary_phone_number', 'secondary_phone_number']
        }),
        ('Profile Picture', {
            'fields': ['profile_picture']
        })
    )
    add_fieldsets = (
        ('Basic Details', {
            'fields': ['username', 'password', 'password2' ]
        }),
        ('Personal Details', {
            'fields': ['first_name', 'last_name', 'address', 'designation', 'about']
        }),
        ('Contact Details', {
            'fields': ['email', 'primary_phone_number', 'secondary_phone_number']
        }),
    )

class SocialMediaAccountAdmin(admin.ModelAdmin):
    model = SocialMediaAccount
    form = SocialMediaAccountAdminForm
    list_display = ('platform', 'user', 'logo', 'url')
    
    def logo(self, obj):
        return obj.get_logo_html() if obj.logo else '-'
    
    logo.short_description = 'Logo'
    logo.allow_tags = True

admin.site.site_header = 'Gairick Saha Portfolio Admin'
admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SocialMediaAccount, SocialMediaAccountAdmin)
