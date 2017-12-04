# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171203_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='inicio')),
                ('description', models.TextField(blank=True, verbose_name='descricao')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'palestras',
                'verbose_name': 'palestra',
            },
        ),
    ]
