# Generated by Django 4.2.7 on 2023-11-19 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flovour',
            new_name='Flavour',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='flovour',
            new_name='flavour',
        ),
    ]
