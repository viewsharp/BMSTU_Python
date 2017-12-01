# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstall', '0002_auto_20171130_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title', 'image', 'year')},
        ),
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='static/books'),
        ),
    ]