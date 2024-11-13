from django.contrib import admin
from django.urls import path, include
from .views import home, form, save, update, delete

urlpatterns = [
    path("", home, name="url_home"),
    path("new/", form, name="url_new"),
    path("save/", save, name="url_save"),
    path("edit/<int:id>/", update, name="url_update"),
    path("delete/<int:id>/", delete, name="url_delete"),
    #path('search/', search, name='url_search'),
]
