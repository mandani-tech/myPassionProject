# Generated by Django 2.0.6 on 2020-01-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quenchApp', '0011_auto_20200105_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tax',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=100),
        ),
    ]
