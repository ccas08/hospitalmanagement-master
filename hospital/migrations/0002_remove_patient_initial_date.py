# Generated by Django 3.0.5 on 2022-06-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='initial_date',
        ),
    ]
