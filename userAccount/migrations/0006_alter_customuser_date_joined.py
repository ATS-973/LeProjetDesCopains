# Generated by Django 4.0 on 2024-01-16 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0005_customuser_date_joined_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
