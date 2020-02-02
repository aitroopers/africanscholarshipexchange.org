# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180422_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-pub_date']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='posted',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='intext_image',
            field=models.ImageField(default=django.utils.timezone.now, help_text='An in-text image', upload_to='static/images/student/blogs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='/', help_text='thumnail image', upload_to='static/images/student/blogs'),
            preserve_default=False,
        ),
    ]
