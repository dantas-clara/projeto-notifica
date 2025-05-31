from django.urls import path
from searchApp.views.ProfileView import list_profile_view, edit_profile

urlpatterns = [
    path('', list_profile_view, name='profiles'),
    path('<int:id>/', list_profile_view, name='profile'),
    path('edit/', edit_profile, name='edit-profile'),
]

#o 'name=...' são os nomes dinâmicos no link. Permitem que um link seja alterado sem precisar trocá-lo.
#o name será como uma variável e utiliza esse nome nos arquivos de html