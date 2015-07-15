from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix


class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    pub_date = models.DateField(default=datetime.now)

    def __unicode__(self):
        return "{} - {}".format(self.title, self.get_blurb())

    def get_blurb(self):
        return smart_truncate(self.content)

    class Meta:
        verbose_name_plural = "News"

class Section(models.Model):
    name = models.CharField(max_length=30, default='')
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return "{}".format(self.name)

class Article(models.Model):
    title = models.CharField(max_length=30)
    teaser = models.TextField()
    content = models.TextField()
    pub_date = models.DateField(default=datetime.now)
    active = models.BooleanField(default=True)
    section = models.ForeignKey(Section, default=None)

    tags = TaggableManager()

    def __unicode__(self):
        return "{} - {}".format(self.title, self.get_blurb())

    def get_blurb(self):
        return smart_truncate(self.content)
