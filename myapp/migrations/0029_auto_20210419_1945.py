# Generated by Django 3.1.2 on 2021-04-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20210419_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='level1',
            field=models.CharField(default='level1', max_length=60),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='level2',
            field=models.CharField(default='level2', max_length=60),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='level3',
            field=models.CharField(default='level3', max_length=60),
        ),
    ]
