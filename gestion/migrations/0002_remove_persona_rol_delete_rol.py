# Generated by Django 4.2 on 2023-10-01 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]