# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='logos/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model,),
        ),
    ]
