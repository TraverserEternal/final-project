# Generated by Django 2.0.3 on 2018-11-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculations', '0002_auto_20181128_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='load',
            field=models.FloatField(verbose_name='player load (abs cumsum / 9.81)'),
        ),
    ]
