# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_auto_20160703_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='createrecdata',
            name='URL_to_Poster_or_Video',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(),
        ),
    ]
