# Generated by Django 2.0.6 on 2020-01-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quenchApp', '0012_auto_20200105_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=100),
        ),
    ]
