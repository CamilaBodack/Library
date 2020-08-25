# Generated by Django 3.1 on 2020-08-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bravo_library', '0011_auto_20200825_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bravo_library.registerbook')),
                ('book_movement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movement', to='bravo_library.registerbookmovement')),
            ],
        ),
    ]
