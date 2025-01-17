from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),  # Ruta para el home del dashboard
    path('graphs', views.graphs, name='graphs'),  # Ruta para el home del dashboard
    path('registers', views.registers, name='registers'),  # Ruta para el home del dashboard
    # path('settings/', views.dashboard_settings, name='dashboard_settings'),  # Ruta para configuraciones
]