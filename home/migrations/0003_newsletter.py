# Generated by Django 4.1.5 on 2023-02-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_subscribe_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('subscribers', models.CharField(max_length=124)),
                ('subject', models.CharField(max_length=124)),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]
