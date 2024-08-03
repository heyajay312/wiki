from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.getEntry, name="getEntry"),
    path("search", views.search, name='search'),
    path("new", views.new_page, name="newPage"),
    path("edit/<str:title>", views.edit, name="edit"),
    path('random/', views.random, name='randomPage')
]
