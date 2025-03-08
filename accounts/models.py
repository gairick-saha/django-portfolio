from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, URLValidator
from django.utils.safestring import mark_safe
from utils import icons_helper


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$', 
        message="Phone number must be a valid international format."
                "Start with + and country code, followed by 1-14 digits."
                "Example: +14155552671 or +911234567890"
    )
    
    primary_phone_number = models.CharField(
        'Primary phone number',
        validators=[phone_regex], 
        max_length=17, 
        blank=True, 
        null=True, 
        unique=True,
        default=None,
    )
    
    secondary_phone_number = models.CharField(
        'Secondary phone number',
        validators=[phone_regex], 
        max_length=17, 
        blank=True, 
        null=True, 
        unique=True,
        default=None,
    )
    
    address = models.CharField(
        'Address',
        blank=True, 
        null=True, 
        unique=True,
        default=None,
    )
    
    designation = models.CharField(
        'Designation',
        blank=True, 
        null=True, 
        unique=True,
        default=None,
    )
    
    about = models.CharField(
        'About',
        blank=True, 
        null=True, 
        unique=True,
        default=None,
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        null=True, 
        blank=True,
        verbose_name='Profile Picture'
    )

    def __str__(self):
        return self.username
    
    def get_social_media_accounts(self):
        return self.social_media_accounts.all()
    
    def get_technology_skills(self):
        return self.technologies.all()
    
    def get_projects(self):
        return self.projects.all()

class SocialMediaAccount(models.Model):
    LOGO_CHOICES = [
        (icon, icon) for icon in icons_helper.get_devicon_list()
    ]
    
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='social_media_accounts',
        verbose_name='User',
    )
    platform = models.CharField('platform', max_length=50)
    url = models.URLField(
        validators=[URLValidator()],
        verbose_name='url',
    )
    
    logo = models.CharField(
        'Logo', 
        max_length=100, 
        choices=LOGO_CHOICES,
        blank=True,
        null=True,
        default=None,
    )
    
    def get_logo_html(self):
        if not self.logo:
            return ''
        return mark_safe(f'<i class="devicon-{self.logo} colored"></i>')
        
    def get_logo_display(self):
        if not self.logo:
            return ''
        return mark_safe(f'<i class="devicon-{self.logo} colored"></i> {self.logo.replace("-", " ").title()}')

    def __str__(self):
        return f"{self.platform} - {self.user.username}"


