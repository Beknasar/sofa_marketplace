# Generated by Django 4.2.11 on 2024-04-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('in_stock', 'В наличии'), ('for_order', 'На заказ 30%')], default='in_stock', max_length=20, verbose_name='Наличие'),
        ),
    ]
