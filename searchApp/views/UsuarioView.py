from django.contrib.auth.decorators import login_required
#from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from searchApp.models import Profile
#from searchApp.models.Profile import Profile
from django.db import transaction, IntegrityError
from django.db.models import Q
from django.core.paginator import Paginator


#users = Profile.objects.filter(role=2).order_by('id')

@login_required()
def list_users_view(request):
    #global parameters
    name = request.GET.get("name")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")
    #users = Profile.objects


    users = Profile.objects.all()

    if name is not None and name != '':
        users = users.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))

    if neighborhood is not None:
        users = users.filter(addresses__neighborhood__id=neighborhood)
    elif city:
        users = users.filter(addresses__neighborhood__city__id=city)
    elif state: #is not None:
        users = users.filter(addresses__neighborhood__city__state__id=state)

    #if len(users) > 0:
    paginator = Paginator(users, 8)
    page = request.GET.get('page')
    users = paginator.get_page(page) #get_page verifica qual pág foi selecionada pelo usuário

    get_copy = request.GET.copy() #get.copy copia os parâmetros da url
    parameters = get_copy.pop('page', True) and get_copy.urlencode() #get_copy.urlencod trará o resultado: page=2&page=1&name=&speciality=1&state=1&city=1&neighb orhood=1


    context = {
        'users': users,
        'parameters': parameters
    }

    return render(request, template_name='usuario/usuarios.html', context=context, status=200)




#deletando um usuário
try:
    profile = Profile.objects.filter(user__id=3).first()
    if profile is not None:
        profile.user.delete()
    else:
        print('Nenhum perfil com user_id=3 foi encontrado.')

except Exception as erro:
    print("Erro. Descrição %s" % erro)




#UPDATE
try:
    with transaction.atomic():
        profile = Profile.objects.filter(id=1).first()

        if profile is not None:
            profile.role = 3 #as 3 opções que têm
            profile.user.first_name = "Ana"
            profile.user.last_name = "Souza (está no usuarioview)"

            #Atualizando a tabela de Profile e User juntas
            profile.save()
            profile.user.save() #aciona o obj 'USER' sem precisar fazer um query direto
        else:
            print("Nenhum profile com id=1 foi encontrado.")

except IntegrityError as erro:
    print("Erro. Descrição %s" % erro)














