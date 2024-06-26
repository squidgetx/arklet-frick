# Generated by Django 4.0.4 on 2023-07-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ark', '0003_set_defaults_in_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='ark',
            name='format',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ark',
            name='identifier',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ark',
            name='relation',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ark',
            name='source',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ark',
            name='title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ark',
            name='type',
            field=models.TextField(blank=True, default=''),
        ),
    ]
