# Generated by Django 3.1.2 on 2021-04-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_level2data_img_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='level2data',
            name='img_id',
            field=models.IntegerField(default='0'),
        ),
    ]
