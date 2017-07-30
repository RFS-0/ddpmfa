# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpmfa', '0003_auto_20170730_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='id',
        ),
        migrations.RemoveField(
            model_name='model',
            name='name of the model',
        ),
        migrations.AddField(
            model_name='model',
            name='description',
            field=models.TextField(default='This is a very detailed description of this model!', verbose_name='Description of this model'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model',
            name='name',
            field=models.CharField(default='Name of test model', max_length=250, primary_key=True, serialize=False, verbose_name='name of the model'),
            preserve_default=False,
        ),
    ]
