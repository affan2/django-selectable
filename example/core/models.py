from __future__ import unicode_literals

try:
    from localflavor.us.models import USStateField
except ImportError:
    from django.contrib.localflavor.us.models import USStateField
from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Farm(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='farms')
    fruit = models.ManyToManyField(Fruit)

    def __unicode__(self):
        return "%s's Farm: %s" % (self.owner.username, self.name)


class City(models.Model):
    name = models.CharField(max_length=200)
    state = USStateField()

    def __unicode__(self):
        return self.name
