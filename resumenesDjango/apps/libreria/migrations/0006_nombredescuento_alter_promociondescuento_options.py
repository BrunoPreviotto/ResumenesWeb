# Generated by Django 4.1.1 on 2022-10-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_promociondescuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='NombreDescuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'nombre_descuento',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='promociondescuento',
            options={'managed': False},
        ),
    ]
