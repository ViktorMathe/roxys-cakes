# Generated by Django 4.1.5 on 2023-02-27 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0005_alter_contact_us_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='answered',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
