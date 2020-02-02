# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from home.models import TeamMember
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    def __unicode__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100, unique=True, help_text="Blog title. Maximum 100 characters")
    body = HTMLField(help_text="Blog body")
    pub_date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Create a category for the blog")
    author = models.ForeignKey(TeamMember, on_delete=models.CASCADE, help_text="Author(s)")
    thumbnail = models.ImageField(upload_to="static/images/student/blogs", help_text="thumnail image")
    intext_image = models.ImageField(upload_to="static/images/student/blogs", help_text="An in-text image")
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']