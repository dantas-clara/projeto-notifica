from django.forms import ModelForm
from django import forms
from searchApp.models.Profile import Profile
from django.contrib.auth.models import User

# Estou usando a model Profile como base

class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):  # __init__ é o construtor
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and getattr(self.instance, 'role', None) != 1:
            if 'role' in self.fields:
                del self.fields['role']

    class Meta:  # Criando um formulário baseado na model Profile
        model = Profile
        # fields = '__all__'
        exclude = ('name', 'image', 'addresses',)

        widgets = {  # Adicionando classes CSS com widgets
            # 'token': forms.Textarea(attrs={'class': "form-control"}),
            'user': forms.HiddenInput(),  # Oculta o campo no formulário
            'role': forms.Select(attrs={'class': "form-control"}),  # Removido type="date", pois não faz sentido aqui
            'password': forms.PasswordInput(),
            'date': forms.DateInput(attrs={"type": "date"}),
            'birthday': forms.DateInput(attrs={"type": "date"}),
            'address': forms.TextInput(attrs={'class': "form-control"}),
            'health_information': forms.Textarea(attrs={'class': "form-control"}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
        }































"""
class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs): #__init__ é o construtor
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

#caso o usuário n]ão sej ao admin, o "del self.files['rol'] deleta o campo role, caso o usuário não seja o admin.

    class Meta: #usamos essa classe, pois estamos criando um formulário baseado em uma model(profile) do sistema
        model = Profile
        #fields = '__all__'
        exclude = ('name', 'image', 'addresses',)

        widgets = { #classe usada para add uma class css
            'token': forms.Textarea(attrs={'class': "form-control"}),
            'user': forms.HiddenInput(), #o hiddenInput é usado para modificarum campo do formulário
            'role': forms.Select(attrs={'class': "form-control", "type": "date"}),
            'password': forms.PasswordInput(),
            'date': forms.DateInput(attrs={"type": "date"}),
            'birthday': forms.DateInput(attrs={"type": "date"}),
            'address': forms.TextInput(attrs={'class': "form-control"}),
            'health_information': forms.Textarea(attrs={'class': "form-control"}),
        }
                                    #o form-control é uma class do framework bootstrap

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
        }
"""