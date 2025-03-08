from django.shortcuts import render, Http404
from accounts.models import CustomUser

def simpleIndex(request):
   return render(request, 'index.html')



def index(request, username):
    user_queryset = CustomUser.objects.filter(username=username)
        
    if not user_queryset.exists():
        raise Http404("User does not exist")
    
    user = user_queryset.first()
    
    title = f"{user.first_name} {user.last_name}" if user.first_name else user.username.upper()
    
    socialMediaAccount = list(user.get_social_media_accounts())
    technologySkills = list(user.get_technology_skills())
    projects = list(user.get_projects())
    
    return render(request, 'portfolio.html', context={
        'user': user,
        'title': title,
        'socialMediaAccounts': socialMediaAccount,
        'technologySkills': technologySkills,
        'projects': projects,
    })

