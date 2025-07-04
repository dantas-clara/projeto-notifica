from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from searchApp.models import Profile
from searchApp.forms.UserProfileForm import UserProfileForm, UserForm



def list_profile_view(request, id=None):
    profile = None


    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()

    elif not request.user.is_authenticated:

        return redirect(to='/')

    context = {
        'profile': profile,

    }
    return render(request, template_name='profile/profile.html', context=context, status=200)


@login_required()
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    emailUnused = True

    message = None

    if request.method == 'POST':
        profileForm = UserProfileForm(request.POST, request.FILES
                                      , instance=profile)
        userForm = UserForm(request.POST, instance=request.user)
        verifyEmail = Profile.objects.filter(user__email=request.
                                             POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None

    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid() and emailUnused:
        profileForm.save()
        userForm.save()

        message = {'type': 'success', 'text': 'Dados atualizados com sucesso' }

    else:
       if request.method == 'POST':
           if emailUnused:
            message = {'type': 'warning', 'text': 'Dados inválidos' }

       else:
            message = {'type': 'warning', 'text': 'E-mail já usado por outro usuário'}


    context = {
        'profileForm': profileForm,
        'userForm': userForm,
        'message' : message,
    }

    return render(request, template_name='user/profile.html', context=context, status=200)



