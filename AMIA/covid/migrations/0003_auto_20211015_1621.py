# Generated by Django 3.1.5 on 2021-10-15 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_auto_20211015_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccinekind',
            old_name='one_component',
            new_name='is_one_component',
        ),
    ]
