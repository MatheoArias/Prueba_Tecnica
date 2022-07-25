from django.db import models
from django.contrib.auth.models import User


""" Defino el Modelo Departamento
Ex: Antioquia-Atlántico"""


class State(models.Model):
    indicative = models.IntegerField(
        verbose_name="Indicativo", blank=False, unique=True)
    state_name = models.CharField(
        ("Departamento"), max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamento"

    def __str__(self):
        return f'{self.state_name}'


""" Defino el Modelo Ciudad
Ex: Medellín-Barranquilla-Bogotá """


class City(models.Model):
    state = models.ForeignKey(
        State, verbose_name="Departamento", blank=False, on_delete=models.CASCADE)
    city_name = models.CharField(
        ("Ciudad"), max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return f'{self.city_name}'


""" Defino el Modelo Habitante"""


class Citizen(models.Model):
    date = models.DateField(auto_now_add=True)
    cc = models.IntegerField(blank=False, verbose_name="C.C.", unique=True)
    city = models.ForeignKey(City, verbose_name="Ciudad",
                             blank=False, on_delete=models.CASCADE)
    id_indicative = models.ForeignKey(
        State, verbose_name="Departamento", blank=False, on_delete=models.CASCADE)
    first_name = models.CharField(
        ("Primer Nombre"), max_length=50, blank=False)
    last_name = models.CharField(("Segundo Nombre"), max_length=50, blank=True)
    first_surnames = models.CharField(
        ("Primer Apellido"), max_length=50, blank=False)
    last_surnames = models.CharField(
        ("Segundo Apellido"), max_length=50, blank=False)
    direction = models.CharField(("Dirección"), max_length=100, blank=False)
    tel_number = models.IntegerField(blank=False, verbose_name="Teléfono Fijo")
    cel_number = models.IntegerField(
        blank=False, verbose_name="Teléfono Celular")

    class Meta:
        verbose_name = "Habitante"
        verbose_name_plural = "Habitantes"

    def __str__(self):
        return f'{self.first_name} { self.last_name} {self.first_surnames} {self.last_surnames}'
