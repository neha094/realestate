# Generated by Django 3.1.4 on 2021-01-21 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calcs', '0003_remove_calc_listin_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calc',
            old_name='email',
            new_name='Required',
        ),
    ]
