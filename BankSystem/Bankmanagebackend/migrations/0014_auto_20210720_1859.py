# Generated by Django 3.0.8 on 2021-07-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankmanagebackend', '0013_auto_20210720_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateField(null=True),
        ),
    ]
