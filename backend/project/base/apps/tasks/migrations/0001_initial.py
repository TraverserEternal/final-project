# Generated by Django 2.0.3 on 2018-12-04 09:12

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trackers', '0007_auto_20181203_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('finished', models.BooleanField(default=False, verbose_name='finished')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='load_tasks', to='trackers.Session', verbose_name='session')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
