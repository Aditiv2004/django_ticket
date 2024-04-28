# Generated by Django 5.0.2 on 2024-03-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0009_alter_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='complaint_type',
            field=models.CharField(blank=True, choices=[('2', 'HARDWARE'), ('1', 'SOFTWARE')], default='', max_length=255),
        ),
    ]
