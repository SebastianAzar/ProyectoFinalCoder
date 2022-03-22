from django.urls import path
from AppCoder import views
from .views import inicio, categoria, auto, equipo, busqueda_auto # No olvidarse de esto!!


urlpatterns = [
    path('', views.inicio, name="inicio"), # Inicio de nuestra página
    path('categoria', views.categoria, name="categoria"),
    path('auto', views.auto, name="auto"),
    path('equipo', views.equipo, name="equipo"),
    path('busqueda-auto', views.busqueda_auto, name = "busqueda_auto")
]

