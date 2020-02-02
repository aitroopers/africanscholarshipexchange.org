# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
from models import *
# Create your tests here.


class BlogTestCase(TestCase):

    def setUp(self):
       author =  TeamMember(first_name="John", last_name="Norton", position="CEO", about="He is the CEO of the company")
       author.save()
       category = Category(title="Machines", slug="machine")
       category.save()
       Blog.objects.create(
           title="Welcome!",
           body="<p>I'd like to welcome you home!</p>",
           pub_date= datetime.datetime.now(),
           category = category,
           author = author,
           thumbnail = "static/images/blog-8.jpg",
           intext_image = "static/images/blog-9.jpg"
       )

    def test_object_construction(self):
        # test model object is contructed
        member = Blog.objects.get(title="Welcome!")
        self.assertEqual(member.thumbnail, "static/images/blog-8.jpg")