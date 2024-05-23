"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from registrosABM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registrarPersona/', views.registrarPersona),
    path('edicionPersona/<dni_pasaporte>', views.edicionPersona, name='edicionPersona/<dni_pasaporte>'),
    path('editarPersona/', views.editarPersona),
    path('eliminarRegistro/<dni_pasaporte>', views.eliminarRegistro, name='eliminarRegistro'),
    path('dnis-registrados/', views.dnis_registrados, name='dnis_registrados'),
    path('buscar_resultados/', views.buscar_resultados, name='buscar_resultados'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    
]
