# Generated by Django 3.0.2 on 2020-05-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_aboutme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='hobby',
            new_name='accomplish',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='skills',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='experiance',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='work',
            field=models.TextField(default='', null=True),
        ),
    ]
