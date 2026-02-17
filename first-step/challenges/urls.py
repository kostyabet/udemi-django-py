from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.month_int),
    path("<str:month>", views.month, name='month-challenge'),
    path("", views.index, name='index'),
]