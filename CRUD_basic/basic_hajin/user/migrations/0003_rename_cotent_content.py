# Generated by Django 4.0.5 on 2022-06-20 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_cotent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cotent',
            new_name='Content',
        ),
    ]