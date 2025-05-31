from django.urls import path
from searchApp.views.HomeView import home_view


urlpatterns = [
    path('', home_view),
]