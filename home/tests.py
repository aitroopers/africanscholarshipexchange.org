# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.test import TestCase
from models import *
# Create your tests here.

class TeamMemberTestCase(TestCase):

    def setUp(self):
        TeamMember.objects.create(first_name="John", last_name="Norton", position="CEO", about="He is the CEO of the company")

    def test_object_construction(self):
        # test model object is contructed
        member = TeamMember.objects.get(position='CEO')
        self.assertEqual(member.first_name, "John")



class StudentTestCase(TestCase):

    def setUp(self):
        Student.objects.create(
            first_name="Jojo",
            last_name="Yaw",
            about_short="He is a cool kid",
            about_long="<p>He is something else. He really needs your help</p>",
            age = 18,
            country = "Uganda",
            profile_image = "static/images/s1.png",
            funding_goal = 6000,
            current_funding= 4000,
            graduation_date = datetime.datetime.now()
        )

    def test_object_construction(self):
        # test model object is contructed
        member = Student.objects.get(first_name="Jojo")
        self.assertEqual(member.age, 18)

