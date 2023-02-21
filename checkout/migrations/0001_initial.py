# Generated by Django 4.1.5 on 2023-01-25 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cakes', '0002_remove_cake_image_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(
                    editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=64)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=24)),
                ('city', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('county', models.CharField(
                    blank=True, max_length=50, null=True)),
                ('post_code', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(
                    max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bag_total', models.DecimalField(
                    decimal_places=2, default=0, max_digits=10)),
                ('delivery', models.DecimalField(
                    decimal_places=2, default=0, max_digits=8)),
                ('order_total', models.DecimalField(
                    decimal_places=2, default=0, max_digits=10)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('name', models.ForeignKey(
                    default=None, on_delete=django.db.models.deletion.CASCADE,
                    related_name='checkout_form',
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutLine',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(
                    decimal_places=2, editable=False, max_digits=6)),
                ('cake', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='cakes.cake')),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='lineitems', to='checkout.checkout')),
            ],
        ),
    ]
