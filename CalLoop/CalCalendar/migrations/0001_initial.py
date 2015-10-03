# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('due_date', models.DateTimeField()),
                ('due_in', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, choices=[(b'Mon', b'Monday'), (b'Tues', b'Tuesday'), (b'Wed', b'Wednesday'), (b'Thurs', b'Thursday'), (b'Fri', b'Friday'), (b'Sat', b'Saturday'), (b'Sun', b'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('weekday', models.ManyToManyField(to='CalCalendar.Day')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(to='CalCalendar.Subject'),
        ),
    ]
