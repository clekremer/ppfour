# Generated by Django 4.2.16 on 2024-09-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_appointment_approved_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('canceled', 'Canceled')], default='pending', max_length=10),
        ),
    ]
