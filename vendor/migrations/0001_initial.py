# Generated by Django 3.2.5 on 2021-07-26 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vendor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer'), (3, 'Doctor')], null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('shop_name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('business_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(default='none', max_length=10)),
                ('dob', models.DateField()),
                ('contact_number', models.IntegerField()),
                ('pan_number', models.CharField(max_length=10)),
                ('vat_number', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to=vendor.models.get_upload_path)),
                ('img_type', models.CharField(choices=[('profile', 'Profile Picture'), ('pan', 'PAN Card'), ('vat', 'VAT'), ('citizenship', 'Citizenship Card'), ('license', 'License')], default='license', max_length=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
