# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='generic_name',
            field=models.CharField(max_length=255),
        ),
    ]