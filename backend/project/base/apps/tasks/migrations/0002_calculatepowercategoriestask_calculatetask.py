# Generated by Django 2.0.3 on 2018-12-04 12:48

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0008_file_filename'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatePowerCategoriesTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('finished', models.BooleanField(default=False, verbose_name='finished')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculate_power_categories_tasks', to='trackers.Session', verbose_name='session')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CalculateTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('finished', models.BooleanField(default=False, verbose_name='finished')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculate_tasks', to='trackers.Session', verbose_name='session')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]