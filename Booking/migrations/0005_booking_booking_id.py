# Generated by Django 2.1.1 on 2018-11-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_auto_20181113_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(default='000000', editable=False, max_length=6, unique=True),
        ),
    ]
