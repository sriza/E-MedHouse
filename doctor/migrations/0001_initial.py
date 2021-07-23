# Generated by Django 3.2.5 on 2021-07-25 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('user_name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='none', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=200)),
                ('available_day', models.CharField(max_length=255)),
                ('specialist', models.CharField(max_length=200)),
                ('charge', models.FloatField()),
                ('contact_number', models.IntegerField()),
                ('nmc_number', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to=doctor.models.get_upload_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120)),
                ('contact_number', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(null=True)),
                ('payment', models.BooleanField(default=False)),
                ('appointment_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('fixed', 'Fixed'), ('completed', 'Completed')], default='booked', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fixed_on', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
