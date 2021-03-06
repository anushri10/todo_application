# Generated by Django 2.2.1 on 2019-05-27 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2019, 5, 27, 13, 8, 32, 378112, tzinfo=utc), editable=False)),
            ],
            options={
                'ordering': ['join_date'],
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_job', models.TextField(max_length=255)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('completed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 5, 27, 13, 8, 32, 378861, tzinfo=utc), editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.User')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
    ]
