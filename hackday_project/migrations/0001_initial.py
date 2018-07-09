# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=255)),
                ('family_photo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'family',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'groceries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('families_donated', models.ManyToManyField(to='hackday_project.Family')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='family',
            name='groceries',
            field=models.ManyToManyField(to='hackday_project.Grocery'),
        ),
    ]
