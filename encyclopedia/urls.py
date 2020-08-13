from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.look, name="look"),
    path("<str:title>", views.title, name="title"),
    path("/newPage", views.newPage, name="newPage"),
    path("/ranentry", views.ranentry, name="ranentry"),
    path("/entry", views.entry, name="entry"),
    path("/edit", views.edit, name="edit"),
    path("/search", views.search, name="search"),
    path("/saventry", views.saventry, name="saventry")
]
