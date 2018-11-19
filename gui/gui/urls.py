from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .view import redirect_view

urlpatterns = [
    path('',  redirect_view),
    path('administracao/', include('administracao.urls')),
    path('usuario/', include('user.urls')),
]
