# Generated by Django 3.1.2 on 2021-03-18 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_answers_r1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='r1',
            new_name='idd',
        ),
    ]
