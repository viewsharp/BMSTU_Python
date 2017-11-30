# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='bookstall/static/books'),
        ),
    ]
