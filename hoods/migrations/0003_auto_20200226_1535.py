# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-26 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0002_profile_neighbor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='health',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='police',
            field=models.CharField(max_length=200),
        ),
    ]