# Generated by Django 3.1.7 on 2021-04-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_sender_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
