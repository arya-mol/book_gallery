# Generated by Django 3.2.11 on 2022-02-24 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Item',
            new_name='item',
        ),
    ]
