# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_about_tag_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of this location', max_length=48)),
                ('latitude', models.FloatField(help_text='The latitudes of the location')),
                ('longitude', models.FloatField(help_text='The longitude of the location')),
            ],
        ),
    ]
