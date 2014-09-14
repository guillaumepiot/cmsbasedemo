import os
from django.contrib.sites.models import Site
from django.conf import settings

def website_settings(request):
    
    site = Site.objects.get_current()

    data = {
        'SITE_NAME': site.name,
        'SITE_DOMAIN': site.domain,
        'AUTHOR': settings.AUTHOR,
        'AUTHOR_URL': settings.AUTHOR_URL,
        'MULTILINGUAL': settings.PREFIX_DEFAULT_LOCALE,
    }
    
    return data