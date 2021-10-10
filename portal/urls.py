"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    # адмінка
    path('admin/', admin.site.urls),
    # форма реєстрації або аутентифікації
    path('', views.main, name='main'),
    # реєстрація
    path('registration/', views.registration, name='registration'),
    # аутентифікація, якщо наявні крендшали
    path('authentication/', views.authentication, name='authentication'),
    path('index/', views.index, name = 'index')


]
