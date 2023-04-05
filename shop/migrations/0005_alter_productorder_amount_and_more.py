# Generated by Django 4.1.7 on 2023-03-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_composition_rename_orders_order_productorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='shop.ProductOrder', to='shop.product'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
