# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
            bases=(models.Model,),
        ),
    ]
