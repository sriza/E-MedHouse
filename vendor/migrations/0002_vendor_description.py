# Generated by Django 3.1.3 on 2021-07-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
