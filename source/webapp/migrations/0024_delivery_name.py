# Generated by Django 4.2.11 on 2024-05-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_alter_delivery_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='name',
            field=models.CharField(default='Bob', max_length=100, verbose_name='Ответственный за доставку'),
            preserve_default=False,
        ),
    ]
