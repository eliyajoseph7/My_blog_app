# Generated by Django 3.0.2 on 2020-06-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20200524_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]