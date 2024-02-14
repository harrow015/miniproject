# Generated by Django 4.1.7 on 2023-10-30 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_alter_cart_table_quantity_alter_cart_table_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('order_date', models.CharField(max_length=20)),
                ('order_time', models.CharField(max_length=20)),
                ('grandtotal', models.IntegerField()),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.register_table')),
            ],
        ),
    ]
