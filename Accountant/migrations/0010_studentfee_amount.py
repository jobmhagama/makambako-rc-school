# Generated by Django 4.0.1 on 2022-03-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountant', '0009_studenttransportfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfee',
            name='amount',
            field=models.FloatField(default=200000.0),
        ),
    ]
