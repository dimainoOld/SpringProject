# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='static/imageApp/images/no-img.jpg', upload_to='static/imageApp/images/')),
            ],
        ),
    ]