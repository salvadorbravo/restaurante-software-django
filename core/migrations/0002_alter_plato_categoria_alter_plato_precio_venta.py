# Generated by Django 4.2.1 on 2023-06-16 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='categoria',
            field=models.CharField(choices=[('V', 'Veganos'), ('MV', 'Mas Vendidos'), ('N', 'Novedades'), ('G', 'Generales'), ('PC', 'Platos Caseros'), ('P', 'Pastas'), ('S', 'Sopas')], max_length=80),
        ),
        migrations.AlterField(
            model_name='plato',
            name='precio_venta',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
    ]