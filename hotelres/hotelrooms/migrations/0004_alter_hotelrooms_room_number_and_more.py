# Generated by Django 5.1.3 on 2024-11-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelrooms', '0003_rename_hotel_id_hotelrooms_hotel'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrooms',
            name='room_number',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='hotelrooms',
            unique_together={('hotel', 'room_number')},
        ),
    ]