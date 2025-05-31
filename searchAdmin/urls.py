from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('searchApp.urls.HomeUrls')),
    path('', include('searchApp.urls.AuthUrls')),
    path('profile/', include('searchApp.urls.ProfileUrls')),
    path('users/', include('searchApp.urls.UsuarioUrls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


















