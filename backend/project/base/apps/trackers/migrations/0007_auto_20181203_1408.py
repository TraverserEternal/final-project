# Generated by Django 2.0.3 on 2018-12-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0006_auto_20181128_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='file'),
        ),
    ]