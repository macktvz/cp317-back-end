# Generated by Django 3.2 on 2021-04-10 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudySpaceApi', '0012_auto_20210409_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='picture',
        ),
    ]
