# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackday_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='groceries',
            field=models.ManyToManyField(to='hackday_project.Grocery', null=True, blank=True),
        ),
    ]
