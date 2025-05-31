from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Usuário')
)

STATUS_CHOICES = (
    (1, 'Solteiro(a)'),
    (2, 'Casado(a)'),
    (3, 'União estável'),
    (4, 'Divorciado(a)'),
    (5, 'Viúvo(a)')
)

EDUCATION_CHOICES= (
    (1, 'Fundamental 9º ano'),
    (2, 'Ensino Secundário, 12º ano'),
    (3, 'Graduação'),
    (4, 'Pós-graduação')
)

from .State import State
from .City import City
from .Neighborhood import Neighborhood
from .Address import Address
from .Profile import Profile
