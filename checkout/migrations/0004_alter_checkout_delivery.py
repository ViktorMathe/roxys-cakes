# Generated by Django 4.1.5 on 2023-01-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_checkout_address_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='delivery',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=6),
        ),
    ]
