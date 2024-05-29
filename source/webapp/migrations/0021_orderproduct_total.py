# Generated by Django 4.2.11 on 2024-05-29 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Итоговый прайс'),
            preserve_default=False,
        ),
    ]
