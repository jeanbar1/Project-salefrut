from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("vendedor/", include("Usuario.urls")),
    path("produto/", include("Produto.urls")),
    path('autenticacao/', include('autenticacao.urls')),
    
]