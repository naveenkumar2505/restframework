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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.FloatField()),
                ('product_color', models.CharField(max_length=20)),
            ],
        ),
    ]
