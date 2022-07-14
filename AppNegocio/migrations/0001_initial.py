# Generated by Django 4.0.5 on 2022-07-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_sku_art', models.CharField(max_length=50)),
                ('nombre_art', models.CharField(max_length=50)),
                ('familia_art', models.CharField(max_length=50)),
                ('stock_art', models.IntegerField()),
                ('costo_art', models.FloatField()),
                ('precio_venta_art', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cli', models.CharField(max_length=50)),
                ('tipo_cli', models.CharField(max_length=50)),
                ('direccion_cli', models.CharField(max_length=50)),
                ('fecha_alta_cli', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prov', models.CharField(max_length=50)),
                ('direccion_prov', models.CharField(max_length=50)),
                ('rubro_prov', models.CharField(max_length=50)),
                ('fecha_alta_prov', models.DateField()),
            ],
        ),
    ]