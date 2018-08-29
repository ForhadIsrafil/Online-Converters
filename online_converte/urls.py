"""online_converte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from online_converteApp.views import *
urlpatterns = [
    path('', home, name='home'),
    path('fraction/', fraction , name="fraction"),
    path('factorial/', factorial, name='factorial'),
    path('how_long_is_it/', how_long_is_it, name='how_long_is_it'),
    path('How_much_does_it_weigh/', weigh, name='weigh'),
    path('mmmv/', mmmv, name='mmmv'),
    path('random_no/', random_no, name='random_no'),
]
