from django.urls import path
from . import views

urlpatterns = [
    path("", views.sudoku_solver, name="sudoku_solver"),
]