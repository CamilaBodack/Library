# Generated by Django 3.1 on 2020-08-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0008_auto_20200825_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('l', 'lent'), ('a', 'Available'), ('r', 'Reserved')], default='a', max_length=1),
        ),
    ]