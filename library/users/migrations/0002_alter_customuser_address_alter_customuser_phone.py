# Generated by Django 5.1.4 on 2025-01-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
