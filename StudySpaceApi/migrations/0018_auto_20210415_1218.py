# Generated by Django 3.2 on 2021-04-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudySpaceApi', '0017_alter_posts_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='StudySpaceApi.user'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='StudySpaceApi.group'),
        ),
    ]
