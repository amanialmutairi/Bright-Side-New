# Generated by Django 3.2.4 on 2021-06-28 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brightside', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient',
            new_name='profile',
        ),
    ]
