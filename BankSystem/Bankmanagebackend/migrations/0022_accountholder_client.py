# Generated by Django 3.0.8 on 2021-08-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankmanagebackend', '0021_remove_accountholder_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountholder',
            name='client',
            field=models.BooleanField(default=True),
        ),
    ]
