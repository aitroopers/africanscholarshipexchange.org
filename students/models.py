# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30, help_text="First Name")
    last_name = models.CharField(max_length=30, help_text="Last Name")
    about_short = models.CharField(max_length=200, help_text="A short description about this member. Maximum 200 characters")
    about_long = HTMLField(help_text="A long description about this member.")
    age = models.IntegerField(help_text="Age")
    country= models.CharField(max_length=100, help_text="Country of origin")
    degree = models.CharField(max_length=60, help_text="The degree the student is pursuing")
    profile_image = models.ImageField(upload_to="static/images/student/profiles")
    funding_goal = models.FloatField(help_text="Total amount needed")
    current_funding = models.FloatField(help_text="Current money raised")
    graduation_date = models.DateField(help_text="Year of graduation")
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)