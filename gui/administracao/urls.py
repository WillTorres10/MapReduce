from django.http import HttpResponse
from django.urls import path

app_name = 'administracao'
urlpatterns = [
    path('', lambda req:HttpResponse("Hello World"))
]