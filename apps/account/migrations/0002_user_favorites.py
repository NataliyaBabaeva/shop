# Generated by Django 4.2.6 on 2023-11-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productcolors_productsizes_remove_product_color_and_more'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]