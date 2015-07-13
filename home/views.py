from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse

def navitems():
    return [
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
    ]
# Create your views here.
def index(request):
    context = RequestContext(request, {
        "pagetitle": "azuer88.org",
        "META": settings.META,
        "navitems": navitems(),
    })
    return render(request, 'index.html', context)