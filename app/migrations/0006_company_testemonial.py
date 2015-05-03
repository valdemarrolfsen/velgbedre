# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_company_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='testemonial',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
