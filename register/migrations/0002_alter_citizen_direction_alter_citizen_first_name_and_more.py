# Generated by Django 4.0.6 on 2022-07-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='direction',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='first_surnames',
            field=models.CharField(max_length=50, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='last_surnames',
            field=models.CharField(max_length=50, verbose_name='Segundo Apellido'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=50, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_name',
            field=models.CharField(max_length=50, verbose_name='Departamento'),
        ),
    ]