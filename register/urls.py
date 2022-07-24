from django.contrib import admin
from django.urls import path
from register import views

app_name='register'
urlpatterns = [
    ###Estas son las URLs del template add
    path("menu/", views.menu, name="menu"),
    
    path("add/", views.addcitizen, name="add"),
    path("edit/<int:citizen_id>", views.editcitizen, name="edit"),
    path("delete/<int:citizen_id>", views.deletecitizen, name="delete"),


    #####################################################################
    path("addspace/", views.addspace, name="addspace"),
    path("editcity/<int:city_id>", views.editcity, name="editcity"),
    path("deletecity/<int:city_id>", views.deletecity, name="deletecity"),
    ######################################################################
    path("editstate/<int:state_id>", views.editstate, name="editstate"),
    path("deletestate/<int:state_id>", views.deletestate, name="deletestate"),
    
]