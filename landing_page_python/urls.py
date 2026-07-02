"""
URL configuration for landing_page_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include # Importamos o 'include' para conectar outros arquivos de URL

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conexão com o App:
    # O primeiro argumento em branco '' significa a Raiz do site (ex: www.meusite.com/).
    # O include('site_python.urls') diz: "Se o usuário acessar a raiz ou qualquer subpasta que não seja o admin,
    # mande o Django olhar os caminhos que estão mapeados dentro de site_python/urls.py".
    path('home/', include('site_python.urls'))
]
