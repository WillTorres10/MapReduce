from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'administracao'
urlpatterns = [
    path('', views.verifica, name="padrao")
]