# Generated by Django 3.2.5 on 2021-07-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]