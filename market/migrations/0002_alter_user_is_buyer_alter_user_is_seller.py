# Generated by Django 4.0.2 on 2022-02-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_buyer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
