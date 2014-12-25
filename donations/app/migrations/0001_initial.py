# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('donation_date', models.DateField(null=True, blank=True, verbose_name='Donation Date')),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('amount', models.CharField(max_length=200, null=True, blank=True)),
                ('donor', models.CharField(max_length=200, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('pub_date', models.DateTimeField(null=True, blank=True, verbose_name='date published')),
                ('created_by', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
