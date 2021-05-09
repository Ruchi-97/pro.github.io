# Generated by Django 3.1.2 on 2021-03-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210324_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='level1data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(default='', max_length=60)),
                ('img_data', models.CharField(default='', max_length=60)),
                ('img_flag', models.CharField(default='', max_length=60)),
                ('img_src', models.ImageField(default='', upload_to='static/l3images')),
            ],
        ),
        migrations.CreateModel(
            name='level2data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(default='', max_length=60)),
                ('img_data', models.CharField(default='', max_length=60)),
                ('img_flag', models.CharField(default='', max_length=60)),
                ('img_src', models.ImageField(default='', upload_to='static/l3images')),
            ],
        ),
        migrations.DeleteModel(
            name='answers',
        ),
    ]
