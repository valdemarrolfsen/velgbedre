# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='product',
            field=models.ImageField(upload_to='products/%Y/%m/%d', default=None),
            preserve_default=False,
        ),
    ]
