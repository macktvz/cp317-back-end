# Generated by Django 3.2 on 2021-04-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudySpaceApi', '0016_auto_20210411_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]