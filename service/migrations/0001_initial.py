# Generated by Django 3.2.5 on 2021-07-24 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('meta_title', models.CharField(max_length=120, null=True)),
                ('slug', models.SlugField()),
                ('price', models.FloatField()),
                ('appointment', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('expiry_date', models.DateField(null=True)),
                ('packed_date', models.DateField(null=True)),
                ('blood_type', models.CharField(max_length=256)),
                ('service_type', models.CharField(choices=[('clinical microbiology', 'clinical microbiology'), ('clinical chemistry', 'clinical chemistry'), ('hematology', 'hematology'), ('blood bank', 'blood bank'), ('molecular diagnotics', 'molecular diagnotics'), ('reproductive biology', 'reproductive biology')], default='clinical microbiology', max_length=100)),
                ('description', models.TextField()),
                ('lab_name', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.lab')),
            ],
        ),
    ]
