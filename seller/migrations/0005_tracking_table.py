# Generated by Django 4.1.7 on 2023-11-06 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0008_payment_table'),
        ('seller', '0004_alter_product_table_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracking_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=20)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_table')),
            ],
        ),
    ]
