# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.CharField(max_length=40)),
                ('score', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
    ]
