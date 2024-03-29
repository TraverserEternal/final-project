# Generated by Django 2.0.3 on 2018-12-03 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_member_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='team.Team', verbose_name='team'),
        ),
    ]
