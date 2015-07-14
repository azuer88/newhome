from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse

from models import News


def navitems():
    return [
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
        {"url": reverse('home-index'), "title": "Home"},
    ]


def about_me():
    active_news_with_order = News.objects.filter(active=True, order__gte=1).order_by('order')
    about_me_record = list(active_news_with_order[:1])
    if about_me_record:
        return about_me_record[0]
    return None


def get_news():
    return News.objects.filter(active=True, order=0).order_by('-pub_date')


def index(request):
    me = about_me()
    mydict = {
        "pagetitle": "azuer88.org",
        "META": settings.META,
        "navitems": navitems(),
        "news": get_news(),
    }
    if me:
        mydict['aboutme'] = me

    context = RequestContext(request, mydict)
    return render(request, 'index.html', context)