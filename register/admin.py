from django.contrib import admin
from .models import State,City, Citizen

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=("state_name","indicative")
    fields=["state_name","indicative"]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("state","city_name")
    fields=["state","city_name"]



@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    fields=["cc","city","first_name","last_name","first_surnames","last_surnames","direction","tel_number","cel_number"]
    list_display=("cc","city","first_name","last_name","first_surnames","last_surnames","direction","tel_number","cel_number")
