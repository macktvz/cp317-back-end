# Generated by Django 3.1.7 on 2021-03-27 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudySpaceApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstName',
        ),
    ]
