# Generated by Django 3.1.7 on 2021-04-05 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudySpaceApi', '0005_auto_20210404_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_id', to='StudySpaceApi.group'),
        ),
    ]
