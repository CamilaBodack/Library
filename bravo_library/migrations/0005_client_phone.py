# Generated by Django 3.1 on 2020-08-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0004_auto_20200825_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default=0, max_length=50, verbose_name='Phone Number'),
        ),
    ]