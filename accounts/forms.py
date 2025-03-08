from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, SocialMediaAccount
from utils.searchable_choice_field_widget import SearchableChoiceFieldWidget

class SocialMediaAccountAdminForm(forms.ModelForm):
    platform = forms.CharField(max_length=50)
    url = forms.URLField()
    
    def __init__(self, *args, **kwargs):
        super(SocialMediaAccountAdminForm, self).__init__(*args, **kwargs)
        
        # Get all logo choices from model
        logo_choices = []
        for icon_tuple in SocialMediaAccount.LOGO_CHOICES:
            icon_value = icon_tuple[0]
            icon_display = icon_value.replace('-', ' ').title()
            logo_choices.append((icon_value, icon_display))
        
        # Create the logo field with proper choices
        self.fields['logo'] = forms.ChoiceField(
            choices=logo_choices,
            required=False,
            widget=SearchableChoiceFieldWidget()
        )
        
        # Set the choices on the widget too
        self.fields['logo'].widget.choices = logo_choices
        
        # Get user choices for the select widget
        user_queryset = CustomUser.objects.all()
        self.fields['user'] = forms.ModelChoiceField(
            queryset=user_queryset,
            empty_label='Select a user',
            widget=SearchableChoiceFieldWidget()
        )
        
        # Set user choices on widget
        self.fields['user'].widget.choices = [(str(u.id), u.username) for u in user_queryset]
    
    class Meta:
        model = SocialMediaAccount
        fields = '__all__'
        
        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields =  '__all__'
