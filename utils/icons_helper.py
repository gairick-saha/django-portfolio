import re
from django.core.cache import cache
import requests

def fetch_devicon_icons():
    url = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses
        icon_pattern = r'\.devicon-([a-zA-Z0-9-]+)(?:\:|\s)'
        icons = re.findall(icon_pattern, response.text)
        unique_icons = sorted(set(icons))
        return unique_icons
    
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error fetching Devicon CSS: {e}")
        return []

def get_devicon_list():
    cached_icons = cache.get('devicon_icons')
    if cached_icons:
        return cached_icons    
    icons = fetch_devicon_icons()
    cache.set('devicon_icons', icons, 60 * 60 * 24)
    return icons

