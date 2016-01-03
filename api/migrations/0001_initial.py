# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creditcard',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=50)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]
