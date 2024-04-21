from django.urls import path
from . import views

app_name = 'flightApp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('find-flights/', views.find_flights, name='find_flights'),
    path('save-reservation/', views.save_reservation, name='save_reservation'),
]