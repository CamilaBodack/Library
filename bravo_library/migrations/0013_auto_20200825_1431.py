# Generated by Django 3.1 on 2020-08-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0012_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerbookmovement',
            name='status',
            field=models.CharField(blank=True, choices=[('D', 'Disponível'), ('E', 'Emprestado')], default='D', max_length=1),
        ),
    ]
