# Generated by Django 3.1 on 2020-08-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0024_auto_20200826_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_movement',
            field=models.DateField(auto_now=True, verbose_name='Withdrawal date'),
        ),
    ]