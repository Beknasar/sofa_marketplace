# Generated by Django 4.2.11 on 2024-06-01 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_alter_orderproduct_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Запись заказа', 'verbose_name_plural': 'Записи заказов'},
        ),
    ]
