# Generated by Django 4.1.7 on 2023-10-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_table',
            name='Password',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
