# Generated by Django 4.2.11 on 2024-04-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_remove_order_products_order_products_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products_old',
            new_name='products',
        ),
    ]