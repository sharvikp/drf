# Generated by Django 4.0.4 on 2022-05-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='intro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='video_link',
            field=models.CharField(max_length=100),
        ),
    ]
