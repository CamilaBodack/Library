# Generated by Django 3.1 on 2020-08-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0021_book_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='delivery_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Delivery Date'),
        ),
    ]
