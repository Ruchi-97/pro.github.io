# Generated by Django 3.1.2 on 2021-04-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20210428_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level1data',
            name='img_data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='level1data',
            name='img_src',
            field=models.ImageField(default='', upload_to='static/l1images'),
        ),
        migrations.AlterField(
            model_name='level2data',
            name='img_data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='level2data',
            name='img_src',
            field=models.ImageField(default='', upload_to='static/l2images'),
        ),
        migrations.AlterField(
            model_name='level3data',
            name='img_data',
            field=models.TextField(),
        ),
    ]
