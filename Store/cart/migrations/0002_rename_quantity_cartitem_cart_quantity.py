# Generated by Django 4.2.3 on 2023-10-24 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantity',
            new_name='cart_quantity',
        ),
    ]
