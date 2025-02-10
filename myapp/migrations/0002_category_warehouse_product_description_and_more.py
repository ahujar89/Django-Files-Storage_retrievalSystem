# Generated by Django 5.1.5 on 2025-02-03 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='warehouse',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_units', models.PositiveIntegerField()),
                ('order_status', models.IntegerField(choices=[(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'Order Shipped'), (3, 'Order Delivered')], default=1)),
                ('status_date', models.DateField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
