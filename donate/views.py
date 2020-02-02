# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import About
# Create your views here.


def donate(requests):
    about = About.objects.get(id=1)
    ase_summary = about.summary_text
    return render(requests, "donate/index.html", locals())