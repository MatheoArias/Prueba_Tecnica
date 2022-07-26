# Generated by Django 4.0.6 on 2022-07-24 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicative', models.IntegerField(unique=True, verbose_name='Indicativo')),
                ('state_name', models.CharField(max_length=50, unique=True, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, unique=True, verbose_name='Ciudad')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.state', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('cc', models.IntegerField(unique=True, verbose_name='C.C.')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Segundo Nombre')),
                ('first_surnames', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('last_surnames', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('direction', models.CharField(max_length=100, verbose_name='Dirección')),
                ('tel_number', models.IntegerField(verbose_name='Teléfono Fijo')),
                ('cel_number', models.IntegerField(verbose_name='Teléfono Celular')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.city', verbose_name='Ciudad')),
                ('id_indicative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.state', verbose_name='Departamento')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Habitante',
                'verbose_name_plural': 'Habitantes',
            },
        ),
    ]
