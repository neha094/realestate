# Generated by Django 3.1.4 on 2021-01-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210121_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='SuperArea',
            field=models.IntegerField(),
        ),
    ]