from django.urls import path
from searchApp.views.UsuarioView import list_users_view


urlpatterns = [
    path("", list_users_view, name='users'),
   #path("admin/dashboard/", dashboard_view, name='admin-dashboard'),
]
