from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import SocialMediaAccount, CustomUser

class Technology(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='technologies',
        verbose_name='User',
    )
    
    name = models.CharField('name', max_length=100, unique=True)
    description = models.TextField('description')
    experience_years = models.DecimalField('Years of Experience', max_digits=4, decimal_places=1, default=0)
    proficiency = models.IntegerField('Proficiency %', default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    
    logo = models.CharField(
        'Logo', 
        max_length=100, 
        choices=SocialMediaAccount.LOGO_CHOICES,
        blank=True,
        null=True,
        default=None,
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
              
class Project(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='projects',
        verbose_name='User',
        default=None,
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField('description')
    technologies = models.ManyToManyField(Technology, related_name="projects")
    play_store_url = models.URLField(blank=True, null=True)
    app_store_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class OpenSourceContribution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField('description')
    technologies = models.ManyToManyField(Technology, related_name="contributions")
    repository_url = models.URLField('repository_url')
    package_url = models.URLField('package_url', blank=True, null=True)
    license = models.CharField('license', max_length=50, blank=True, default=None, null=True) 
    image = models.ImageField(upload_to='contribution_images/', blank=True, null=True, default=None, )
    
    def __str__(self):
        return self.name
    
class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    technologies = models.ManyToManyField(Technology, related_name="experiences",  default=None)
    projects = models.ManyToManyField(Project, related_name="experiences", blank=True, default=None)
    
    def save(self, *args, **kwargs):
        if self.end_date is None:
            self.is_current = True
        else:
            self.is_current = False
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']