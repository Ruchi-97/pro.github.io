# Generated by Django 3.1.2 on 2021-03-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0003_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=60)),
            ],
        ),
    ]