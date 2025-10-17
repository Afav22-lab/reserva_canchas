from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('canchas/', views.lista_canchas, name='lista_canchas'),
    path('reservar/<int:cancha_id>/', views.reservar_cancha, name='reservar_cancha'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar-reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
]
