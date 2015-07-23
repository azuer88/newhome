from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse

from models import News, Article, Section


def get_context(request, extra=None):
    me = about_me()
    mydict = {
        "pagetitle": "azuer88.org",
        "META": settings.META,
        "navitems": navitems(),
        "news": get_news(),
        "articles": get_articles()
    }
    if extra:
        mydict.update(extra)
    if me:
        mydict['aboutme'] = me

    return RequestContext(request, mydict)

def article(request, article_id):
    return render(request, 'single_column.html', context=get_context(request))

def section(request, section_name):
    context = get_context(request,
        {
            "articles": get_articles(),
            "pagetitle": "azuer88.org - {}".format(section_name),
        }
    )
    return render(request, 'index.html', context=context)

def navitems():
    sections = Section.objects.filter(active=True).order_by('order', 'name')
    items = [{"url": reverse('home-index'), "title": "Home"},]
    for s in sections:
        if s.article_set.count():
            items.append(
                {
                    "url": reverse("home-section",args=[s.name.lower()]),
                    "title": s.name,
                }
            )
    return items


def about_me():
    active_news_with_order = News.objects.filter(active=True, order__gte=1).order_by('order')
    about_me_record = list(active_news_with_order[:1])
    if about_me_record:
        return about_me_record[0]
    return None


def get_news():
    return News.objects.filter(active=True, order=0).order_by('-pub_date')[:5]


def get_articles():
    return Article.objects.filter(active=True).order_by('-pub_date')[:5]


def index(request):
    context = get_context(request)
    return render(request, 'index.html', context)