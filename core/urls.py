# pylint: disable=missing-module-docstring

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Configuracion de la ruta de autenticacion con las vistas que trae django incluidas:
    path('', include('home.urls'), name="home"),
    
    path('login/', auth_views.LoginView.as_view(template_name="base/login.html"), name="login"),
    
    path('logout/', auth_views.LogoutView.as_view(template_name="base/login.html"), name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
