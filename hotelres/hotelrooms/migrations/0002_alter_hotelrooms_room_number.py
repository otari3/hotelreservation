# Generated by Django 5.1.3 on 2024-11-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrooms',
            name='room_number',
            field=models.IntegerField(unique=True),
        ),
    ]