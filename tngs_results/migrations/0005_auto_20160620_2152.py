# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tngs_results', '0004_auto_20160620_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_list',
            name='capture_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='comments',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='ex_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='mody_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='profile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='sample_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sample_list',
            name='sequencing_panel_version',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
