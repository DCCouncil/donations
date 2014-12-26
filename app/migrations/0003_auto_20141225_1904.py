# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_donation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='p', max_length=1),
            preserve_default=True,
        ),
    ]
