from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("create/", views.index, name="create"),
    path("", views.index, name="index"),
    path("update/", views.index, name="update"),
    path("delete/", views.index, name="delete"),
]
