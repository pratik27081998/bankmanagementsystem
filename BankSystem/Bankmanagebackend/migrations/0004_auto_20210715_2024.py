# Generated by Django 3.0.8 on 2021-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankmanagebackend', '0003_auto_20210715_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountholder',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountholder',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
