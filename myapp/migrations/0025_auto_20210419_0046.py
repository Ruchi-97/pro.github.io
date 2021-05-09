# Generated by Django 3.1.2 on 2021-04-18 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20210416_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='ccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.CharField(default='', max_length=60)),
                ('count', models.IntegerField(default=3)),
                ('AdditionalCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
        migrations.AddField(
            model_name='ccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userinfo'),
        ),
    ]
