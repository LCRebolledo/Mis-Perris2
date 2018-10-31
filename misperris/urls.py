"""misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from adopciones import views
from adopciones.views import*
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'',include('adopciones.urls')),
    url(r'^registrar$',views.registrar_list),
	url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^inicia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='perfiles/bienvenida.html'),
        name='profile'),
    url(r'^registrom/$', views.registrar_mascota, name="guarda_mascota"),
    url(r'^listar/$', mascota_lista, name="listar_mascota"),
    url(r'^somos/$', Somos_list, name="quienes_somos"),
	

	]