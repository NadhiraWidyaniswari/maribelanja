# Generated by Django 4.2.5 on 2023-09-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]