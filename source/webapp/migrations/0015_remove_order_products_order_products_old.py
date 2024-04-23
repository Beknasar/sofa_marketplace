# Generated by Django 4.2.11 on 2024-04-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products_old',
            field=models.ManyToManyField(blank=True, related_name='orders', through='webapp.OrderProduct', to='webapp.product', verbose_name='Продукты'),
        ),
    ]
