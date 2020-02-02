# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.


admin.site.site_header = 'ASE administration'
admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(Location)
