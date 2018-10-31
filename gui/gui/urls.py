from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('usuario/', include('user.urls')),
]
