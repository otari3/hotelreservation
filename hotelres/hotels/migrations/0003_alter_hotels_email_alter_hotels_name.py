# Generated by Django 5.1.3 on 2024-11-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_hotels_email_hotels_password_alter_hotels_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='email',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
