from django.shortcuts import render
from utils import icons_helper

def devicon_view(request):
    from django.shortcuts import render
    
    icons = icons_helper.get_devicon_list()
    
    return render(request, 'devicons.html', {
        'icons': icons,
        'total_icons': len(icons)
    })


def test(request):
    return render(request, 'test.html')