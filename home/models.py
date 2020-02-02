# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class About(models.Model):
    tag_line = models.CharField(max_length=150, help_text="Home page tag line. Maximum 150 characters.")
    summary_text = models.CharField(max_length=400, help_text="A short summary about ASE. Maximum 400 characters.")
    description_text = HTMLField('Content', help_text="Description about ASE")
    def __unicode__(self):
        return self.summary_text

class TeamMember(models.Model):
    first_name = models.CharField(max_length=30, help_text="First Name")
    last_name = models.CharField(max_length=30, help_text="Last Name")
    position = models.CharField(max_length=48, help_text="What is his/her position at the company?")
    about = models.CharField(max_length=200, help_text="A short description about this member. Maximum 200 characters")
    profile_image = models.ImageField(upload_to="static/images/teamprofiles")
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)



class Location(models.Model):
    name = models.CharField(max_length=48, help_text="Name of this location")
    latitude = models.FloatField(help_text="The latitudes of the location")
    longitude = models.FloatField(help_text="The longitude of the location")
    def __unicode__(self):
        return self.name
