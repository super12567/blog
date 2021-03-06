# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=128, unique=True)),
                ('author', models.CharField(max_length=128)),
                ('publisher', models.CharField(max_length=128)),
                ('publicationdate', models.DateField()),
                ('printversion', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
