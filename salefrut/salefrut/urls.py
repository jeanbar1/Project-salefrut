from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("vendedor/", include("Usuario.urls")),
    path('admin/', admin.site.urls),
]
