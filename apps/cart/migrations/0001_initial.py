# Generated by Django 4.2.6 on 2023-11-01 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_productcolors_productsizes_remove_product_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_finished', models.DateTimeField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('finished', 'Finished'), ('waiting', 'Waiting for payment')], default='active', max_length=10)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='PromotionalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('discount', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Promo code',
                'verbose_name_plural': 'Promo codes',
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=25)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='shop.product')),
            ],
            options={
                'verbose_name': 'Cart Product',
                'verbose_name_plural': 'Cart Products',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='promo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to='cart.promotionalcode'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
    ]
