# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Student
from home.models import About
from random import shuffle

# Create your views here.
def students(requests):

    about = About.objects.get(id=1)
    website_name = "African Scholarship Exchange"
    title = "ASE | Students"
    ase_summary = about.summary_text
    tag_line = about.tag_line
    page = {"title": " Students", "name": "Students"}
    student_id = requests.GET.get('student')
    if student_id:
        student = Student.objects.get(id=int(student_id))
        return render(requests, "students/student_profile.html", locals())

    student_objects = Student.objects.all()
    students = [i for i in student_objects]
    shuffle(students)

    return render(requests, "students/index.html", locals())

