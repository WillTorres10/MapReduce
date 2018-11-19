from django.urls import path, include
from . import views

app_name = 'usuario'
urlpatterns = [
    path('cadastrar/', views.signup, name="cadastrar"),
    path('acessar/', views.acessar, name="acessar"),
    path('sair/', views.logout_view)
]