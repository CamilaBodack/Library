# Generated by Django 3.1 on 2020-08-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0017_auto_20200825_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(default=0, max_length=1000, verbose_name='Book summary'),
        ),
    ]
