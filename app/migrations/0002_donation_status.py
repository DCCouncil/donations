# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.CharField(default='p', choices=[('d', 'Draft'), ('p', 'Published')], max_length=1),
            preserve_default=False,
        ),
    ]
