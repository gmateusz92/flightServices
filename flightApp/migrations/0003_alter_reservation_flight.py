# Generated by Django 5.0.1 on 2024-04-20 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_alter_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.flight'),
        ),
    ]
